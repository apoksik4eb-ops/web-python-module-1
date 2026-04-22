firm = {
    "Иванов Иван Иванович": {"телефон": "20-20-20", "email": "ivanov@ya.ru", "должность": "директор", "№ кабинета": "215", "skype": "ivanov_skype"},
    "Егоров Егор Егорович": {"телефон": "30-30-30", "email": "egorov@ya.ru", "должность": "экономист", "№ кабинета": "205", "skype": "egorov_skype"}
    }

def list_employee():
    print("Все сотрудники фирмы:")
    if not firm:
        print("В базе нет сотрудников.")
        return
    
    for fio, info in firm.items():
        print(f"ФИО: {fio}")
        for key, value in info.items():
            print(f"  {key}: {value}")
        print("")

def add_employee():
    fio = input("Введите ФИО: ")
    if fio in firm:
        print("Сотрудник с таким ФИО уже существует!")
        return
    
    phone = input("Введите телефон: ")
    email = input("Введите email: ")
    position = input("Введите занимаемую должность: ")
    room = input("Введите номер кабинета: ")
    skype = input("Введите Skype: ")
    
    firm[fio] = {
        "Телефон": phone,
        "Email": email,
        "Должность": position,
        "Кабинет": room,
        "Skype": skype
    }
    print("Сотрудник успешно добавлен!")

def delete_employee():
    fio = input("Введите ФИО сотрудника для удаления: ")
    if fio in firm:
        del firm[fio]
        print("Информация о сотруднике удалена.")
    else:
        print("Такой сотрудник не найден.")

def find_employee():
    fio = input("Введите ФИО сотрудника для поиска: ")
    if fio in firm:
        print(f"Информация о сотруднике {fio}:")
        for key, value in firm[fio].items():
            print(f"  {key}: {value}")
        print()
    else:
        print("Сотрудник не найден.")

def replace_employee():
    fio = input("Введите ФИО сотрудника: ")
    if fio in firm:
        choise = input("Какую информацию необходимо заменить:\n 1. Телефон \n 2. Email\n 3. Должность\n 4. № кабинета\n 5. Skype\n")
    
        if choise == "1":
            phone = input("Телефон: ")
            firm[fio]["телефон"] = phone
        if choise == "2":
            email = input("Email: ")
            firm[fio]["Email"] = email
        if choise == "3":
            position = input("Должность: ")
            firm[fio]["Должность"] = position
        if choise == "4":
            room = input("Номер кабинета: ")
            firm[fio]["Кабинет"] = room
        if choise == "5":
            skype = input("Skype: ")
            firm[fio]["Skype"] = skype
      
        print(f"Данные сотрудника {fio} обновлены!")

    else:
        print(f"Сотрудник {fio} не найден")

def main():
    while True:
        print("Выберите действие:")
        print("1. Показать всех сотрудников")
        print("2. Добавить сотрудника")
        print("3. Удалить сотрудника")
        print("4. Найти сотрудника")
        print("5. Заменить данные сотрудника")
        print("6. Выйти")
        
        choice = input("Выберите действие (1–6): ")
        
        if choice == "1":
            list_employee()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            find_employee()
        elif choice == "5":
            replace_employee()
        elif choice == "6":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

main()
