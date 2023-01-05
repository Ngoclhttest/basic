if __name__ == '__main__':
    # '''calculate the sum of all numbers from 1 to a given number'''
    number = int(input("Number: "))
    Sum = 0
    for i in range(1, number + 1):
        Sum += i
        print(i)
    print("Tong la:", Sum)
