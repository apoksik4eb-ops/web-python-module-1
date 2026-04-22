text = "Hello World"
replacement = {"e": 1, "l": 0, "o": 2, "r": 3}
result = ""

for key in text:
    result += str(replacement.get(key, key))
print(result)