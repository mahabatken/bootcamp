# welcome = 'Hello a studient'
# name = 'Mahabat'
# syrname = 'Keneshova'
# patronymis = 'Aitkylovna'
# birth_year = '1990'
# print(f"{welcome} {name.capitalize()} {syrname.upper()} {patronymis.lower()}\n {birth_year},\n\t Pad privetstvovanm v nashei akademii!")                     



# a = 5
# b = 6
# print(a % b)
# print(a == b)
# print(a > b)
# print(a < b)


# chislo = int(input('Vvedite chislo ot 1 do 10:'))
# if chislo == 7:
#     print(f'Браво, Вольф Мессинг!')
# else:
#     print('Не угадал!')
#6--------------


# flag = True
# symbol = '0123456789' + '-'  + '.'

# while flag :
#     print()
#     num1 = input('vvedint pervoe  chislo:')
#     is_correct = True
#     for x in num1:
#         if x not in symbol:
#             print("vvedeny ne pravilno chislo!")
#             is_correct = False
#             break
#     if not is_correct:
#             continue
        
   
#     num2 = input('vvedint vtoroe  chislo:')
#     is_correct = True
#     for x in num2: 
#         if x not in symbol:
#             print("vvedeny ne pravilno chislo!")
#             is_correct = False
#             break
#     if not is_correct:
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)

#     # print(num1, type(num1))

#     operator = input('Введите операцию(+, -, *, /): ').strip()
#     if operator == '+':
#         print(f'Результат:{num1 + num2}') 
#     elif operator == '-':
#         print(f'Результат:{num1 - num2}') 
#     elif operator == '*':
#         print(f'Результат:{num1 * num2}')
#     elif operator == '/':
#         print(f'Результат:{num1 / num2}' if num2 !=0 else 'На ноль делить нельзя!')
#     else:
#          print('Вы вели не правильный оператор!')

#     choice = input('Хотите продолжить?(yes/no):')
#     if choice.lower().strip() != 'yes':
#         flag = False
#         print("Пока пока!")