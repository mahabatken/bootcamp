1
# def get_sorted_names(input_list):
#     names = [name.capitalize() for name in input_list if isinstance(name, str)]
#     sorted_names = sorted(names)
#     return sorted_names

# def print_reverse_sorted_integers(input_list):
#     integers = [item for item in input_list if isinstance(item, int)]
#     integers.sort(reverse=True)
#     for num in integers:
#         print(num)

# def get_sum_of_floats(input_list):
#     floats = [item for item in input_list if isinstance(item, float)]
#     total = sum(floats)
#     return total
# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]

# sorted_names = get_sorted_names(list_1)
# print("Отсортированные имена:", sorted_names)

# print("Целочисленные значения в обратном порядке:")
# print_reverse_sorted_integers(list_1)

# sum_of_floats = get_sum_of_floats(list_1)
# print("Сумма чисел с плавающей точкой:", sum_of_floats)

#2

# def describe_sandwich(size, components):
#     size_description = {
#         "Большой": "Большой сэндвич со следующими ингредиентами: ",
#         "Средний": "Средний сэндвич со следующими ингредиентами: ",
#         "Маленький": "Маленький сэндвич со следующими ингредиентами: ",
#     }
    
#     if size in size_description:
#         description = size_description[size]
#         description += ", ".join(components)
#         print(description)
#     else:
#         print("Извините, размер сэндвича не распознан.")

# describe_sandwich("Большой", ["огурец", "колбаса", "сыр"])
# describe_sandwich("Средний", ["томат", "кетчуп"])
# describe_sandwich("Маленький", ["варенье"])

#3
# def make_car(manufacturer, model, **kwargs):
#     car_info = {
#         "manufacturer": manufacturer,
#         "model": model,
#     }
#     car_info.update(kwargs)
    
#     car_description = f"{manufacturer} {model}"
    
#     for key, value in car_info.items():
#         car_description += f", {key} is {value}"
    
#     return car_description

# car = make_car('Subaru', 'Outback', color='blue', engine='V8')
# print(car)

#4

# def count_letters(text):
#     letter_count = 0
#     digit_count = 0
#     for char in text:
#         if char.isalpha():  
#             letter_count += 1
#         elif char.isdigit():  
#             digit_count += 1
#     print(f"Количество букв: {letter_count}")
#     print(f"Количество цифр: {digit_count}")
# text = "Привет. Меня зовут  Нурай мне 12 лет."
# count_letters(text)

#5
def generate_employee_sentences(employee_data):
    ls = []
    for name, position in employee_data.items():
        ls= f"Работник {name}, занимает должность {position}"
        ls.append(sentence)
    return ls
employee_data = {
    "Асан": "Директор",
    "Бекзат": "Менеджер",
    "Гульназ": "Инженер",
}

ls = generate_employee_sentences(employee_data)
for sentence in ls:
    print(ls)






          