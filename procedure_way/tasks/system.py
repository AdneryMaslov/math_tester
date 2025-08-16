""" 1) Алгебра - Решение систем уравнений"""

import random
import sympy as sp

x, y, z = sp.symbols('x y z')

def generate_system(diff):
    """
    Генерирует задачу по решению задач темы 1) Алгебра

    При diff == 1 - линейное уравнение
    При diff == 2 - система линейных уравнений с 2мя переменными
    При diff == 3 - система линейных уравнений с 3мя переменными

    Для каждой сгенерированной задачи: текст вопроса, правильный ответ, подсказка и объяснение.
    """
    if diff == 1:
        a = random.randint(1, 5)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)
        eq = sp.Eq(a * x + b, c)
        sol = sp.solve(eq, x)
        answer = sol[0] if sol else None

        text = f"Решите уравнение: {a}*x + {b} = {c}"
        hint = "Используйте основные алгебраические операции для изоляции x."
        explanation = f"Чтобы решить {a}*x + {b} = {c}, сначала вычтите {b} из обеих сторон: {a}*x = {c - b}. Затем разделите обе стороны на {a}: x = {(c - b) / a}."
        params = {}

    elif diff == 2:
        a, b, c = [random.randint(1, 5) for _ in range(3)]
        d, e, f = [random.randint(1, 5) for _ in range(3)]

        # Убедимся, что система имеет уникальное решение
        while (a * e - b * d) == 0:
            a, b, c = [random.randint(1, 5) for _ in range(3)]
            d, e, f = [random.randint(1, 5) for _ in range(3)]

        eq1 = sp.Eq(a * x + b * y, c)
        eq2 = sp.Eq(d * x + e * y, f)
        sol = sp.solve((eq1, eq2), (x, y))
        answer = sol

        text = (
            f"Решите систему из двух уравнений:\n"
            f"{a}*x + {b}*y = {c}\n"
            f"{d}*x + {e}*y = {f}")
        hint = "Попробуйте метод подстановки или сложения."
        explanation = (
            "Для решения этой системы можно использовать метод сложения или подстановки. "
            "Например, умножьте первое уравнение на {d} и второе на {a}, затем вычтите одно из другого, чтобы исключить x."
            f"Решение: x={sol[x]}, y={sol[y]}."
        )
        params = {'vars': (x, y)}

    else:
        coeffs = [random.randint(-3, 3) for _ in range(9)]
        rhs1 = random.randint(-5, 5)
        rhs2 = random.randint(-5, 5)
        rhs3 = random.randint(-5, 5)

        eq1 = sp.Eq(coeffs[0] * x + coeffs[1] * y + coeffs[2] * z, rhs1)
        eq2 = sp.Eq(coeffs[3] * x + coeffs[4] * y + coeffs[5] * z, rhs2)
        eq3 = sp.Eq(coeffs[6] * x + coeffs[7] * y + coeffs[8] * z, rhs3)
        sol = sp.solve((eq1, eq2, eq3), (x, y, z))

        # Убедимся, что система имеет решение
        while not sol or not all(isinstance(val, (int, float, sp.Rational)) for val in sol.values()):
            coeffs = [random.randint(-3, 3) for _ in range(9)]
            rhs1 = random.randint(-5, 5)
            rhs2 = random.randint(-5, 5)
            rhs3 = random.randint(-5, 5)
            eq1 = sp.Eq(coeffs[0] * x + coeffs[1] * y + coeffs[2] * z, rhs1)
            eq2 = sp.Eq(coeffs[3] * x + coeffs[4] * y + coeffs[5] * z, rhs2)
            eq3 = sp.Eq(coeffs[6] * x + coeffs[7] * y + coeffs[8] * z, rhs3)
            sol = sp.solve((eq1, eq2, eq3), (x, y, z))
        answer = sol

        text = (
            f"Решите систему из трех уравнений:\n"
            f"{coeffs[0]}*x + {coeffs[1]}*y + {coeffs[2]}*z = {rhs1}\n"
            f"{coeffs[3]}*x + {coeffs[4]}*y + {coeffs[5]}*z = {rhs2}\n"
            f"{coeffs[6]}*x + {coeffs[7]}*y + {coeffs[8]}*z = {rhs3}")
        hint = "Используйте метод Гаусса или Крамера."
        explanation = (
            "Для решения систем трех уравнений можно использовать матричные методы, "
            "такие как метод Гаусса, или метод Крамера, если определитель матрицы не равен нулю. "
            f"Решение: x={sol[x]}, y={sol[y]}, z={sol[z]}.")
        params = {'vars': (x, y, z)}

    return {'text': text, 'answer': answer, 'params': params, 'hint': hint, 'explanation': explanation}
