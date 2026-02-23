"""
ЗАДАЧА: Умный контроль доступа (бейджи)

Даны записи содержащие журнал проходов сотрудников.

Каждая строка файла имеет формат:
дата,имя,действие

Где:
- дата     — строка в формате YYYY-MM-DD
- имя      — имя человека
- действие — ENTER (вход) или EXIT (выход)

Журнал проходов:
2026-02-01,Иван,ENTER
2026-02-01,Мария,ENTER
2026-02-01,Иван,EXIT
2026-02-01,Иван,EXIT
2026-02-01,Олег,EXIT
2026-02-02,Мария,EXIT
2026-02-02,Олег,ENTER

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Записать проходы в файл access.log

2. Прочитать файл access.log и загрузить данные.

3. Для каждого человека:
   - посчитать количество входов (ENTER)
   - посчитать количество выходов (EXIT)
   - определить, находится ли человек ВНУТРИ в конце лога
     (ENTER без последующего EXIT)

4. Найти людей с ошибками доступа:
   - EXIT без предварительного ENTER
   - два ENTER подряд без EXIT
   (сохранить таких людей в множество)

5. Для каждой даты посчитать количество входов (ENTER).

6. Найти дату с максимальным количеством входов.

7. Записать подробный отчёт в файл access_report.txt.
"""
with open("access.log", "w", encoding="utf-8") as file:
   file.write("2026-02-01,Иван,ENTER\n")
   file.write("2026-02-01,Мария,ENTER\n")
   file.write("2026-02-01,Иван,EXIT\n")
   file.write("2026-02-01,Иван,EXIT\n")
   file.write("2026-02-01,Олег,EXIT\n")
   file.write("2026-02-02,Мария,EXIT\n")
   file.write("2026-02-02,Олег,ENTER")

stats, inside, daily_enters = {}, {}, {}
errors = set()

with open("access.log", "r", encoding="utf-8") as file:
   for line in file:
      date, user, action = line.strip().split(",")
      stats.setdefault(user, {"ENTER": 0, "EXIT": 0})
      inside.setdefault(user, False)
      daily_enters.setdefault(date, 0)

      if action == "ENTER":
         if inside[user]:
            errors.add(user)
         inside[user] = True
         stats[user]["ENTER"] += 1
         daily_enters[date] += 1
      else:
         if not inside[user]:
            errors.add(user)
         inside[user] = False
         stats[user]["EXIT"] += 1

      max_day = None
      max_enters = 0
      for date, count in daily_enters.items():
         if count > max_enters:
            max_day = date
            max_enters = count

with open("access_report.txt", "w", encoding="utf-8") as file:
   for user, status in stats.items():
      for action, count in status.items():
         file.write(f"{action}: Сотрудник {user} - {count} раз.\n")
   file.write("\n")
   for user, status in inside.items():
      if status == True:
         file.write(f"Сотрудник {user} находится внутри здания.\n")
   file.write("\n")
   for user in errors:
      file.write(f"Сотрудник {user} имеет ошибку доступа.\n")
   file.write("\n")
   for date, count in daily_enters.items():
      file.write(f"Количество входов {date} - {count} раз.\n")
   file.write("\n")
   file.write(f"{max_day} было максимальное количество входов - {max_enters} раз\n")

#       users_enter.setdefault(user, 0)
#       if action == "ENTER":
#          users_enter[user] = users_enter.get(user, 0) + 1

#       users_exit.setdefault(user, 0)
#       if action == "EXIT":
#          users_exit[user] = users_exit.get(user, 0) + 1
      
#       user_on_enter.setdefault(user, True)
#       if action == "ENTER":
#          user_on_enter.setdefault(user, True)
#       elif action == "EXIT":
#          user_on_enter.setdefault(user, False)
# print(user_on_enter)

# print(users_enter, users_exit, user_on_enter)