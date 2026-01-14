prices = { "bread": 20, "milk": 80, "cheese": 25}
cart = {"bread": 2, "cola": 1, "milk": 3}
sum = 0
for key, value in cart.items():
    if key in prices:
        sum += prices.get(key) * value
    else: 
        print("Цена на данный товар отсутствует")
print(sum)