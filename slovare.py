# dict()-slovar->   упорядочная коллекция элементов
# pyhton 3.7 -> каждый элемент внутри словаря хранится в виде пары -->{ключ значения}

# ассоциативный массив,hash table,object(js) ==dictionari(pyhton)

# thisdict ={
#     "brant":"Ford",
#     "model": "Mystang",
#     "year": 1967,}


# print(thisdict, type(thisdict))
# print(thisdict, ["brant"],(thisdict["model"])
# print(thisdict["year"] )  
      
# thisdict[motor] = "B12"  
# print(thisdict[motor])
# thisdict[color]= "yellow"
# print[thisdict]



# print(dir(dict))
# items, keys, values

# user_info = {
#     "first_name":"John"
#     "las_name" : "Snow",
#     "age":24,
#     "email":"john@jug.com"
#     "role": "admin"}
#     "age":35

# kluchi = user_info.keys
# print(kluchi, type(kluchi))
# ls = list(kluchi)
# print(ls, ls[0], ls[3:])



# ls = user_info.values
# print(ls, type(ls))
# print(ls, ls[0], ls[3:])


# elementy = user_info.items()
# print(user_info)
# print(elementy)




# изменения переменной 

# dict_ = {"name": "Jack", "age": 17}
# print(dict_)#{"name", : "Jack", "age": 17"}
# dict_["name"] = John
# dict_["age"] = 24
# print(dict_)#{"name": "Jack", "age": 24}
# dict_.update({"name": "Tirion", "addres":"Wesnoros"})
# print(dict_)# {"name":"Tirion", "age": 24<,"address": 'Westorons"}   


# получения данных со словаря:
# # get
# dict_ = {1: "pizza", "2: "burger"3:"steak",}
# print(dict_[3,]"!!!")
# print(dict__get(5))#None



# setdefauld - работает так же как и get,  но если нет такого ключа то создает новую пару из этого 
# dict_={1: "pizza", 2: "burger", 3: "steak",}
# print(dict_.setdefault(5, "manty"))
# print(dict__)


#fromkeys
# ls = list (range(1, 100))
# print(ls)

# nwe_dict = dict.fromkeys(ls)
# print(new_dict)


#удаления элементо
#pop, popitem

#pop(<key>)-удаляет пру по ключу


# dict_= {"name":"Johh", "last_name": "Snow"}
# print(dict_)
# remover = dict_.pop("name")
# print(removed)
# print(dict_)


#popitem - удаляет и возврашает последнюю пару
# print("\n\n")
# dict_= {"name":"Johh", "last_name": "Snow"}
# print(dict_)
# remover = dict_.popitem()
# print(removed)
# print(dict_)



# roles = {
#     1: "admin",
#     2:"customer",
#     3:"vendor",
# }   
# product = {
#     "id": 31,
#     "title":"Macbook Air M1",
#     "description":"Lorem  Ipsum",
#     "prise": 900
# }   

# users = {
#     16:{'username':'johnsnow_12', 'password':
#         'bastard123', 'role':roles[1]},
#     34:{'username':'tirion_small',
#         'password': 'short123', 'role':roles[3]},
#     54:{'username':'serseya_terminator',
#         'password': 'terminator123', 'role':roles[2]}
# }
# print(users)
# print(product)

# username = input("Vvedite svoi username:").lower()
# user_exists = False
# for key, dict_ in users.items():
#     if username ==  dict_["username"]:
#         id = key
#         user_exists = True


# if not user_exists:
#     raise ValueError("username not foynd!")    

# password = input("Vveditesvoi password:").lower()

# if users[id]["password"] != password:
#     raise ValueError("Passwords did not match!")

# if users[id] ["role"] == roles[1]:
#     product["description"] = input("Vvedite novoe opisanie")
# else:
#     raise Exception("you do not have permissions!")
# print(product)   





#hw1
# a =[["Bishkek", "CholponAta", "Tokmok"]]
# d = {
# "Bishek": 312,
# "CholponAta" : 453,
# "Tokmok" : 543
# }
# print(d)

# r = dict(Bishek = 312,CholponAta = 453, Tokmok = 543)
# print(r)


# r = dict(Bishek = 312,CholponAta = 453, Tokmok = 543)
# t= dict()                  
# print(r)
  

#2
# d= {
#     1: "one",
#     2: "two",
#     3: "three"
# }
# print(d)
# del d[1]
# print(d)

#3
# d = {
#     1: 23,
#     2: 786,
#     3: 789
# }

# del d[1] 

# print(d)   

#4

# d = {
#     1: 23,
#     2: 786,
#     3: 789
#  }

# d.clear()

# print(d)

#5
# d = {
#     1: 23,
#     2: 786,
#     3: 789
# }
# print(d.keys())
# print(d.pop (2,))   
# print(d.pop (3,))
#6

# d = {"key1": "value1", "key2": "value2"}  
# print(d, '--- eto slovar "d"')
# copy = d.copy() # == {"key1": "value1", "key2": "value2"}
# print(copy, '--- eto copiya slovarya "d"') 

#7
# menu = {'Pad Thai': 200, 'Tom Yam': 170, 'Chicken Teriyaki': 250}
# print(menu.setdefault("friedRice", 250))
# print(menu)

# menu["Tom Yam"] = 250
# removed = menu.pop("PadThai")
# print(removed)
# print(menu)

#8

# dict = {"кружка" :"стакан","вода": "жидкость"}
# print(dict["вода"])

#9

# dict_= {"name": "Lucky", "age": 5, 'eyes': 'blue' }
# name = dict_["name"]
# age = dict_["age"]
# eyes = dict_["eyes"]
# print(dict_)
# print(f"This is a dog. His name is {name}.It has  {eyes} eyes.Lucky is {age} years old. ")

#10
# students_dict= {
#     "менеджмент": ["Махабат", "Аида", "Нуржахан"] , "Юрuдический":["Азат", "Марат", "Самат"]
# }
# group_student = students_dict["менеджмент"][2]
# for a, b in students_dict.items():
#     if group_student in b:
#         print(f"This is {group_student}. He stadies {a} ")

