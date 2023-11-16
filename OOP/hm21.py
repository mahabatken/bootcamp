

    # 1 Напишите класс Subscriber, у которого есть переменные экземпляра:
    #     firstname
    #     lastname
    #     Сделайте так, чтобы метод __repr__ возвращал firstname + lastname

# class Subscriber:
#     def __init__(self ,firsname, lastname) :
#         self.firsname = firsname
#         self.name = lastname
#         print (f"{self.firsname}{self.name}")
# obj = Subscriber("Maha ", "Aitkylova")

#-----------


# class Terminal:
#     def __init__(self):
#         self.amount = 0
#         self.providers = []

#     def register(self, provider):
#         if isinstance(provider, Provider):
#             self.providers.append(provider)
#         else:
#             raise ValueError("Only Provider instances can be registered.")

#     def pay(self, provider, subscriber, amount):
#         if provider in self.providers:
#             if provider.register_payment(subscriber, amount):
#                 self.amount += amount
#                 print(f"Payment of {amount} accepted for provider {provider.name}.")
#             else:
#                 print(f"Payment of {amount} for provider {provider.name} failed.")
#         else:
#             print(f"Provider {provider.name} is not registered with this terminal.")

# class Provider:
#     def __init__(self, name):
#         self.name = name

#     def register_payment(self, subscriber, amount):
#         # Replace this with your payment registration logic.
#         # For example, you can update subscriber's balance.
#         # If the payment is successful, return True, otherwise, return False.
#         return True

# class Subscriber:
#     def __init__(self, name):
#         self.name = name

# # Пример использования классов:

# # Создаем экземпляры провайдеров и терминала
# provider1 = Provider("Provider A")
# provider2 = Provider("Provider B")
# terminal = Terminal()

# # Регистрируем провайдеров в терминале
# terminal.register(provider1)
# terminal.register(provider2)

# # Создаем подписчика
# subscriber = Subscriber("Alice")

# # Выполняем платеж
# payment_amount = 500.0
# p = 200
# terminal.pay(provider1, subscriber, payment_amount)
# terminal.pay(provider2, subscriber, p)

# # Проверяем баланс провайдера и сумму в терминале
# print(f"Provider A balance: {payment_amount}")
# print(f"Terminal amount: {terminal.amount}")
