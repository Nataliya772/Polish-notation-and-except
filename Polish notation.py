def polish_notation_one_operand():
    user_input = input('Введите выражение в форме префиксной нотации, используя пробел между операндом и переменными:\n').split()
    assert len(user_input) == 3, 'В вашем выражении чего-то не хватает или есть что-то лишнее'
    operator = user_input[0]
    assert operator in ['+', '-', '*', '/'], 'Вы указали не допустимый операнд (допустимые операнды: +, -, /, *)'
    try:
        operand1 = int(user_input[1])
        operand2 = int(user_input[2])
    except ValueError as e:
        print(f'Введенное выражение содержит букву, текст исключения {e}')
        return None
    if operator == '+':
        print(f'Результат вычисления {operand1 + operand2}')
    elif operator == '-':
        print(f'Результат вычисления {operand1 - operand2}')
    elif operator == '*':
        print(f'Результат вычисления {operand1 * operand2}')

    try:
        if operator == '/':
            print(f'Результат вычисления {operand1 / operand2}')
    except ZeroDivisionError as e:
        print(f'Нельзя делить на 0, текст исключения {e}')

    finally:
        print('Начните заново')
    return None

polish_notation_one_operand()
