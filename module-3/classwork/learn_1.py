# text = "row_1\nrow_2\nrow_3"

# print(text[0:7])
# print(text[0:3])
# print(text[::-1])

# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.swapcase())

# print(text.find("p"))
# print(text.index("j"))
# print(text.replace("pyt", "123", 2))

# print("Только буквы: ",text.isalpha())
# print("Только цифры: ", text.isdigit())
# print("Только буквы и цифры: ", text.isalnum())
# print("Пробелы: ", text.isspace())
# print("Заглавные: ", text.isupper())
# print("Прописные: ", text.islower())

# print(text.strip("*")) # очистка с левой и правой части
# print(text.lstrip()) # очистка левой части
# print(text.rstrip()) # очистка правой части

# f = text.split(", ") # если пусто разбивка по пробелам
# u = ", ".join(f) # объединение в строку
# print(f, u)

# sl = text.splitlines()
# print(sl)

# tuple_1 = (1,2,3)
# tuple_1 = tuple(range(0, 11))
# # tuple_3 = 1,2,3

# print(tuple_1[0])
# print(tuple_1[2:5])

# num1, *other, last_el = tuple(range(0, 11))
# print(num1, other, last_el)

# num1, _, num3, num4 = (1,2,3,4)
# print(num1, num3, num4)

# объединение
# tuple1 = (1,2)
# tuple2 = (3,4)
# result = tuple1 + tuple2
# print(result)

# повторение
# pattern = ("a", "b")
# repeated = pattern * 2
# print(repeated)

# принадлежность
# f = ("apple", "banana")
# print("apple" in f)

# методы кортежей
# numbers = (1,2,3,2,4,5,6,2)
# print(numbers.count(2)) # Считаем количество
# print(numbers.index(2)) # индекс первого вхождения поиск

# num_tuple = tuple(range(0,5))
# for index, num in enumerate(num_tuple):
#     print(index, num)

tuple_1_sym = ("b")
tuple_2_sym = ("b",)
print(tuple_1_sym, tuple_2_sym)