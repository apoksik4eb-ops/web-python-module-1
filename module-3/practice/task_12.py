numbers = [1,2,-2,-4,5,7,10,3,6,3,-4,-7,-7,]

print(f"Сумма отрицательных чисел = {sum(list(filter(lambda x: x < 0, numbers)))}")
print(f"Сумма четных чисел = {sum(list(filter(lambda x: x % 2 == 0, numbers)))}")
print(f"Сумма нечетных чисел = {sum(list(filter(lambda x: x % 2 != 0, numbers)))}")

result = 1
for num in numbers:
    if num % 3 == 0:
        result *= num
print(f"Произведение чисел кратных 3 = {result}")

# print([1 * num for num in numbers if num % 3 == 0])

print(f"Произведение минимального и максимального чисел = {min(numbers) * max(numbers)}")

new_numbers = []
for num in numbers:
    if num > 0:
        new_numbers.append(num)
print(new_numbers)