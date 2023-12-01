strings_1 = ['1', '2', '3']
strings_2 = ['0.4', '0.5', '0.6']


def map_to_int(strings):
    total = []
    for string in strings:
        total.append(int(string))
    return total


def map_to_float(strings):
    floats = []
    for string in strings:
        floats.append(float(string))
    return floats


if __name__ == '__main__':
    print(map_to_int(strings_1))
    print(map_to_float(strings_2))
