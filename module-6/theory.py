my_set = {1,1,2,2,3,3}
print(my_set)

my_set_1 = set([1,2,3,3,4])
print(my_set_1)

letter = set("привет")
print(letter)

set_tuple = set((1,1,2,2,3,3))
print(set_tuple)

# Генератор множеств
my_set = {x for x in range(5)}
print(my_set)

# Добавление элементов
fruits = {"яблоко", "банан", "апельсин"}
fruits.add("груша")
fruits.update(["смородина", "клубника"])
print(fruits)

# Удаление элементов
fruits = {"яблоко", "банан", "апельсин"}
fruits.remove("яблоко")
fruits.discard("груша")
fruits.pop()
print(fruits)

# Операции над множествами
# 1. Объединение
set_a = {1,2,3,4}
set_b = {4,5,6,7}
result = set_a.union(set_b) # метод
result_operator = set_a | set_b # оператор
set_a |= set_b # присвоение
print(set_a, result, result_operator)

# 2. Пересечение
set_a = {1,2,3,4}
set_b = {3,4,5,6}
result = set_a.intersection(set_b) # метод
result_operator = set_a & set_b # оператор
set_a &= set_b # присвоение
print(result, result_operator, set_a)

# 3. Разность
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
result = set_a.difference(set_b) # метод
result_operator = set_a - set_b # оператор
set_a -= set_b # присвоение
print(result, result_operator, set_a)

# 4. Симметрическая разность
set_a = {1,2,3,4}
set_b = {3,4,5,6}
result = set_a.symmetric_difference(set_b) # метод
result_operator = set_a ^ set_b # оператор
set_a ^= set_b # присвоение
print(result, result_operator, set_a)

my_set = {1,2,3}
print(3 in my_set)
print(5 not in my_set)
print(len(my_set)) # длина множества
print(sum(my_set)) # сумма множества
print(min(my_set), max(my_set)) # Мин/Макс число в множестве

for num in my_set:
    print(num)