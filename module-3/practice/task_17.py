numbers = [23,45,87,-23,-56,0,21,0,59,-17]

minimum = min(numbers)
maximum = max(numbers)
minus = len(list(filter(lambda x: x < 0, numbers)))
plus = len(list(filter(lambda x: x > 0, numbers)))
zero = len(list(filter(lambda x: x == 0, numbers)))

print(f"Минимальное число {minimum}")
print(f"Максимальное число {maximum}")
print(f"Количество отрицательных чисел {minus}")
print(f"Количество положительных чисел {plus}")
print(f"Количество нулей {zero}")