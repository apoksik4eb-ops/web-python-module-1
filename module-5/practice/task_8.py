def input_marks():
    marks = []
    for i in range(1, 11):
        while True:
            mark = int(input(f"Введите оценку {i}: "))
            if 1 <= mark <= 12:
                marks.append(mark)
                break
            else:
                print("Оценка должна быть от 1 до 12.")
    return marks

marks = input_marks()

def list_marks(marks):
    print("Список оценок студента:")
    for i, mark in enumerate(marks, start=1):
        print(f"{i}: {mark}")

def remake_marks(marks):
    index = int(input("Введите номер экзамена для пересдачи: "))
    new_mark = int(input("Введите новую оценку: "))
    if 1 <= new_mark <= 12:
        marks[index] = new_mark
        print(f"Оценка {index} успешна обновлена на {new_mark}")
    else:
        print("Оценка должна быть от 1 до 12.")

def average_marks(marks):
    average = sum(marks) / len(marks)
    if average >= 10.7:
        print(f"Стипендия присвоена. Ваш средний бал {average}")
    else:
        print(f"В стипендии отказано. Ваш средний бал {average}")

def sort_marks(marks):
    sort_mode = input("Введите режим сортировки:\n 1. По возрастанию\n 2. По убыванию\n")
    if sort_mode == "1":
        sorted_marks = sorted(marks)
        print("Оценки по возрастанию", sorted_marks)
    elif sort_mode == "2":
        sorted_marks = sorted(marks, reverse=True)
        print("Оценки по убыванию", sorted_marks)
    else:
        print("Ошибка выбора.")

def main(marks):
    while True:
        print("Выберите действие:")
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Выходит ли стипендия")
        print("4. Сортировка списка")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        if choice == "1":
            list_marks(marks)
        elif choice == "2":
            remake_marks(marks)
        elif choice == "3":
            average_marks(marks)
        elif choice == "4":
            sort_marks(marks)
        elif choice == "5":
            break
        else:
            print("Неверный выбор")

main(marks)