library = {
    "Война и мир": {"автор": "Лев Николаевич Толстой", "жанр": "роман", "год выпуска": "2017", "количество страниц": "1424", "издательство": "Речь"},
    "Идиот": {"автор": "Фёдор Михайлович Достоевский", "жанр": "роман", "год выпуска": "2023", "количество страниц": "640", "издательство": "Азбука"}
    }

def list_book():
    print("Все книги библиотеки:")
    if not library:
        print("В базе нет книг.")
        return
    
    for title, info in library.items():
        print(f"Название книги: {title}")
        for key, value in info.items():
            print(f"  {key}: {value}")
        print("")

def add_book():
    title = input("Введите название книги: ")
    if title in library:
        print("Книга с таким названием уже существует!")
        return
    
    author = input("Введите автора: ")
    genre = input("Введите жанр: ")
    year = input("Введите год выпуска: ")
    pages = input("Введите количество страниц: ")
    publishing = input("Введите издательство: ")
    
    library[title] = {
        "автор": author,
        "жанр": genre,
        "год выпуска": year,
        "количество страниц": pages,
        "издательство": publishing
    }
    print("Книга успешно добавлена.")

def delete_book():
    title = input("Введите название книги для удаления: ")
    if title in library:
        del library[title]
        print(f"Информация о книге {title} удалена.")
    else:
        print(f"Книга {title} не найдена.")

def find_book():
    title = input("Введите название книги для поиска: ")
    if title in library:
        print(f"Информация о книге {title}:")
        for key, value in library[title].items():
            print(f"  {key}: {value}")
        print()
    else:
        print("Книга не найдена.")

def replace_book():
    title = input("Введите название книги: ")
    if title in library:
        choiсe = input("Какую информацию необходимо заменить:\n 1. Автор \n 2. Жанр\n 3. Год выпуска\n 4. Количество страниц\n 5. Издательство\n")
    
        if choiсe == "1":
            new_author = input("автор: ")
            library[title]["автор"] = new_author
        if choiсe == "2":
            new_genre = input("жанр: ")
            library[title]["жанр"] = new_genre
        if choiсe == "3":
            new_year = input("год выпуска: ")
            library[title]["год выпуска"] = new_year
        if choiсe == "4":
            new_pages = input("количество страниц: ")
            library[title]["количество страниц"] = new_pages
        if choiсe == "5":
            new_publishing = input("издательство: ")
            library[title]["издательство"] = new_publishing
      
        print(f"Данные книги {title} обновлены!")

    else:
        print(f"Книга {title} не найдена")

def main():
    while True:
        print("Выберите действие:")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Найти книгу")
        print("5. Заменить данные книги")
        print("6. Выйти")
        
        choice = input("Выберите действие (1–6): ")
        
        if choice == "1":
            list_book()
        elif choice == "2":
            add_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            find_book()
        elif choice == "5":
            replace_book()
        elif choice == "6":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

main()
