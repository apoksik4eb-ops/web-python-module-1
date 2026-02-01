def separation(a, b):
    if b == 0:
        return a
    else:
        return separation(b, a % b)

print(f"Наибольший общий делитель чисел 96 и 24 равен {separation(96, 24)}")