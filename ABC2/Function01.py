def sum_list(y):
    t = 0
    for x in y:
        t += x

    return t


if __name__ == '__main__':
    a = [1, 2, 3]
    print(sum_list(a))
    b = [4, 5, 6]
    print(sum_list(b))
