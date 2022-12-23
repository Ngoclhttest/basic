# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # a = 1
    # print(a)
    # a = "abc"
    # print(a)
    # a = [1,2,3,"abc"]
    # print(a)
    # print(len(a))
    # for elem in a:
    #     print(elem)
    # a[0] = 5
    # print(a)
    # a.append(6) # them vao cuoi
    # print(a)
    # a.insert(1, 7)
    # print(a)
    # del a[-2]
    # print(a)

    # map, dictionary / dict
    # key la duy nhat, khong duoc trung
    # a = {
    #     "key2": "value2",
    #     "key1": "value1",
    #     "value1": "value11",
    # }
    # print(a["key1"])
    # print(a["value1"])
    # a["key1"] = "value3"
    # print(a["key1"])
    # del a["key2"]
    # print(a)
    # print(len(a))
    # # print(a["key2"])
    # print(a.get("key2") is None)
    #
    # print()

    # a = 2
    # if a == 1:
    #     print("ok")
    # else:
    #     print("not ok")

    # a = [1,2,3,"abc"]
    # b = input()
    # print(b)
    # if b in a:
    #     print("Ok")
    # else:
    #     print("not ok5")
    # a.append(b)
    # # print(a)
    # print(len(a))
    # for elem in a:
    #     print(elem)

    # a = {
    #     "key1": "value1",
    #     "key2": "value2",
    # }
    # b = input()
    # c = input()
    # if b in a:
    #     a[b] = c
    #     print(a)
    # else:
    #     print("a khong chua b")
    # a = {
    #     "key1": "valueA",
    #     "key2": "valueB",
    #     "key3": [1,3,5,"nnnn"],
    #     "key4": [1],
    #     10: {
    #         "key11": "valueA",
    #         "key22": "valueB",
    #         "key33": [1,3,5,"nnnn"],
    #         "key44": [1],
    #     },
    #     "abc": {
    #         "key11": "valueA",
    #         "key22": "valueB",
    #         "key33": [1,3,5,"nnnn"],
    #         "key44": [1],
    #     },
    # }
    # b = input()
    # c = input()
    # if b in a[10]:
    #     print (a[10][b])
    #     if isinstance(a[10][b], list) :
    #         a[10][b].append(c)
    #         print(a)
    #
    # else:
    #     print("khong ok")
    # for elem in a:
    #     if isinstance(a[elem], dict):
    #         for elem2 in a[elem]:
    #             print(elem2,a[elem][elem2])
    #     else:
    #         print(elem,a[elem])
    # bizops={"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5nb2MubGVAYmUuY29tLnZuIiwicGhvbmUiOiIiLCJuYW1lIjoiXCJOZ1xcdTFlY2RjIExcXHUwMGVhIChTci4gUUEgTWFudWFsKVwiIiwic3ViIjoibmdvYy5sZUBiZS5jb20udm4iLCJjbGllbnRfaWQiOiJzdGdfYmUtZm9vZCIsImlzcyI6InN0YWZmLmJlLWF1dG9zIiwiZXhwIjoxNjY1MDYzMzA0LCJncm91cHMiOm51bGx9.-x3MCe5kD_sFt8D-Lcntrx6sL8hJPxJW2bF1TIzQr8o","clientId":"stg_be-autos"}
    # for key in bizops:
    #     print(bizops[key])
    #     print(len(bizops[key]))
    queue_option={"queue":[{"id":"-1","clientId":"stg_be-autos","name":"All Staff"},{"id":"11","clientId":"stg_be-autos","name":"Fraud Team"},{"id":"15","clientId":"stg_be-autos","name":"ob"},{"id":"16","clientId":"stg_be-autos","name":"SI"},{"id":"17","clientId":"stg_be-autos","name":"long test"},{"id":"18","clientId":"stg_be-autos","name":"All"},{"id":"20","clientId":"stg_be-autos","name":"abc"},{"id":"22","clientId":"stg_be-autos","name":"new food"},{"id":"24","clientId":"stg_be-autos","name":"Toannguyen"}]}
    for key in queue_option["queue"]:
        print(key)
        if key["name"]!= "Toannguyen":
            print("error")

        # print(queue_option["queue"][key])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
