all_symbols = []
all_strs = []

with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        for symbol in line:
            all_symbols.append(symbol)

        all_strs.append(line)

text = ''.join(all_symbols)
vowel_letters = "аеёиоуэюя"
consonant_letters = "бвгджзйклмнпрстфхцчшщ"
digits = "1234567890"
count_vowel_letters = 0
count_consonant_letters = 0
count_digits = 0        

for i in text.lower():
    if i in vowel_letters:
        count_vowel_letters += 1
    elif i in consonant_letters:
        count_consonant_letters += 1
    elif i in digits:
        count_digits += 1

with open("statistic.txt", "w", encoding="utf-8") as file:
    file.write("Статистика по исходному файлу:\n")
    file.write(f"Количество символов = {len(all_symbols)} шт.\n")
    file.write(f"Количество строк = {len(all_strs)} шт.\n")
    file.write(f"Количество гласных букв = {count_vowel_letters} шт.\n")
    file.write(f"Количество согласных букв = {count_consonant_letters} шт.\n")
    file.write(f"Количество цифр = {count_digits} шт.\n")