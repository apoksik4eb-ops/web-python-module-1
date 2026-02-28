employes = []

with open("employes_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        surname, name, patronymic = parts[0], parts[1], parts[2]
        age = int(parts[3])
        
        employes.append({
            "Фамилия": surname,
            "Имя": name,
            "Отчество": patronymic,
            "Возраст": age
        })

def list_employes():
    if not employes:
        print("Список сотрудников пуст")
        return
    print("Список сотрудников:")
    for employe in employes:
        print(f"Фамилия: {employe["Фамилия"]}, Имя: {employe["Имя"]}, Отчество: {employe["Отчество"]}, Возраст: {employe["Возраст"]}")

def add_employes():
    new_surname = input("Введите фамилию: ")
    new_name = input("Введите имя: ")
    new_patronymic = input("Введите отчество: ")
    new_age = int(input("Введите возраст: "))

    employes.append({
        "Фамилия": new_surname,
        "Имя": new_name,
        "Отчество": new_patronymic,
        "Возраст": new_age
    })

    print(f"Сотрудник {new_surname} {new_name} {new_patronymic} добавлен.")

def replace_employes():
    if not employes:
        print("Список сотрудников пуст.")
        return

    surname = input("Введите фамилию сотрудника для редактирования: ")
    for employe in employes:
        if employe["Фамилия"] == surname:
            employe["Фамилия"] = input(f"Фамилия ({employe["Фамилия"]}): ") or employe["Фамилия"]
            employe["Имя"] = input(f"Имя ({employe["Имя"]}): ") or employe["Имя"]
            employe["Отчество"] = input(f"Отчество ({employe["Отчество"]}): ") or employe["Отчество"]
            employe["Возраст"] = int(input(f"Возраст ({employe["Возраст"]}): "))
            print("Данные сотрудника обновлены!")
            return
    print("Сотрудник с такой фамилией не найден.")

def find_employes():
    choice = int(input("Выберите тип поиска:\n1. По фамилии\n2. По первой букве фамилии\n3. По возрасту\n"))

    if choice == 1:
        surname = input("Введите фамилию: ")
        found = []
        for employe in employes:
            if employe["Фамилия"] == surname:
                found.append(employe)
    elif choice == 2:
        letter = input("Введите первую букву фамилии: ")
        found = []
        for employe in employes:
            if employe["Фамилия"].startswith(letter):
                found.append(employe)
    elif choice == 3:
        age = int(input("Введите возраст: "))
        found = []
        for employe in employes:
            if employe["Возраст"] == age:
                found.append(employe)
    else:
        print("Неверный выбор.")
        return

    if found:
        print(f"Найдено {len(found)} сотрудников:")
        for employe in found:
            print(f"Фамилия: {employe['Фамилия']}, Имя: {employe['Имя']}, Отчество: {employe['Отчество']}, Возраст: {employe['Возраст']}")
    else:
        print("Сотрудники не найдены.")

def delete_employes():
    delete = input("Введите фамилию: ")
    for i, employe in enumerate(employes):
        if employe["Фамилия"] == delete:
            del employes[i]
            print(f"Сотрудник с фамилией {delete} удалён.")
            return

    print("Сотрудник с такой фамилией не найден.")

def save_files():
    with open("employes_log.txt", "w", encoding="utf-8") as file:
        for employe in employes:
            file.write(f"{employe["Фамилия"]},{employe["Имя"]},{employe["Отчество"]},{employe["Возраст"]}\n")

    with open("employes_list.txt", "w", encoding="utf-8") as file:
        file.write("Список сотрудников:\n")
        for employe in employes:
            file.write(f"Фамилия: {employe["Фамилия"]}\nИмя: {employe["Имя"]}\nОтчество: {employe["Отчество"]}\nВозраст: {employe["Возраст"]}\n" + "\n")

def main():
    while True:
        print("1. Показать всех сотрудников")
        print("2. Добавить сотрудника")
        print("3. Редактировать сотрудника")
        print("4. Найти сотрудника")
        print("5. Удалить сотрудника")
        print("6. Сохранить данные в файлы")
        print("0. Выход")

        choice = int(input("Выберите действие: "))

        if choice == 1:
            list_employes()
        elif choice == 2:
            add_employes()
        elif choice == 3:
            replace_employes()
        elif choice == 4:
            find_employes()
        elif choice == 5:
            delete_employes()
        elif choice == 6:
            save_files()
        elif choice == 0:
            save_files()
            print("Программа завершена.")
            break

main()