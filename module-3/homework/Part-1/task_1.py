text = input("Введите текст: ")
palin = text.replace(" ", "").lower()
reverse = palin[::-1]

if reverse == palin:
    print(f"{text} - это палиндром")
else:
    print(f"{text} - это не палиндром")