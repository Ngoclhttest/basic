from string import ascii_lowercase as alc


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 1. input a string of number and print out largest number from the input
    a = input("Nhap vao so can tinh:")
    if a.isnumeric() is False:
        print("ban nhap khong phai la so")
    else:
        chars = list(a)
        print(chars)
        chars.sort(reverse=True)
        print(chars)
        print("".join(chars))
    # 2. Input 1 number and print out the longest "0" string of the binary of this number
    # a = input("Nhap vao so thap phan:")
    # if a.isnumeric() is False:
    #     print("ban nhap khong phai la so, vui long nhap lai")
    # else:
    #     b = bin(int(a)).replace("0b", "") # đổi qua nhị phân
    #     b = str(b) # đổi từ nhị phân thành chuỗi
    #     zero = b.split("1") # cắt 1
    #     print(zero)
    #     m = 0
    #     for element in zero:
    #         if len(element) >= m:
    #             m = len(element)
    #             print(m)
    #
    #     print("".join(["0"*m]))
    # 3.''' input a string and print out new string which remove all duplicated chars (not include space) in string’’’
    # a = input("nhập chuỗi ký tự :")
    # if a.isnumeric() is True:
    #     print("bạn nhập không phải kiểu str ")
    # else:
    #     danh_sach_ky_tu = list(a)
    #     luu_tam = {}
    #     ket_qua = []
    #     for ky_tu in danh_sach_ky_tu:
    #         if ky_tu in luu_tam and ky_tu != " ":
    #             continue
    #         else:
    #             luu_tam[ky_tu] = True
    #             ket_qua.append(ky_tu)
    #
    #         print(luu_tam)
    #
    #     print("".join(ket_qua))
    #     print(''.join(sorted(set(a), key=a.index)))
    # ''' Same requirement with exercise #3, but you need to read the string inputted from the
    # console and have to validate if the user enters nothing. Program should retry/prompt user
    # for 3 times to enter correct string otherwise close the program’’’
    # n = 0  # so lan thu
    # a = ""
    # while n < 3:
    #     a = input("nhập tên vào:")
    #     if a is None or a == "":
    #         print("giá trị không được để trống!")
    #         n += 1
    #     elif a.isnumeric() is True:
    #         print("nhập giá trị là kiểu string ")
    #         n += 1
    #     else:
    #         break
    # danh_sach_ky_tu = list(a)
    # luu_tam = {}
    # ket_qua = []
    # for ky_tu in danh_sach_ky_tu:
    #     if ky_tu in luu_tam and ky_tu != " ":
    #         continue
    #     else:
    #         luu_tam[ky_tu] = True
    #         ket_qua.append(ky_tu)
    #
    # print("".join(ket_qua))
    # ''' Concatenate two lists, print out a complete string which is the combination of index value of each list.'''

    # list_1 = ["i", "not", "someone"]
    # list_2 = ["'m", "love"]
    # # print(len(list_2))
    # a = ""
    # for index, element in enumerate(list_1):
    #     a += element + " "
    #     # print("Day la element", element)
    #     # print("day la index", index)
    #     if index < len(list_2):
    #         a += list_2[index] + " "
    #     else:
    #         a += "yet"
    # print(a)
    # '''Detect the input array/tuples/dict and return correct type and count total elements in it.'''
    # a = input("nhap vao a:")
    # b = eval(a)
    # if isinstance(b, dict):
    #     print("\"dict\" with length:" + str(len(b)))
    # elif isinstance(b, list):
    #     print("\"list\" with length:" + str(len(b)))
    # elif isinstance(b, tuple) :
    #     print("\"tuple\" with length:" + str(len(b)))
    # else:
    #     print("k xac dinh duoc type")

    # '''Enter a number and will create a dictionary which has a total pair of key,value equal to the inputted number.
    # Format of key will be alphabet and value will be numeric'''
    # a = input("nhap vao so:")
    # b = eval(a)
    # c = {}
    # for index, element in enumerate(alc):
    #     if index < int(a):
    #         c[element] = str(index + 1)
    #
    # print(c)

    # '''Create a dict function that the key’s value will be auto converted to UPPERCASE'''.
    # d = {'hello': "1", "world": "2"}
    # e = {}
    # for k, v in d.items():
    #     print("key la:" + k.upper())
    #     print("value la:" + v.upper())
    #     e[k.upper()] = v
    # print(e)

    # Loop Function
    # '''calculate the sum of all numbers from 1 to a given number'''
    # number = int(input("Number: "))
    # Sum = 0
    # for i in range(1, number + 1):
    #     Sum += i
    #     print(i)
    # print("Tong la:", Sum)

    #     '''Display only those numbers from a list,tuple that satisfy the following conditions
    # The number must be divisible by 3
    # and the number is greater than 119
    # And the number is not greater than 500''' .e.g
    # a = input("nhập vào list: ")
    # a = eval(a)
    # b = []
    # if isinstance(a, list) or isinstance(a, tuple):
    #     for i in a:
    #         if i % 3 == 0 and 119 < int(i) < 500:
    #             b.append(i)
    #     print(b)
    # else:
    #     print("bạn phải nhập vào list hoặc tuple")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
