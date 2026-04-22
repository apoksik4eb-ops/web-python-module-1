purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"], "price": 120, "timestamp": 1},
    {"user": "Боб", "items": ["банан"], "price": 50, "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"], "price": 150, "timestamp": 5},
    {"user": "Боб", "items": ["яблоко", "апельсин"], "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"], "price": 70, "timestamp": 15},
    {"user": "Боб", "items": ["банан"], "price": 40, "timestamp": 25},
]

count_items = {}
total_price = {}
unique_fruit = {}
count_fruit= {}
count_unique_fruit = {}
max_item_fruit = {}
max_user_price = {}
max_count_fruit_user = {}

for purchase in purchases:
    user = purchase["user"]
    items = purchase["items"]
    price = purchase["price"]
    timestamp = ["timestamp"]

    count_items[user] = count_items.get(user, 0) + 1
    
    if user not in total_price:
        total_price[user] = 0 
    total_price[user] += price

    unique_fruit.setdefault(user, set()).update(items)

    for item in items:
        count_fruit[user] = count_fruit.get(user, 0) + 1

        count_unique_fruit[item] = count_unique_fruit.get(item, 0) + 1
   
max_fruit = None
max_count = 0
for fruit, count in count_unique_fruit.items():
    if count > max_count:
        max_fruit = fruit
        max_count = count
max_item_fruit[max_fruit] = max_count

max_user = None
max_price = 0
for user, price in total_price.items():
    if price > max_price:
        max_user = user
        max_price = price
max_user_price[max_user] = max_price

max_count_user = None
max_count_fruit = 0
for user, count in count_fruit.items():
    if count > max_count_fruit:
        max_count_user = user
        max_count_fruit = count
max_count_fruit_user[max_count_user] = max_count_fruit

print("----------------------------------------------------------------")                
for key, value in count_items.items():
    print(f"{key} совершил {value} покупки.")
print("----------------------------------------------------------------")
for key, value in total_price.items():
    print(f"{key} потратил {value} рублей.")
print("----------------------------------------------------------------")
for key, value in unique_fruit.items():
    print(f"Уникальные покупки у {key}: {value}.")
print("----------------------------------------------------------------")
for key, value in count_fruit.items():
    print(f"{key} купил {value} фруктов.")
print("----------------------------------------------------------------")
for key, value in max_item_fruit.items():
    print(f"Чаще всего покупали {key}, его покупали {value} раз.")
print("----------------------------------------------------------------")
for key, value in max_user_price.items():
    print(f"{key} потратил больше денег, сумма покупок составила {value} рублей.")
print("----------------------------------------------------------------")
for key, value in max_count_fruit_user.items():
    print(f"{key} купил больше фруктов, их количество составило {value} штук.")
print("----------------------------------------------------------------")
