def day1(input_str):
    input_without_letters = remove_letters_from(input_str)
    digit_lines = input_without_letters.split('\n')
    numbers = first_and_last_digit_to_int_of_each_line(digit_lines)
    return sum_of(numbers)


def remove_letters_from(item):
    without_letters = ""
    for char in item:
        if not char.isalpha():
            without_letters += char
    return without_letters


def first_and_last_digit_to_int_of_each_line(digit_lines):
    numbers = []
    for digit_line in digit_lines:
        number_of_this_line = int(f'{digit_line[0]}{digit_line[-1]}')
        numbers.append(number_of_this_line)
    return numbers


def sum_of(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum


if __name__ == '__main__':
    print(day1('1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet'))
