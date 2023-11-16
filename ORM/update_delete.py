# from models import Product, Category


# обновления данных
# query = Product.update(price=500).where(Product.title == 'Zara t-shirt')
# print(query)
# query.execute()

# чтобы увеличить цену на всех товаров на 0.5 %
# query = Product.update(price=(Product.price + Product.price * 0.5))
# print(query)
# query.execute()

# чтобы удалить определенный товар 
# query = Product.delete().where(Product.id == 17 and Product.id == 19)
# query.execute()
# # удаления через обьект
# product = Product.get(id=18) 
# print(product, product.title)
# product.delete_instance()

# query = Product.delete().where(Product.id >= 20)
# print(query)
# query.excute()



