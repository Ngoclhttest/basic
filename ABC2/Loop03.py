
if __name__ == '__main__':
    retry = 0
    while retry < 5:
        a = input("nhap vao a:")
        # neu la numeric thi cast ve float va check integer
        # if a.isnumeric() and float(a).is_integer() and int(a) < 200:
        #     print("hello world")
        #     break
        # elif a.isnumeric() and float(a).is_integer() and int(a) >= 200:
        #     print("wrong value, int must < 200!")
        #     retry += 1
        # else:
        #     print("wrong value, only accept int!")
        #     retry += 1
        try:
            a = float(a)
            if a < 200:
                print("hello world")
                break
            else:
                print("wrong value, int must < 200!")
                retry += 1
        except ValueError:
            print("wrong value, only accept number!")
            retry += 1
