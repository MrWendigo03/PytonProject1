# Списки
"""list1 = []
list2 = list()
print(list1)
print(list2)"""

# list1 = [1, 1.1, "2", [1, 2, [3, 4]], True]
# print(list1)
# print(list1[3][2][0])
# print(list1[0])
# print(list1[1])
# print(list1[len(list1 - 1)])
# print(list1)
# list1[0] = 21
# print(list1)
# list1[0] = [2, 3, 4]
# print(list1)

# list1.append(11)
# list1.append("99")
# list1.append([11, 22])
# print(list1)
# list1.insert(10, 12)
# print(list1)
# list1.insert(9, 11)
# print(list1)
# del list1[2]
# print(list1)

# newlist = ["Lima", "Washington", "Mexico", "London", "Paris"]
# print(newlist)
# newlist.append("Moscow")
# print(newlist)
# newlist.insert(0, "Rio-De-Jeneiro")
# print(newlist)
# newlist[0] = "Brazilia"
# print(newlist)
# del newlist[2]
# print(newlist)
# newlist.pop(3)
# print(newlist)

# print(sorted(newlist))
# newlist.sort()
# print(newlist)
# print(list(reversed(newlist)))
# newlist.reverse()
# print(newlist)
# print(newlist[::-1])

# if 412 not in newlist:
#     # newlist.remove(412)
#     newlist.append(412)
# print(newlist)

# text1 = "Teacher's name: 404: not: found:"
# print(text1.split(":"))
# text2 = text1.split(":")
# print(":".join(text2))

# print(newlist)
# for i in newlist:
#     print(i + "_2022", end=" ")

# print(list(range(20)))
# print(list(range(1, 20)))
# print(list(range(1, 20, 2)))
# print(list(range(20, 10, -1)))

# print(newlist)
# print(list(enumerate(newlist)))

# for index, value in enumerate(newlist):
#     print(index, value)

# Списки часть 2
# list1 = [1, 2, 3]
# print(list1)
# list1.extend((1, 2, 3))
# print(list1)

# tuple_1 = (1, 2, 3)
# tuple_2 = 1, 2, 3
# tuple_3 = tuple([1, 2, 3])
# print(tuple_1 is tuple_3)
# print(tuple_2)
# print(tuple_3)

# str1 = "abcd"
# str2 = str([1, 2, 3, 4])
# str3 = "abcd"
# print(str1 is str3)

# list2 = [1, 2, 3, 4, 5]
# list1 = [i ** 2 for i in list2 if i > 4] # () - выражение
# print(list1)
# list1 = (i ** 2 for i in list2) # [] - список
# print(list(list1))

# print(10 if 20 < 10 and 10 > 3 else 30)

# print([i for i in range(100) if i % 2 == 0])
# print(list(range(0, 200, 2)))

# list1 = (randint(1, 100) for _ in range(10))
# print(list1)

# list1 = (randint(-100, 100), for _ in range(30))
# minel = list1[0]
# maxel = list1[0]
# for i in range(list1):
#     if minel > list1[i]:
#         minel = list1[i]
#     if maxel < list1[i]:
#         maxel = list1[i]
# print(minel, maxel)

# list1 = [1, 2, 3, 4]
# list2 = list1.copy()
# print(id(list2))
# print(id(list1))

# for i in range(1, 10):
#     if i % 2 == 0:
#         print("Троян")
#         break
# else:
#     print("Чисто")

# urok5

# from random import randint

# list_1 = [randint(1, 9) for _ in range(20)]
# for i in range(list_1):
#     if i % 2 == 0:
#         print(i, end=" ")
#     else:
#         continue

# for i in range(1, 10):
#     for num in range(1, i):
#         print(num, end="")
#     print()

# urok 6:
# vok1 = {"clue": "mean"}
# vok2 = dict()
# print(vok1)
# print(vok2)

# dict1 = {"it_center1": "Tashkent",
#          2: "Andijan",
#          (1, 2): "Jizzakh",
#          frozenset(): "Bukhara",
#          True: False,
#          False: True,
#          1: "Here"}

# print(dict1)
# print(dict1[True])
# print(dict1[1])
# print(dict1.get(100, "22"))
# dict1[1] = "Moron"
# print(dict1)
# dict1[1] = {"new": "value"}
# print(dict1)
# dict1[11] = 23
# print(dict1)

# dict2 = {1: 2}
# dict3 = {3: 4}
# dict3 = dict2 | dict3
# print(dict3)

# dict1 = {
#     "id": 1,
#     "email": "Что-то@.com",
#     "firstname": "Кто-то",
#     "friendname": {
#         {
#             "id": 34,
#             "email": "Что-тоещё@.com",
#             "firtname": "Кто-тоещё"
#         },
#         {
#             "id": 35,
#             "email": "что-то",
#             "firstname": "Кто-то"
#         },
#         {
#             "id": 36,
#             "email": "Что-то",
#             "firstname": "Кто-то"
#         }
#     }
# }
# print(dict1("email"))
# print(dict1("firstname"))
# for friend in dict1["friendname"]:
#     print("email")
#     print("firstname")

# # 5
# goods = {
#     'Lampa': '12345',
#     'Stol': '23456',
#     'Divan': '34567',
#     'Stul': '45678'}
# store = {
#     '12345': [ {
#             'quantity': 27,
#             'price': 42} ],
#     '23456': [ {
#             'quantity': 22,
#             'price': 510},
#         {
#             'quantity': 32,
#             'price': 520 } ],
#     '34567':[ {
#             'quantity': 2,
#             'price': 1200}, {
#             'quantity': 1,
#             'price': 1150} ],
#     '45678': [ {
#             'quantity': 50,
#             'price': 100}, {
#             'quantity': 12,
#             'price': 95}, {
#             'quantity': 43,
#             'price': 97} ] }
# quantity = 0
# print("Наименование товара:", goods)
# for i in store.values():
#     quantity += int(i)
# print("Кол-во:", quantity)
# quantity = 0

# urok 7
# function

# list1 = [22, 45, 267, 77, 23]
# list2 = [10, 11, 13, 15]

# def fciyaodd(new_list):
#     new_list = []
#     for i in list1:
#         if i % 2 == 0:
#             new_list.append(i)
#     print(new_list)

# fciyaodd(list1)
# fciyaodd(list2)

# # urok 8
# def smth():
#     def smth2():
#         return 100
#     return smth2
# print(smth()())
