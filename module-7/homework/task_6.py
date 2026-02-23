find_word = input("Введите слово для поиска: ").strip().lower()
replace_word = input("Слово для замены: ").strip()

with open("text.txt", "r", encoding="utf-8") as file:
    word = file.read()

new_word = word.replace(find_word, replace_word)

with open("text.txt", "w", encoding="utf-8") as file:
    file.write(new_word)