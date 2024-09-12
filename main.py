''' 
:( :( :(

Сильно сократить код и оптимизировать его можно, если ввести функции, 
которые будут определять числа и уменьшать количество одинакого кода.
Но в звдвнии написано написать функцию, поэтому, я полагаю, что это все придется делать так:
'''

def calc(string):
    operations = ['плюс', 'минус', 'умножить']
    string = string.lower()
    data = string.split()

    # определяем первое число
    if data[1] in operations:
        if data[0] == 'один':
            number1 = 1
        elif data[0] == 'два':
            number1 = 2
        # продолжить до 20 и не забыть про 0
    elif data[2] in operations:
        if data[0] == 'двадцать':
            if data[1] == 'один':
                number1 = 21
            elif data[0] == 'два':
                number1 = 22
            #  продолжить до 9
        elif data[0] == 'тридцать':
            if data[1] == 'один':
                number1 = 31
            elif data[0] == 'два':
                number1 = 32
        # продолжить до 90
    
    # определяем второе число
    if data[1] in operations and len(data) == 3:
        if data[-1] == 'один':
            number2 = 1
        elif data[-1] == 'два':
            number2 = 2
        # продолжить до 20 и не забыть про 0
    elif (data[1] in operations and len(data) == 4) or (data[2] in operations and len(data) == 5):
        if data[-2] == 'двадцать':
            if data[-1] == 'один':
                number2 = 21
            elif data[-1] == 'два':
                number2 = 22
            #  продолжить до 9
        elif data[-2] == 'тридцать':
            if data[-1] == 'один':
                number2 = 31
            elif data[-1] == 'два':
                number2 = 32
            # продолжить до 9
        # продолжить до 90
    
    # определяем операцию
    if data[1] in operations:
        operation = data[1]
    elif data[2] in operations:
        operation = data[2]

    # подсчитываем результат в числовой форме
    if operation == 'плюс':
        result = number1 + number2
    elif operation == 'минус':
        result = number1 - number2
    elif operation == 'умножить':
        result = number1 * number2
    
    # переводим результат в словесную форму
    if len(str(result)) == 1:
        if result == 1:
            word_result = 'один'
        elif result == 2:
            word_result = 'два'
        # продолжить до 20 и не забыть 0
    elif len(str(result)) == 2:
        if str(result)[0] == '2':
            word_result = 'двадцать '
            if str(result)[1] == '1':
                word_result += 'один'
            elif str(result)[1] == '2':
                word_result += 'два'
            # продолжить до 9
        elif str(result)[0] == '3':
            word_result = 'тридцать '
            if str(result)[1] == '1':
                word_result += 'один'
            elif str(result)[1] == '2':
                word_result += 'два'
            # продолжить до 9
        # продолжить до 90
    
    print(word_result)


calc(input())