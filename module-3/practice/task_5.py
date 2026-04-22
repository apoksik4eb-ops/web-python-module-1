text = input("Введите текст: ")
letter = 0
digit = 0
for x in text:
    if x.isalpha():
        letter += 1
    elif x.isdigit():
        digit +=1
print(letter, digit)
