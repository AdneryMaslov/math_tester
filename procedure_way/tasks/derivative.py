""" 2) Мат анализ - Производная функции"""

import random
import sympy as sp

x = sp.symbols('x')


def generate_derivative(diff):
    """
    Генерирует задачу по решению задач темы 2) Мат анализ

    При diff == 1 - простые производные (степенные, синус/косинус без множителей x)
    При diff == 2 - цепочное правило, суммы функций
    При diff == 3 - более сложные функции, комбинации правил

    Для каждой сгенерированной задачи: текст вопроса, правильный ответ, подсказка и объяснение.
    """
    if diff == 1:
        if random.choice([True, False]):
            f = random.choice([2, 3, 5]) * x ** random.choice([2, 3])
            hint_text = "Вспомните правило производной степени: (x^n)' = n*x^(n-1)."
            explanation_template = "Для функции {f_str}, производная равна {ans_str} по правилу (c*x^n)' = c*n*x^(n-1)."
        else:  # Синус/косинус
            f = random.choice([1, 2, 3]) * sp.sin(x)
            hint_text = "Производная sin(x) равна cos(x)."
            explanation_template = "Для функции {f_str}, производная равна {ans_str}."

    elif diff == 2:
        if random.choice([True, False]):
            f = random.choice([-3, 4]) * sp.sin(2 * x + 1)
            hint_text = "Примените правило цепочки: (f(g(x)))' = f'(g(x)) * g'(x)."
            explanation_template = "Для функции {f_str}, используем правило цепочки. Внешняя функция sin(u), внутренняя 2x+1. Производная равна {ans_str}."
        else:
            f = random.choice([-2, 3]) * x ** random.choice([3, 4]) + random.randint(1, 5) * x
            hint_text = "Производная суммы равна сумме производных."
            explanation_template = "Для функции {f_str}, найдите производную каждого члена отдельно и сложите их. Производная равна {ans_str}."
    else:
        if random.choice([True, False]):
            f = random.choice([4, -5]) * sp.cos(-2 * x + sp.pi / 3)
            hint_text = "Не забудьте про знак при производной косинуса и правило цепочки."
            explanation_template = "Для функции {f_str}, производная cos(u) равна -sin(u)*u'. Здесь u = -2x + pi/3, u' = -2. В итоге {ans_str}."
        else:
            f = random.choice([-3, 2]) * (x - 1) ** random.choice([2, 3]) + sp.sin(x ** 2)
            hint_text = "Примените правило цепочки дважды и правило для суммы."
            explanation_template = "Для функции {f_str}, используйте правило цепочки для каждого члена. Производная (x-1)^n это n*(x-1)^(n-1). Производная sin(x^2) это cos(x^2)*2x. Итого: {ans_str}."

    ans = sp.diff(f, x)
    explanation_text = explanation_template.format(f_str=sp.sstr(f), ans_str=sp.sstr(ans))
    params = {'f': f}

    return {'text': f"Найдите производную функции f(x) = {sp.sstr(f)}", 'answer': ans, 'params': params,
            'hint': hint_text, 'explanation': explanation_text}
