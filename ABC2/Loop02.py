if __name__ == '__main__':
    # '''Display only those numbers from a list,tuple that satisfy the following conditions
    # The number must be divisible by 3
    # and the number is greater than 119
    # And the number is not greater than 500''' .e.g
    a = input("nhập vào list: ")
    a = eval(a)
    b = []
    if isinstance(a, list) or isinstance(a, tuple):
        for i in a:
            if i % 3 == 0 and 119 < int(i) < 500:
                b.append(i)
        print(b)
    else:
        print("bạn phải nhập vào list hoặc tuple")