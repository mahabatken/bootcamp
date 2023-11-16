# Работа с файлами 
# Коретка - Указатель - Курсор

# open(<путь до файла>)

# file = open('files.py') #Относительный путь 
# ~ working - > Desktop/bootcamp.05/ lections/ files.property
# files -> lection/ files.py

# base_dir = 

# file  = open ('files.py')
# data = file.read()
# print(data, type(data))
# file.close



# Режимы работы с файлами 
# 1. r/r+/ rb _-> read - для читение файлов 
# 2. w/w+/wb -> write - для записи файла 
# 3. a/a+ -> append - для добавление двнных 
# b , x -> 



# file = open ('test.txt','r')
# print(file.read())
# file.close()


# file = open ('test.txt','r') # считывает линии , переводит в список
# print(file.readlines())
# file.close()

# file = open ('test.txt','r') # считывает одну сторку 
# print(file.readline())
# file.close()


# file.tell() - Возврашает индекс где находтся курсор (указаатель)
# file.seek() - Перемишает курсор на индекс которую вы передали 

# file = open ('test.txt', 'r')
# print(file.tell())
# data = file.read()
# print(data,'!!')
# print(file.tell())# 275
# file.seek(0)
# print(file.tell()) # 0
# print(file.read())
# print(file.tell())
# file.close()

# контексный менеджер 
# with open ("test.txt", "r")as file: # file = open()
#     date = file.read()
#     print(date)
#     print(file, "inside")

# print (file.read(),"outside")


# with open ("test.txt", "w")as file:
#     file.write("Pervaya stroka!")
#     file.write("\nHe is bastard of Ned Stark!\n")
#     file.write("This is lection about files!")
#     file.seek(0)
#     data = [" Test 1 stroka\n!", "test 2 strpka!"]
#     file.writelines(data)

# with open("test.txt", "a") as f:
#     f.write("\nJohn Snow is Kind of North!")
#     f.write("\nYou know nothind John Snow !")
#     f.seek(0)
#     print(f.read())

# from PIL import Image
# import pytesseract
# import re 
# base_url = "/home/mahabat/Desktop/bootcamp.05/files/lections/"

# def get_imei_code(image:str):
#     string = pytesseract.image_to_string(image)
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

# image = base_url +"imei.jpg"
# get_imei_code(image) 


