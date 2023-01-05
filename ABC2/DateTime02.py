from datetime import datetime

if __name__ == '__main__':
    retry = 0
    while retry < 3:
        d = input("input datetime:")
        try:
            x = datetime.strptime(d, "%d-%m-%Y")
            print(x.strftime("%A %d %B %Y"))
            break
        except ValueError:
            print("sai kieu du lieu")
            retry += 1

