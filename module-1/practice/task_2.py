number = input("Введите четырех значное число: ")

result = 1
for num in number:
    digit = int(num)
    result *= digit
print(f"Результат умножения введеных чисел = {result}")