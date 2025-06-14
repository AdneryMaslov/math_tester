import sys
from procedure_way.utils.generator import generate_question
from procedure_way.utils.checker import check_answer


def main():
    print("Выберите тип задачи:\n"
          "1. Решение уравнений/системы уравнений\n"
          "2. Производная функции\n"
          "3. Вероятность и статистика\n"
          "4. Логические задачи\n"
          "5. Комбинаторика\n"
          "0. Выход")
    while True:
        # Выбор задачи
        choice = input("Введите тип задачи (0-5): ")
        if choice == '0':
            print("Выход.")
            sys.exit()
        if choice not in [str(i) for i in range(1, 6)]:
            print("Такой задачи нет.")
            continue

        # Выбор сложности задачи
        difficulty = input("Уровень сложности (1-3): ")
        if difficulty not in ['1', '2', '3']:
            print("Неверный уровень сложности.")
            continue

        q_type = int(choice)
        diff = int(difficulty)

        # При выборе задачи, получаем текст вопроса, правильный ответ, подсказку, объяснение
        question_data = generate_question(q_type, diff)
        question_text = question_data['text']
        correct_answer = question_data['answer']
        hint = question_data.get('hint', "Подумайте еще раз.")
        explanation = question_data.get('explanation', "К сожалению, объяснения для этой задачи нет.")
        params = question_data.get('params', {})

        print("\n" + "=" * 50)
        print(f"Задача: {question_text}")
        print("=" * 50 + "\n")

        attempts = 3
        for attempt in range(1, attempts + 1):
            user_input = input("Ваш ответ: ")

            # Проверяем ответ
            ok, message = check_answer(user_input, correct_answer, q_type, params)

            if ok:
                print("✅ Правильно!")
                break
            else:
                print(f"❌ Неправильно. {message}")
                if attempt < attempts:
                    print(f"Подсказка: {hint}")
                    print(f"Осталось попыток: {attempts - attempt}")
                else:
                    print(f"Правильный ответ: {correct_answer}")
                    print(f"Объяснение: {explanation}")
        print("-" * 40)


if __name__ == "__main__":
    main()
