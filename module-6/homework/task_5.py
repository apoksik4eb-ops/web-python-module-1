logs = [
    ("ivan", 8),
    ("ivan", 10),
    ("olga", 20),
    ("petr", 45),
]
all_hours = {}

for log in logs:
    employee = log[0]
    hours = log[1]
    if employee not in all_hours:
        all_hours[employee] = 0
    all_hours[employee] += hours

for key, value in all_hours.items():
    print(f"Суммарно работник {key} отработал {value} часов")

for key, value in all_hours.items():    
    if value > 40:
        recycling_hours = value - 40
        print(f"Работник {key} переработал {recycling_hours} часов")
    elif value < 20:
        unfinished_hours = 20 - value
        print(f"Работник {key} недоработал {unfinished_hours} часов")