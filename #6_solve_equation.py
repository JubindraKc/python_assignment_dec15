def equ(m, x, c):
    return m * x + c


def solve_for_y():

    value_x = [1, 2.3, 5.6, 7, 78]
    m = 45
    c = 0.5

    for x in value_x:
        y = equ(m, x, c)
        print("solved value of y is {0.2f}" .format(y))


solve_for_y()
