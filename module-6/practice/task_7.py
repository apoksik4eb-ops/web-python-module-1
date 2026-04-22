logs = [
    ("ivan", "day", 8),
    ("ivan", "night", 4),
    ("olga", "day", 6),
    ("petr", "night", 3),
    ("anna", "day", 4),
    ("anna", "day", 3)
]

diff_change = {}
shift_hours = {}
employee_hours = {}

for log in logs:
    name = log[0]
    shift = log[1]
    hours = log[2]
    if name not in diff_change:
        diff_change[name] = set()
    diff_change[name].add(shift)

    if shift not in shift_hours:
        shift_hours[shift] = 0
    shift_hours[shift] += hours

    if name not in employee_hours:
        employee_hours[name] = 0
    employee_hours[name] += hours

    
for work in diff_change:
    value = diff_change[work]
    if len(value) > 1:
        print(work)

for time in shift_hours:
    result_time = shift_hours[time]
    if result_time < 8:
        print(f"На смене {time} суммарно отработали {result_time} часов")

employees = []
for employee in employee_hours:
    if employee_hours[employee] >= 12:
        employees.append(employee)
print(employees)
