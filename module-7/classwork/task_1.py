"""
ЗАДАЧА: Учёт инвентаря на складе

Формат строки:
дата,товар,тип,количество

Операции:
2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,IN,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5

Типы операций:
- IN  : поступление товара
- OUT : отгрузка товара

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Создать файл inventory.txt с операциями склада

2. Прочитать файл и загрузить все операции.

3. Для каждого товара:
   - посчитать итоговое количество на складе
   - посчитать общее количество поступивших единиц
   - посчитать общее количество отгруженных единиц

4. Найти товары:
   - у которых итоговое количество < 0 (ошибка учёта)
   - которые ни разу не поступали, но отгружались

5. Найти товар с:
   - максимальным количеством поступлений
   - максимальным количеством отгрузок

6. Сформировать множество всех дат,
   когда происходили операции с товаром "яблоко".

7. Записать подробный отчёт в файл report.txt.

- ОТЧЁТ ПО СКЛАДУ
- Итоговые остатки
- Общее поступление
- Общая отгрузка
- Товары с отрицательным остатком:
- Товары без поступлений, но с отгрузкой:
- Товар с максимальным поступлением:
- Товар с максимальной отгрузкой:
- Даты операций с яблоком:
"""
with open("inventory.txt", "w", encoding="utf-8") as file:
      file.write("2024-01-01,яблоко,IN,50\n")
      file.write("2024-01-02,банан,IN,30\n")
      file.write("2024-01-03,яблоко,OUT,10\n")
      file.write("2024-01-03,груша,OUT,5\n")
      file.write("2024-01-04,груша,IN,20\n")
      file.write("2024-01-05,банан,OUT,40\n")
      file.write("2024-01-06,яблоко,OUT,5")

ins, outs, result, max_in, max_out = {}, {}, {}, {}, {}
in_prod, out_prod = set(), set()
result_prod, date_apple = [], []

with open("inventory.txt", "r", encoding="utf-8") as file:
   for line in file:
      date, product, operation, quantity = line.split(",")
      quantity = int(quantity)

      ins.setdefault(product, 0)
      if operation == "IN":
         ins[product] += quantity
         in_prod.add(product)
      
      outs.setdefault(product, 0)
      if operation == "OUT":
         outs[product] += quantity
         out_prod.add(product)

      result[product] = ins[product] - outs[product]
      
      if product == "яблоко":
         date_apple.append(date)

negativ_products = []
for product, quantity in result.items():
   if quantity < 0:
      negativ_products.append(product)

for product in out_prod:
   if product not in in_prod:
      result_prod.append(product)
if len(result_prod) == 0:
   print("пусто")
else:
   print(result_prod)

max_in_fruit = None
max_in_count = 0
for fruit, count in ins.items():
   if count > max_in_count:
      max_in_fruit = fruit
      max_in_count = count
max_in[max_in_fruit] = max_in_count

max_out_fruit = None
max_out_count = 0
for fruit, count in outs.items():
   if count > max_out_count:
      max_out_fruit = fruit
      max_out_count = count
max_out[max_out_fruit] = max_out_count

with open("report.txt", "w", encoding="utf-8") as file:
   file.write("ОТЧЁТ ПО СКЛАДУ:\n")
   file.write("- Итоговые остатки\n")
   for key, value in result.items():
      file.write(f"Товар {key} остаток = {value} шт.\n")
   file.write("- Общее поступление\n")
   for key, value in ins.items():
      file.write(f"Товар {key} поступление = {value} шт.\n")
   file.write("- Общая отгрузка\n")   
   for key, value in outs.items():
      file.write(f"Товар {key} отгрузка = {value} шт.\n")
   file.write("- Товары с отрицательным остатком:\n")
   for fruit in negativ_products:
      file.write(f"{fruit}\n")
   file.write("- Товары без поступлений, но с отгрузкой:\n")
   for word in result_prod:
      file.write(f"{word}\n")
   file.write("- Товар с максимальным поступлением:\n")
   for key, value in max_in.items():
      file.write(f"Товар {key} = {value} шт.\n")
   file.write("- Товар с максимальной отгрузкой:\n")
   for key, value in max_out.items():
      file.write(f"Товар {key} = {value} шт.\n")
   file.write("- Даты операций с яблоком:\n")
   for date in date_apple:
      file.write(f"Операции были {date}\n")
