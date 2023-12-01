def add_digit_5(number):
    str_number = str(number)
    number_with_5 = str_number + '5'
    return int(number_with_5)


def add_digit_1(number):
    str_number = str(number)
    number_with_1 = str_number + '1'
    return int(number_with_1)


if __name__ == '__main__':
    print(add_digit_5(3))
    print(add_digit_1(3))
