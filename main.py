def calc(string):
    operations = ['плюс', 'минус', 'умножить']
    tens = [20, 30, 40, 50, 60, 70, 80, 90]
    string = string.lower()
    data = string.split()

    # определяем первое число
    if data[1] in operations:
        number1 = determine_digit(data[0])
    elif data[2] in operations:
        number_sym1 = determine_tens(data[0])
        number_sym2 = determine_digit(data[1])
        number1 = int(str(number_sym1) + str(number_sym2))
    
    print(number1)
    
    # определяем второе число
    if data[1] in operations and len(data) == 3 or data[2] in operations and len(data) == 4:
        number2 = determine_digit(data[-1])
    elif (data[1] in operations and len(data) == 4) or (data[2] in operations and len(data) == 5):
        number_sym1 = determine_tens(data[-2])
        number_sym2 = determine_digit(data[-1])
        number2 = int(str(number_sym1) + str(number_sym2))

    
    print(number2)

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
    
    print(result)
    
    # переводим результат в словесную форму
    if result in range(0,20) or result in tens:
        word_result = digits_to_strings(result)
    elif len(str(result)) == 2:
        word_result1 = tens_to_string(int(str(result)[0]))
        word_result2 = digits_to_strings(int(str(result)[1]))
        word_result = word_result1 + ' ' + word_result2
    
    print(word_result)

def determine_digit(str_number):
    match str_number:
        case 'ноль':
            number = 0
        case 'один':
            number = 1
        case 'два':
            number = 2
        case 'три':
            number = 3
        case 'четыре':
            number = 4
        case 'пять':
            number = 5
        case 'шесть':
            number = 6
        case 'семь':
            number = 7
        case 'восемь':
            number = 8
        case 'девять':
            number = 9
        case 'десять':
            number = 10
        case 'одиннадцать':
            number = 11
        case 'двенадцать':
            number = 12
        case 'тринадцать':
            number = 13
        case 'четырнадцать':
            number = 14
        case 'пятнадцать':
            number = 15
        case 'шестнадцать':
            number = 16
        case 'семнадцать':
            number = 17
        case 'восемнадцать':
            number = 18
        case 'девятнадцать':
            number = 19
        case 'двадцать':
            number = 20
        case 'тридцать':
            number = 30
        case 'сорок':
            number = 40
        case 'пятьдесят':
            number = 50
        case 'шестьдесят':
            number = 60
        case 'семдесят':
            number = 70
        case 'восемдесят':
            number = 80
        case 'девяносто':
            number = 90
    return number

def determine_tens(str_number):
    match str_number:
        case 'двадцать':
            number = 2
        case 'тридцать':
            number = 3
        case 'сорок':
            number = 4
        case 'пятьдесят':
            number = 5
        case 'шестьдесят':
            number = 6
        case 'семдесят':
            number = 7
        case 'восемдесят':
            number = 8
        case 'девяносто':
            number = 9
    return number

def digits_to_strings(number):
    match number:
        case 0:
            string = 'ноль'
        case 1:
            string = 'один'
        case 2:
            string = 'два'
        case 3:
            string = 'три'
        case 4:
            string = 'четыре'
        case 5:
            string = 'пять'
        case 6:
            string = 'шесть'
        case 7:
            string = 'семь'
        case 8:
            string = 'восемь'
        case 9:
            string = 'девять'
        case 10:
            string = 'десять'
        case 11:
            string = 'одиннадцать'
        case 12:
            string = 'двенадцать'
        case 13:
            string = 'тринадцать'
        case 14:
            string = 'четырнадцать'
        case 15:
            string = 'пятнадцать'
        case 16:
            string = 'шестнадцать'
        case 17:
            string = 'семнадцать'
        case 18:
            string = 'восемнадцать'
        case 19:
            string = 'девятнадцать'
        case 20:
            string = 'двадцать'
        case 30:
            string = 'тридцать'
        case 40:
            string = 'сорок'
        case 50:
            string = 'пятьдесят'
        case 60:
            string = 'шестьдесят'
        case 70:
            string = 'семдесят'
        case 80:
            string = 'восемдесят'
        case 90:
            string = 'девяносто'
    return string

def tens_to_string(number):
    match number:
        case 2:
            string = 'двадцать'
        case 3:
            string = 'тридцать'
        case 4:
            string = 'сорок'
        case 5:
            string = 'пятьдесят'
        case 6:
            string = 'шестьдесят'
        case 7:
            string = 'семдесят'
        case 8:
            string = 'восемдесят'
        case 9:
            string = 'девяносто'
    return string

calc(input())