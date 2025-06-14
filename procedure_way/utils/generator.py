"""
Диспетчер, перенаправляющий на модуль нужной темы задач
"""
from procedure_way.tasks.derivative import generate_derivative
from procedure_way.tasks.system import generate_system
from procedure_way.tasks.probability import generate_probability
from procedure_way.tasks.logic import generate_logic
from procedure_way.tasks.combinatorics import generate_combinatorics


def generate_question(q_type, diff):
    """Взависимости от типа вопроса, функция возвращает {'text', 'answer', 'hint', 'explanation', 'params'}"""

    if q_type == 1:
        return generate_system(diff)
    elif q_type == 2:
        return generate_derivative(diff)
    elif q_type == 3:
        return generate_probability(diff)
    elif q_type == 4:
        return generate_logic(diff)
    elif q_type == 5:
        return generate_combinatorics(diff)
    else:
        raise ValueError("Неверный тип задачи")
