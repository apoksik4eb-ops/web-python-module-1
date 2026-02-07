bascketball_players = {
    "Абрамов Абрам": 183,
    "Борисов Борис": 185,
    "Владимиров Владимир": 190,
    "Дмитриев Дмитрий": 200
    }

def list_players():
    if bascketball_players:
        print("Список баскетболистов:")
        for name, height in bascketball_players.items():
            print(f"{name} - рост {height} см")
    else:
        print("Список баскетболистов пуст.")

def add_player():
    name = input("Введите фамилию и имя баскетболиста для добавления: ")
    height = int(input("Введите рост, добавляемого баскетболиста, в см: "))
    bascketball_players[name] = height
    print(f"Баскетболист {name} добавлен. Его рост {height} см")

def delete_player():
    name = input("Введите фамилию и имя баскетболиста для удаления: ")
    if name in bascketball_players:
        del bascketball_players[name]
        print(f"Баскетболист {name} удален из списка.")
    else:
        print(f"Баскетболист {name} не найден в списке.")

def search_player():
    name = input("Введите фамилию и имя баскетболиста для поиска: ")
    if name in bascketball_players:
        print(f"{name} - рост {bascketball_players[name]} см")
    else:
        print(f"Баскетболист {name} не найден в списке.")

def replace_player():
    name = input("Введите фамилию и имя баскетболиста для замены информации о нем: ")
    if name in bascketball_players:
        choise = input("Какую информацию заменить (имя или рост): ")
        if choise == "имя":
            new_name = input(f"Введите обновленные фамилию и имя баскетболиста {name}: ")
            bascketball_players[new_name] = bascketball_players.pop(name)
            print(f"Информация о баскетболисте {name} обновлена. Его обновленные фамилия и имя {new_name}.")
        elif choise == "рост":    
            new_height = int(input(f"Введите обновленный рост баскетболиста {name} в см: "))
            bascketball_players[name] = new_height
            print(f"Информация о баскетболисте {name} обновлена. Его обновленный рост {new_height} см.")
        else:
            print("Неверный выбор.")
    else:
        print(f"Баскетболист {name} не найден в списке.")

def main():
    while True:
        print("Меню:")
        print("1. Список баскетболистов.")
        print("2. Добавить в список нового игрока.") 
        print("3. Удалить игрока из списка.")
        print("4. Найти информацию об игроке")
        print("5. Заменить информацию об игроке")
        print("6. Выход")
        choice = int(input("Выберите пункт меню: "))
        if choice == 1:
            list_players()
        elif choice == 2:
            add_player()
        elif choice == 3:
            delete_player()
        elif choice == 4:
            search_player()
        elif choice == 5:
            replace_player()
        elif choice == 6:
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Выберите пункт от 1 до 6.")

main()