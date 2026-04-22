payments = [
    ("ivan", 100),
    ("ivan", -30),
    ("ivan", -20),
    ("olga", 200),
    ("petr", -50),
]

total_balance = {}
count_operation = {}

for user, amount in payments:
    if user not in total_balance:
        total_balance[user] = 0
    total_balance[user] += amount

    if user in count_operation:
        count_operation[user] += 1
    else:
        count_operation[user] = 1
 
for key, value in total_balance.items():
    print(f"Суммарный баланс пользователя {key} = {value} рублей.")
    if value < 0:
        print(f"У пользователя {key} отрицательный баланс, равный {value} рублей.")

for key, value in count_operation.items():
    if value > 2:
        print(f"У пользователя {key} более 2х операций, их количество = {value}.")

