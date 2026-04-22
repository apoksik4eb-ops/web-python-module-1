number_list = (input("Введите список чисел: "))
num = list(map(int, number_list.split()))
print(f"Сумма всех введеных чисел = {sum(num)}")
print(f"Среднеарифметическое всех введеных чисел = {sum(num) / len(num)}")