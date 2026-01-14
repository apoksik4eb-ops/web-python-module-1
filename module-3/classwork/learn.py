# my_list = [[1, 2], [3, 4]]
# lenght = len(my_list)
# print(lenght)

# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)

# numbers = [1, 2, 3, 4, 5]
# maximum = max(numbers)
# minimum = min(numbers)
# print(minimum, maximum)

# numbers = [3, 1, 7, 4, 8, 9, 2]
# sorted_nums = sorted(numbers, reverse=True)
# print(sorted_nums)

# numbers = [3, 1, 7, 4, 8, 9, 2]
# rev = reversed(numbers)
# print(list(rev))

# fruits = ["apple", "cherry", "banana"]
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")

# numbers = [1, 2, 3, 4, 5]
# s = list(map(lambda x: x**2, numbers))
# print(s)

# numbers = ["1", "2", "3"]
# s = list(map(int, numbers))
# print(s)

# def double(num):
#     return num * 2

# numbers = ["1", "2", "3"]
# s = list(map(int, numbers))

# list_double = list(map(double, s))
# print(list_double)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)

# def filter_func(num):
#     return num % 2 == 0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens = list(filter(filter_func, numbers))
# print(evens)

# words = ["paper", "apple", "car"]
# result = " ".join(words)
# print(result)

# my_list = ["apple", 2, "ban"]
# my_list.append(4)
# my_list.extend([5,6])
# print(my_list)

# my_list = ["apple", 2, "ban"]
# my_list_1 = ["banana", 3, "a"]
# new_list = my_list + my_list_1
# my_list += my_list_1
# print(new_list, my_list)

# my_list = ["apple", 2, "ban"]
# my_list.insert(1, "code")
# print(my_list)

# my_list = ["apple", 2, "ban"]
# my_list.insert(1, "apple")
# my_list.remove("apple")
# my_list.pop()
# my_list.pop(1)
# my_list.clear()
# print(my_list)

# my_list = [5,2,7,9,2,3,4,6]
# count = my_list.count(2)
# print(count)

# my_list = [5,2,7,9,2,3,4,6]
# # my_list.sort()
# # my_list.sort(reverse=True)
# my_list.reverse()
# print(my_list)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# print(my_list[:6])
# print(my_list[0:5])
# print(my_list[0:5:2])
# print(my_list[-1])
# print(my_list[:])
# print(my_list[-5:])
# print(my_list[::-1]) 

# my_list = [1,2,3,4,5,6,7,8,9,10]
# res = [x**2 for x in my_list]

# result = []
# for x in my_list:
#     result.append(x**2)

# print(res, result)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# res = [x for x in my_list if x % 2 == 0]

# print(res)

# my_list = [-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10]
# res = [0 if x < 0 else x for x in my_list]

# print(res)