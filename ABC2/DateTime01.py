from datetime import datetime

if __name__ == '__main__':
    retry = 0
    while retry < 3:
        d = input("input datetime:")
        try:
            formatted_d = datetime.strptime(d, '%b %d %Y %I:%M%p')
            print(formatted_d)
            break
        except ValueError:
            print("sai kieu du lieu")
            retry += 1
