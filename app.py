def calculator_app (a: str, b: str) -> None:
    """Функция вычисления результата между двумя числами

    :param a: "Введите число №1: ".
    :param b: "Введите число №2: ".
    :return: None
    """

    print("Добро пожаловать в приложение 'Калькулятор'!")
    while True:
        while True: # проверка числа №1
            try:
                number_1_ch = input(a)
                number_1 = float(number_1_ch)
                if number_1.is_integer():
                    number_1 = int(number_1_ch)
                break
            except ValueError:
                print("Ошибка! Введите число.")
                continue

        while True: # проверка числа №2
            try:
                number_2_ch = input(b)
                number_2 = float(number_2_ch)
                if number_2.is_integer():
                    number_2 = int(number_2_ch)
                break
            except ValueError:
                print("Ошибка! Введите число.")
                continue

        while True: # выбор операции
            operation = input("Введите операцию из списка (+, -, *, /): ")
            if operation == '+':
                result = number_1 + number_2
                print("Результат:", result)
                break
            elif operation == '-':
                result = number_1 - number_2
                print("Результат:", result)
                break
            elif operation == '*':
                result = number_1 * number_2
                print("Результат:", result)
                break
            elif operation == '/':
                try:
                    result = number_1 / number_2
                    print("Результат:", result)
                    break
                except ZeroDivisionError:
                    print("Деление на ноль запрещено!")
                    continue
            else:
                print("В списке такой операции нет.")
                continue
        break

calculator_app("Введите число №1: ", "Введите число №2: ")
