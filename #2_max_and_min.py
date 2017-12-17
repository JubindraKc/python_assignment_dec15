my_list = [4, 2, 4, 0, 2, 4, 5, 7, 8, 9, 23, 8, 5, 4, 2, 2, 34, 4, 45]


def max_min():
    my_list.sort()
    print(my_list)
    print("min: {} \t max: {}" .format(my_list[0], my_list[-1]))


max_min()

