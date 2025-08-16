"""
Проверка и разбор ответов на все задачи
"""
import sympy as sp
import re

x = sp.symbols('x')



def parse_input(user_input: str):
    """
    Парсит ввод пользователя в sympy выражение
    Оптимизирует типы ответов:
    Принимается как правильный ответ 2x и 2*x; 1.5 и 1,5; 3 cos( 3 ) и 3cos(3); x=2 и 2; x**2 и x^2
    """

    # Убирает пробелы по краям строки и заменяет все запятые на точки для десятичных чисел
    s = user_input.strip().replace(',', '.')
    # Удаляет все пробелы внутри строки
    s = s.replace(' ', '')
    # Убирает префикс "x=" в начале строки если он есть
    s = re.sub(r'^x=', '', s)
    # Вставляет знак умножения (*) между цифрой и следующей за ней буквой или открывающей скобкой
    s = re.sub(r'(?<=\d)(?=[A-Za-z\(])', '*', s)
    # Вставка * между переменной/закрывающей скобкой и следующей переменной/функцией/открывающей скобкой
    s = re.sub(r'(?<=[A-Za-z\)])(?=[A-Za-z\(])', '*', s)
    # Замена ^ на ** для степени
    s = s.replace('^', '**')
    try:
        return sp.sympify(s)
    except Exception:
        return None


def normalize_logical_input(user_input: str) -> bool | None:
    """Преобразует логический ввод в bool значение / None при ошибке"""

    value = user_input.strip().lower()
    if value in ('да', 'true', 'истина', '1', 'yes'):
        return True
    if value in ('нет', 'false', 'ложь', '0', 'no'):
        return False
    return None


def check_answer(user_input: str, correct, q_type: int, params: dict):
    """
    Проверка ответа для всех задач всех сложностей

    При списке решений:
        Обрабатывает пустые списки [], "нет решений" и тд
        Пытается оценить ввод пользователя как Python список и сравнивает его
    При словарях (системы уравнений):
        Обрабатывает форматы ввода типа x=1, y=2 или 1, 2
        Использует params['vars'] для сопоставления значений с переменными
    При логических ответах:
        Нормализует ввод пользователя - "да", "нет", "true", "false" в bool значение
        Сравнивает нормализованное значение с правильным bool ответом
    При числовых/символьных выражениях:
        Парсит ввод пользователя с помощью функции parse_input
            Если ожидается числовой ответ - сравнивается введенное число с правильным ответом с учетом округления.
            Если ожидается символьное выражение - упрощается разница между вводом пользователя и правильным ответом.
    """

    # Проверка для списков решений
    if isinstance(correct, list):
        clean = user_input.strip().lower()
        if correct == []:
            if clean in ('[]', 'нет решений', 'решений нет'):
                return True, ''
            return False, ''
        try:
            user_list = eval(user_input, {})
        except Exception:
            return False, ''
        if user_list == correct:
            return True, ''
        return False, ''

    # Проверка для словарей (системы уравнений)
    if isinstance(correct, dict):
        vars_tuple = params.get('vars')
        if '=' in user_input:
            parts = user_input.replace(' ', '').split(',')
            user_sol = {}
            for part in parts:
                if '=' not in part:
                    return False, ''
                key, val_str = part.split('=', 1)
                val = parse_input(val_str)
                if val is None:
                    return False, ''
                sym = next((s for s in correct if str(s) == key), None)
                if sym is None:
                    return False, ''
                user_sol[sym] = val
            if user_sol == correct:
                return True, ''
            return False, ''

        if vars_tuple and ',' in user_input:
            vals = [v.strip() for v in user_input.split(',')]
            if len(vals) != len(vars_tuple):
                return False, ''
            user_sol = {}
            for sym, vstr in zip(vars_tuple, vals):
                val = parse_input(vstr)
                if val is None:
                    return False, ''
                user_sol[sym] = val
            if user_sol == correct:
                return True, ''
            return False, ''

        return False, ''

    # Проверка для логических ответов
    if isinstance(correct, bool):
        val = normalize_logical_input(user_input)
        if val is None:
            return False, ''
        if val == correct:
            return True, ''
        return False, ''

    # Парсинг ввода как выражения
    user_expr = parse_input(user_input)
    if user_expr is None:
        return False, ''

    # Числовая проверка + округление
    has_syms = hasattr(correct, 'free_symbols') and bool(correct.free_symbols)
    if not has_syms:
        try:
            user_val = float(user_expr)
            corr_val = float(correct)
        except Exception:
            pass
        else:
            m = re.match(r'^-?\d+[.,](\d+)$', user_input.strip())
            if m:
                decs = len(m.group(1))
                rounded = round(corr_val, decs)
                if abs(user_val - rounded) < 10**(-decs - 1):
                    return True, ''
            if abs(user_val - corr_val) < 1e-6:
                return True, ''
        return False, ''

    # Символьная проверка
    diff = sp.simplify(user_expr - correct)
    if diff == 0:
        return True, ''
    return False, ''