def sum(num1, num2):
    total = 0
    for num in range(num1, num2 + 1):
        total += num

    print(f"Сумма чисел в указанном диапазоне = {total}")   
sum(1,5)