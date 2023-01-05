from datetime import datetime

if __name__ == '__main__':
    retry = 0
    while retry < 3:
        day1 = input("input day1:")
        day2 = input("input day2:")
        try:
            x = datetime.strptime(day1, "%d-%m-%Y")
            x1 = datetime.strptime(day2, "%d-%m-%Y")
            delta = x - x1
            days = 0
            if delta.days < 0:
                days = delta.days * -1
            else:
                days = delta.days
            y = days // 365
            y_du = days % 365
            m = y_du // 30
            d = y_du % 30
            print("{} year {} month {} days".format(y, m, d))
            break
        except ValueError:
            print("sai kieu du lieu")
            retry += 1
