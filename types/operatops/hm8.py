# import random

# def loto_simulation():
#     numbers = [f"{letter}{i}" for letter in "BINGO" for i in range(1, 16)]
#     random.shuffle(numbers)
#     winning_card = set(random.sample(numbers, 24))

#     turns = 0
#     while True:
#         turns += 1
#         number = numbers.pop()
#         if number in winning_card:
#             break

#     return turns

# simulations = 1000
# results = []
# for _ in range(simulations):
#     results.append(loto_simulation())

# min = min(results)
# max = max(results)
# avg = sum(results) / simulations

# print("Минимальное количество извлечений номеров для выигрыша:", min)
# print("Максимальное количество извлечений номеров для выигрыша:", max)
# print("Среднее количество извлечений номеров для выигрыша:", avg)


s={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}
mass= input('введите сообщение : ').upper()
s_mass=[]

for char in mass:
    if char in s:
        s_mass.append(s[char])
s_text= ' '.join(s_mass)
print('азбука ', s_text)


