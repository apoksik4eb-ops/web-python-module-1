import random
tasks = []

for i in range(10):
    tasks.append({
        "id": f"t_{i}",
        "assignee": random.choice(["ivan", "olga", "petr", "anna", "oleg"]),
        "status": random.choice(["in_progress", "blocked", "in_review", "waiting_vendor"]),
        "days_in_status": random.randint(0, 10)
    })

days_work = set()
for task in tasks:
    if task["status"] == "in_progress" and task["days_in_status"] > 7:
        days_work.add(task["assignee"])

status_assignees = {}
for task in tasks:
    if task["status"] not in status_assignees:
        status_assignees[task["status"]] = set()

    status_assignees[task["status"]].add(task["assignee"])

result = {}
for status in status_assignees:
    if len(status_assignees[status]) == 1:
        result[status] = list(status_assignees[status])[0]

print(tasks)
print(days_work)
print(status_assignees)
print(result)