names = ["Гарри Поттер","Незнайка на луне","Хоббит","Котектив","Охотники за мифами"]
years = [1999,1995,1958,2026,2022]
full_title = list(zip(names, years))

def list_full_title():
    print("Cписок книг: ")
    for name, year in full_title:
        print(f"{name} - {year} год")

def sort_by_names():
    sort_names = sorted((full_title))
    print("Отсортированный список по названиям: ")
    for name, year in sort_names:
        print(f"{name} - {year} год")

def sort_by_years():
    sort_years = sorted((full_title), key = lambda x: x[1])
    print("Отсортированный список по годам: ")
    for name, year in sort_years:
        print(f"{name} - {year} год")

def main():
    while True:
        print("Выберите действие:")
        print("1. Список книг.")
        print("2. Сортирока по названиям.")
        print("3. Сортировка по годам.")
        print("4. Выход.")

        choice = input("Введите действие: ")
        if choice == "1":
            list_full_title()
        elif choice == "2":
            sort_by_names()
        elif choice == "3":
            sort_by_years()
        elif choice == "4":
            break
        else:
            print("Неверный выбор")

main()