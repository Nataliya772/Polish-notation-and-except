def polish_notation_one_operand():
    user_input = input('Введите выражение в форме префиксной нотации, используя пробел между операндом и переменными:\n').split()
    try:
        if user_input[0] == '+':
            print(f'Результат вычисления {int(user_input[1]) + int(user_input[2])}')
        elif user_input[0] == '-':
            print(f'Результат вычисления {int(user_input[1]) - int(user_input[2])}')
        elif user_input[0] == '/':
            print(f'Результат вычисления {int(user_input[1]) / int(user_input[2])}')
        elif user_input[0] == '*':
            print(f'Результат вычисления {int(user_input[1]) * int(user_input[2])}')
        else:
            assert False, 'AssertionError - Вы не указали допустимый операнд (+, -, /, *)'

    except AssertionError as e:
        print(f'Введенное выражение не содержит операнд, текст исключения {e}')

    except ValueError as e:
        print(f'Введенное выражение содержит более 2 аргументов и 1 опранда или букву, текст исключения {e}')

    except ZeroDivisionError as e:
        print(f'Нельзя делить на 0, текст исключения {e}')

    except TypeError as e:
        print(f'Переменная не может быть не числом, текст исключения {e}')

    except IndexError as e:
        print(f'Вы не задали арифметическое выражение, текст исключения {e}')

    finally:
        print('Начните заново')
    return None

polish_notation_one_operand()
