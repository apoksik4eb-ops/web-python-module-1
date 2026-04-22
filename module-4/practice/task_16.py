import random

def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits[:4]))

def count_bulls_and_cows(secret, guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return cows, bulls

def is_valid_guess(s):
    if not s.isdigit() or len(s) != 4 or s[0] == '0':
        return False
    return len(set(s)) == 4

def game_loop(secret, attempts=0):
    guess = input("Введите ваше предположение (4-значное число, цифры не повторяются): ").strip()

    if not is_valid_guess(guess):
        print("Некорректный ввод! Должно быть 4-значное число с неповторяющимися цифрами, первая цифра ≠ 0.")
        return game_loop(secret, attempts)

    attempts += 1

    if guess == secret:
        print(f"Поздравляю! Вы угадали число {secret} за {attempts} попыток.")
        return

    cows, bulls = count_bulls_and_cows(secret, guess)
    print(f"Коровы: {cows}, Быки: {bulls}")

    game_loop(secret, attempts)

def main():
    print("Добро пожаловать в игру «Быки и коровы»!")
    print("Я загадал 4-значное число с неповторяющимися цифрами. Угадайте его!")
    print("Коровы — цифры угаданы и на своих местах.")
    print("Быки — цифры есть в числе, но не на своих местах.")
    
    secret = generate_secret()
    game_loop(secret)

main()


