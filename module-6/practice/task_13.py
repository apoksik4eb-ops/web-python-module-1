dictionary = {
    "apple": "яблоко",
    "banana": "банан",
    "cherry": "вишня",
    "pineapple": "ананас"
    }

def list_word():
    if dictionary:
        print("Список слов в словаре:")
        for english_word, russian_word in dictionary.items():
            print(f"{english_word} - {russian_word}")
    else:
        print("Список слов пуст.")

def add_word():
    english_word = input("Введите английское слово для добавления: ")
    russian_word = input("Введите перевод этого слова на русский: ")
    dictionary[english_word] = russian_word
    print(f"Добавлено слово - {english_word}. Его перевод - {russian_word}")

def delete_word():
    english_word = input("Введите слово для удаления: ")
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Из словаря удалено слово - {english_word}.")
    else:
        print(f"В словаре не найдено слово - {english_word}.")

def search_word():
    english_word = input("Введите слово для поиска: ")
    if english_word in dictionary:
        print(f"{english_word} - {dictionary[english_word]}")
    else:
        print(f"В словаре не найдено слово - {english_word}.")

def replace_word():
    english_word = input("Введите слово для замены: ")
    if english_word in dictionary:
        choise = int(input("Какую информацию заменить:\n 1. Слово\n 2. Перевод\n"))
        if choise == 1:
            new_english_word = input(f"Введите обновленное слово для - {english_word}: ")
            dictionary[new_english_word] = dictionary.pop(english_word)
            print(f"Слово {english_word} обновлено. Его новое значение {new_english_word}.")
        elif choise == 2:    
            new_russian_word = input(f"Введите обновленный перевод слова - {english_word}: ")
            dictionary[english_word] = new_russian_word
            print(f"Обновлен перевод слова - {english_word}. Его обновленный перевод - {new_russian_word}.")
        else:
            print("Неверный выбор.")
    else:
        print(f"В словаре не найдено слово - {english_word}.")

def main():
    while True:
        print("Меню:")
        print("1. Список слов в словаре.")
        print("2. Добавить в словарь новое слово.") 
        print("3. Удалить слово из словаря.")
        print("4. Найти слово в словаре")
        print("5. Заменить слово или его перевод в словаре")
        print("6. Выход")
        choice = int(input("Выберите пункт меню: "))
        if choice == 1:
            list_word()
        elif choice == 2:
            add_word()
        elif choice == 3:
            delete_word()
        elif choice == 4:
            search_word()
        elif choice == 5:
            replace_word()
        elif choice == 6:
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Выберите пункт от 1 до 6.")

main()