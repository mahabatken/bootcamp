# print(x for x in range(1, 10))


# x, a, b, = (x for x in range(1,4))
# print(x, a, b)


# list comprehensions- генераторы списков 
# list comprehensions-oпределения тогоб что в итоге sions - генератор списков 
# упрошенный подход к созданию списков б который задействует в себе цикл  а также конструкцию   для


# list -> 0 - 200 -> chetnye

# ls = []
# for x in range(0, 200):
#     if x % 2 == 0:
#         ls.append(x)
# print(ls)

# ls = [x for x in range(0, 200) if x % 2 == 0]
# print(ls)

#list -> 0, 300 -> num % 2, 5
# ls = [x for x in range(0, 301)if x % 2 == 0 and x % 5 == 0]
# print(ls)
  


# set_={x for x in range(0, 301)if x % 2 == 0 and x % 5 == 0}
# print(set_)  (mnogestva)


# list - 0, 100 -> x 2 -> x ** 2, x 3 -> x **3
# ls = [x ** 2 ifx % 2 == 0 else x ** 3
#        for x in range(0, 100)
#        if x % 2 == 0 or x % 3 == 0]


# print(ls)

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# #[1, 2, 3, 4, 5, 6, 7, 8, 9 ]

# res =[item for x in ls for item in x]
# for x in ls:
#     for item in x:
#         res.append(item)

# print(res)        


# from datetime import datetime

# start = datetime.now() # 12:22:24
# ls = []
# for x in range(0, 100_000_0000):
#     ls.append(x)
# finish = datetime.now()
# print(start - flush)    




# ls = []
# ---------------------
# dict_ = {x: x**2 for x in range(1,11)}
# print(dict_)

 