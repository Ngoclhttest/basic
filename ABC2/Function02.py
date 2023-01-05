def subtract_list(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] - sum(a[1:])


if __name__ == '__main__':
    a = input("nhap list so:")
    a = eval(a)
    if isinstance(a, list):
        total = subtract_list(a)
        if total < 0:
            print("Error")
        else:
            print(total)
    else:
        print("day k phai la list number")
