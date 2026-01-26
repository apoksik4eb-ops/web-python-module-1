def sum(a, b):
    if a == b:
        return b
    return b + sum(a, b - 1)

print(sum(1, 3))