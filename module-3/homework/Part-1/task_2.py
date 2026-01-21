text = input("Введите текст: ")
words = input("Введите зарезервированные слова: ")

for word in words:
    text = text.replace(word, word.upper())

print(text)
