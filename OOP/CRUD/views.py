# # CRUD - C: create, R: read(listing, detail), U: update, D: delete
# import json
# from search import search_object

class CRUD:
    def _get_or_set_objects(self):
        try:
            if self._objects and self._id:
                pass
        except (NameError, AttributeError):
            self._objects = []
            self._id = 0

    def __init__(self) -> None:
        self._get_or_set_objects()

    def create(self, **kwargs):
        self._id += 1
        obj = dict(id = self._id, **kwargs)
        self._objects.append(obj)
        self._save()
        return {'status': '201 Created', 'msg': obj['title']}
    
#     def list(self):
#         res = [{'id': x['id'], 'title': x['title'], 'price': x['price']} 
#                for x in self._objects]
#         return {'status': '200 OK', 'msg': res}
    
#     @search_object
#     def detail(self, id, **kwargs):
#         product = kwargs['object_']
#         return {'status': '200 OK', 'msg': product}
    
#     @search_object
#     def update(self, id, **kwargs):
#         product = kwargs.pop('object_')
#         product.update(**kwargs)
#         self._save()
#         return {'status': '206 Updated'}
    
#     @search_object
#     def delete(self, id, **kwargs):
#         product = kwargs['object_']
#         self._objects.remove(product)
#         self._save()
#         return {'status': '204 No Content'}
    
#     def _save(self):
#         with open('data.json', 'w') as file:
#             json.dump(self._objects, file, indent=4)
#         return 'saved!'



# obj = CRUD()
# obj.create(title='Redmi Note 10',
#            description='The best for own price',
#            qty=10, price=200)

# obj.create(title='Redmi Note 20',
#            description='Flagman of redmi phones, Best!',
#            qty=3, price=500)

# obj.create(title='Iphone 14 Pro Max',
#            description='New phone for ponts!',
#            qty=5, price=1000)

# obj.create(title='Samsung S22 Ultra',
#            description='The best Android Phone!',
#            qty=8, price=900)

# print('------------------------------------list---------------------------------------------')
# print(obj.list())
# print('------------------------------------detail-------------------------------------------')
# print(obj.detail(3))
# print(obj.detail(4))
# print(obj.detail(16))
# print('------------------------------------update-------------------------------------------')
# print(obj.detail(2))
# print(obj.update(2, title='Redmi Note 30 Ultra Max Plus', price = 600))
# print(obj.detail(2))
# print(obj.update(16, title='Redmi', price = 900))
# print('------------------------------------delete-------------------------------------------')
# print(obj.list())
# print(obj.delete(1))
# print(obj.list())
# print(obj.delete(14))
# obj.create(title='Samsung Z Flip 20',
#            description='The best samsung flip flop phone!',
#            qty=3, price=1000)
# print(obj.delete(2))
    
#--------------------------2 наября клавссная работа
# 1
# import json  
# ls = [
#     {"name": "Asan", "raiting": 1},
#     {"name": "Aiperi", "raiting": 5}
# ]  
# with open("data-test.json", "w") as file:
#     json.dump(ls, file, indent=4)
#2
# import json
# with open("data-test.json","r")as f:
#     data = json.load(f)


# print(data) 
# print()
# ls_raiting = [i for i in data if i["raiting"] > 4]
# print(ls_raiting)

# for i in data:
#     if i ["raiting"] > 4:
#         print(i["name"])
#3
# import json

# with open("data-test.json", "r") as file:
#     data = json.load(file)

# for i in data:
#     i["description"] = "..."
# print(data)

# with open("new_db.json", "w")as file:
#     json.dump(data, file, indent=4)
#4
    
# import json

# with open("new_db.json", "r") as file:
#     data = json.load(file)
#     for i in data:
#         if i["id"] == 3:
#             data.remove(i)


# with open("new_db.json", "w") as file:
#     json.dump(data, file, indent=4)
#5
#  Напишите функцию, которая будет запрашивать id, title, description, 
# price, rating и добавлять этот продукт в new_db.json


import json
from bs4 import BeautifulSoup
import requests
url = 'https://auto312.kg/'
def parsing_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_ = 'dj-items-rows')
    cars = container.find_all('div', class_ = 'item_row')
    result = []
    c_id = 0
    for i in cars:
        c_id += 1
        title = i.find('a', class_ = 'title').text
        price = i.find('div', class_ = 'item_price').text
        rating = i.find('div', class_ = 'item_display').text
        desc = i.find('div', class_ = 'item_content_in').text.strip().replace('\n', '')
        data = {'id': int(c_id), 'title': title, 'price': price, 'rating':int(rating), 'desc':(desc)}
        result.append(data)
    return result
with open('car_db.json', 'w') as file:
    json.dump(parsing_data(), file, indent=4)

with open('car_db.json', 'r') as f:
    data = json.load(f)

def add_car(id, title, description, price, rating):
    car = {'id': id, 'title': title, 'description': description, 'price': price, 'rating': rating}
    data.append(car)
    with open('new_car_db.json', 'w') as file:
        json.dump(data, file, indent=4)
    
add_car(21, 'niva', 'temir', '7000', 10)
