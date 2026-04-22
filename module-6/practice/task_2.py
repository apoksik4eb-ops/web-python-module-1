fruits = ("яблоко", "банан", "апельсин", "бананяблоко", "вишня-яблоко")
fruit = input("Введите фрукт: ")
count = 0
for el in fruits:
    if fruit in el:
        count += 1
print(count)