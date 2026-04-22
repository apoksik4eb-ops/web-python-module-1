def symbol(n):
    if n == 1:
        return "*"
    return "*" + symbol(n - 1)

print(symbol(10))