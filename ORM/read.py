import peewee
from models import Product, Category

def get_all_categories():
    return Category.select()

def get_all_products():
    return Product.select()

categories = get_all_categories()
# print(dir(categories))
print(categories.objects())
print('Категории в бд:')
# for x in categories:
    # print(x)
    # print(x.title)
    # print(x.created_at.strftime('%Y-%m-%d -->> %H:%M:%S'))
    # print()
# products = get_all_products()
# print('все товары в бд:')  
# sum_price = 0
# for x in products:
#     print(f'{x.title} --> {x.price}--> {x.category_id.title}') 
#     print()  
#     sum_price += x.price


# print(f'AVG price: {sum_price / len(products)}')     

# products = get_all_products()
# category = int(input('введите сатегории(6-платья, 7-джинсы, 8-футболки, 9-свитера, 10-обувь):'))
# for x in products:
#     # if x.category_id.category_id == category:
#         print(f'{x.title} --> {x.price}--> {x.category_id.title}')

# category_name = input('Vedite title category: ').lower().strip()
# try:
#     category = Category.get(title=category_name)
#     print(category, category.title)
# except peewee.DoesNotExist:
#     print('Такой категории нет!')
# else:
#     for product in category.products:
#         print(f'Title: { product.title}, price: {product.price}, category:{product.category_id.title}')

