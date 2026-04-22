pair = int(input("Введите количество пар 'ключ-значение' необходимо создать: "))
d = {}
for i in range(pair):
    key = input(f"Введите значение ключа {i + 1}: ")
    value = input(f"Введите название значения {i + 1}: ")
    d.setdefault(key, value)
print(d)