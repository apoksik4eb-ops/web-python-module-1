word = "позавчера"
count_word = 0

with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        if word in line.lower().split():
            count_word += 1
print(f"Слово {word} встречается {count_word} раза")
