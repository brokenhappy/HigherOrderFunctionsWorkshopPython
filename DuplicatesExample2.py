nums_1 = [1, 2, 3]
nums_2 = [4, 5, 6]


def sum_of_nums_1():
    total = 0
    for num in nums_1:
        total += num
    return total


def sum_of_nums_2():
    total = 0
    for num in nums_2:
        total += num
    return total


if __name__ == '__main__':
    print(sum_of_nums_1())
    print(sum_of_nums_2())
