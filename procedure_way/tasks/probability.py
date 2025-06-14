""" 3) Вероятность и статистика"""

import random
import sympy as sp

from sympy import binomial


def generate_probability(diff):
    """
    Генерирует задачу по решению задач темы 3) Вероятность и статистика

    При diff == 1 - базовые задачи на вероятность - "хотя бы один раз" для монеты/кубика
    При diff == 2 - задачи на математическое ожидание, дискретное распределение
    При diff == 3 - задачи на вероятность по формуле Бернулли, биномиальное распределение

    Для каждой сгенерированной задачи: текст вопроса, правильный ответ, подсказка и объяснение.
    """
    if diff == 1:
        if random.choice([True, False]):
            n = random.randint(2,5)
            text = f"Вероятность получить орла хотя бы один раз при {n} подбрасываниях монеты?"
            ans = 1 - (1/2)**n
            hint = "Легче посчитать вероятность обратного события (ни одного орла)."
            explanation = f"Вероятность не получить орла ни разу при {n} подбрасываниях: (1/2)^{n}. Вероятность получить орла хотя бы один раз: 1 - (1/2)^{n} = {ans}."
        else:
            m = random.randint(2,4) # уменьшил диапазон для читаемости
            text = f"Вероятность выпадения 6 хотя бы один раз при бросании кубика {m} раз?"
            ans = 1 - (5/6)**m
            hint = "Какова вероятность НЕ получить 6 при одном броске? А при нескольких?"
            explanation = f"Вероятность не выпадения 6 при одном броске: 5/6. При {m} бросках: (5/6)^{m}. Вероятность выпадения 6 хотя бы один раз: 1 - (5/6)^{m} = {ans}."

    elif diff == 2:
        values = [random.randint(1, 6) for _ in range(3)]
        probs_raw = [random.randint(1, 10) for _ in range(3)]
        total = sum(probs_raw)
        # Преобразуем probs_raw в sp.Rational для внутренних расчетов,
        # но для отображения и итогового ответа - округленные значения
        probs_rational = [sp.Rational(p, total) for p in probs_raw]
        # Вычисляем точный ответ в Rational
        ans_rational = sum(v * p for v, p in zip(values, probs_rational))
        # Для вывода в тексте задачи округляем вероятности
        probs_display = [p.round(2) for p in probs_rational]
        text = f"Найдите мат. ожидание для значений {values} с вероятностями {probs_display}."
        # Округляем final_answer до 4 знаков после запятой
        final_answer_float = float(ans_rational)
        ans = round(final_answer_float, 4)
        hint = "Математическое ожидание - это сумма произведений значений на их вероятности."
        explanation = f"Математическое ожидание равно E(X) = Σ(xi * pi). Для данной задачи это будет {' + '.join(f'{v}*{p}' for v, p in zip(values, probs_display))} = {ans}."

    else:
        n = random.randint(5, 10)
        k = random.randint(1, n)
        p_val = random.choice([0.3, 0.4, 0.5, 0.6])
        p = sp.Rational(p_val)
        ans = binomial(n, k) * p**k * (1-p)**(n-k)
        text = f"Вероятность ровно {k} успехов в {n} испытаниях с p={p_val}."
        hint = "Используйте формулу Бернулли: C(n, k) * p^k * (1-p)^(n-k)."
        explanation = f"По формуле Бернулли, C({n}, {k}) * ({p_val})^{k} * ({1-p_val})^{n-k} = {binomial(n,k)} * {p_val**k} * {(1-p_val)**(n-k)} = {ans.round(6)}." # Округляем для вывода
    return {'text': text, 'answer': ans, 'params': {}, 'hint': hint, 'explanation': explanation}
