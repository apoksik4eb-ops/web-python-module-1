logs = [
    ("ivan", "d1", "login"),
    ("ivan", "d1", "view"),
    ("ivan", "d2", "login"),
    ("olga", "d1", "login"),
    ("petr", "d2", "error"),
    ("anna", "d1", "login"),
    ("anna", "d2", "view")
]

user_action_count = {}
user_days = {}
user_actions = {}

for name, day, action in logs:
    user_action_count[name] = user_action_count.get(name, 0) + 1

    if name not in user_actions:
        user_actions[name] = set()
    user_actions[name].add(action)
    

user_errors = []
for name, action in user_actions.items():
    if "error" in action and "login" not in action:
        user_errors.append(name)
      
print(user_action_count, user_errors, user_actions)