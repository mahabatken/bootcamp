
number = 50

blacklist = ["Нурсултан", "Вероника", "Айкена"]

user_name = input("Введите имя пользователя: ")


while True:
    if user_name in blacklist:
        print("Вы в черном списке.")
        break

    chislo = int(input('Угадай число: '))

    if chislo == number:
        print('Ты угадал!')
        break
    elif 40 < chislo < 50 or 50 < chislo < 60:
        print('Ты был очень близок!')
    else:
        print('Ты был далеко!')





