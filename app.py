def check_number (a: str) -> None:
    """Функция проверки числа, вводимого пользователем

    :param a: "Введите число №: ".
    :return: None
    """

    while True:
        try:
            number_1_ch = input(a)
            number_1 = float(number_1_ch)
            if number_1.is_integer():
                number_1 = int(number_1_ch)
            return number_1
            break
        except ValueError:
            print("Ошибка! Введите число.")
            continue

def check_operation(number_1: int|float, number_2: int|float) -> int|float:
    """Функция проверки операции, выбранной пользователем

    :param a: Число №1.
    :param b: Число №2.
    :return: Результат вычисления
    """

    while True:
        operation = input("Введите операцию из списка (+, -, *, /): ")
        if operation == '+':
            result = number_1 + number_2
            break
        elif operation == '-':
            result = number_1 - number_2
            break
        elif operation == '*':
            result = number_1 * number_2
            break
        elif operation == '/':
            try:
                result = number_1 / number_2
                break
            except ZeroDivisionError:
                print("Деление на ноль запрещено!")
                continue
        else:
            print("В списке такой операции нет.")
            continue
    return result

def calculator_app () -> None:
    print("Добро пожаловать в приложение 'Калькулятор'!")
    val1 = check_number('Введите число №1: ')
    val2 = check_number('Введите число №2: ')
    result = check_operation(val1, val2)
    print("Результат:", result)

calculator_app ()