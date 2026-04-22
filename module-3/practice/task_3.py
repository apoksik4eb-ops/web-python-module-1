numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18]
total = sum(numbers) / len(numbers)
print(total)
print(list(num for num in numbers if num > total))