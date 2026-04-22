codes = [919,903,917,905,987]
phones = [2238712,1115533,5552678,3345122,7770011]
full_numbers = list(zip(codes, phones))

def list_numbers():
    print("Cписок телефонов: ")
    for code, phone in full_numbers:
        print(f"7({code}){phone}")

def sort_by_codes():
    sort_codes = sorted((full_numbers))
    print("Отсортированный список по кодам телефонов: ")
    for code, phone in sort_codes:
        print(f"7({code}){phone}")

def sort_by_phones():
    sort_phones = sorted((full_numbers), key = lambda x: x[1])
    print("Отсортированный список по номерам телефонов: ")
    for code, phone in sort_phones:
        print(f"7({code}){phone}")

def main():
    while True:
        print("Выберите действие:")
        print("1. Список номеров.")
        print("2. Сортирока по кодам.")
        print("3. Сортировка по номерам.")
        print("4. Выход.")

        choice = input("Введите действие: ")
        if choice == "1":
            list_numbers()
        elif choice == "2":
            sort_by_codes()
        elif choice == "3":
            sort_by_phones()
        elif choice == "4":
            break
        else:
            print("Неверный выбор")

main()