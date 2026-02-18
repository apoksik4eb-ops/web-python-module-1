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

users_enter, users_exit, user_on_enter = {}, {}, {}

with open("access.log", "r", encoding="utf-8") as file:
   for line in file:
      date, user, action = line.strip().split(",")

      users_enter.setdefault(user, 0)
      if action == "ENTER":
         users_enter[user] = users_enter.get(user, 0) + 1

      users_exit.setdefault(user, 0)
      if action == "EXIT":
         users_exit[user] = users_exit.get(user, 0) + 1
      
      user_on_enter.setdefault(user, True)
      if action == "ENTER":
         user_on_enter.setdefault(user, True)
      elif action == "EXIT":
         user_on_enter.setdefault(user, False)
print(user_on_enter)



print(users_enter, users_exit, user_on_enter)