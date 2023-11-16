#1
# def подсчет_регистров(строка):
#     верхний_регистр = 0
#     нижний_регистр = 0

#     for символ in строка:
#         if символ.isupper():
#             верхний_регистр += 1
#         elif символ.islower():
#             нижний_регистр += 1

#     return верхний_регистр, нижний_регистр

# результат = подсчет_регистров("Maхабат Кен")
# print("Верхний регистр:", результат[0])
# print("Нижний регистр:", результат[1])

# #2
# def генерация_кубов(n):
#     словарь_кубов = {}

#     for число in range(1, n + 1):
#         словарь_кубов[число] = число ** 3

#     return словарь_кубов
# результат = генерация_кубов(5)
# print(результат)

# #3
# def sum_range(start, end):
#     if start > end:
#         start, end = end, start

#     сумма = sum(range(start, end + 1))

#     return сумма
# результат = sum_range(5, 10)
# print(результат)

# 4/
# def is_isogram(слово):
#     слово = слово.lower()

#     return len(слово) == len(set(слово))
# результат = is_isogram("кот")
# print(результат)

#5
# def count_words(sentence):
#     word_count = {}
#     words = sentence.split()

#     for word in words:
#         word = word.strip('.,!?"\'').lower()

#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     return word_count

# phrase = "Money, money, money, it’s always sunny, in the richmen’s world"
# result = count_words(phrase)
# print(result)