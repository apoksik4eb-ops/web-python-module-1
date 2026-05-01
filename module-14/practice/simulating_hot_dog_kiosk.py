from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float

@dataclass
class HotDogRecipe:
    name: str
    ingredient_keys: list[str]

class RecipeFactory:
    def get_standart_recipes() -> dict[int, HotDogRecipe]:
        return {
            1: HotDogRecipe("Хот-дог-1 (майонез, горчица, кетчуп)", ["bun", "sausage", "mayonnaise", "mustard", "ketchup"]),
            2: HotDogRecipe("Хот-дог-2 (только с горчицей)", ["bun", "sausage", "mustard"]),
            3: HotDogRecipe("Хот-дог-3 (только с кетчупом)", ["bun", "sausage", "ketchup"]),
        }

class HotDogBuilder:
    def __init__(self):
        self._ingredient = ["bun", "sausage"]

    def add_ingredient(self, key: str):
        if key not in self._ingredient:
            self._ingredient.append(key)
        return self

    def build(self):
        return HotDogRecipe("Свой хот-дог: ", self._ingredient)
    
# -----------------------------------------------

@dataclass
class OrderItem:
    recipe: HotDogRecipe
    quantity: int

    def total_price(self, ingredients: dict[str, Ingredient]) -> float:
        one_hotdog_price = sum(ingredients[key].price for key in self.recipe.ingredient_keys)

        return one_hotdog_price * self.quantity

    def total_cost(self, ingredients: dict[str, Ingredient]) -> float:
        one_hotdog_cost = sum(ingredients[key].cost for key in self.recipe.ingredient_keys)

        return one_hotdog_cost * self.quantity

@dataclass
class Order:
    items: list[OrderItem]
    payment_type: str

    def total_price(self, ingredients: dict[str, Ingredient]):
        return sum(item.total_price(ingredients) for item in self.items)

    def total_cost(self, ingredients: dict[str, Ingredient]):
        return sum(item.total_cost(ingredients) for item in self.items)

    def total_profit(self, ingredients: dict[str, Ingredient]):
        return self.total_price(ingredients) - self.total_cost(ingredients)
    
    def total_quantity(self) -> int:
        return sum(item.quantity for item in self.items)
    
    def discount_rate(self) -> float:
        if self.total_quantity() >= 7:
            return 0.15
        elif self.total_quantity() >= 5:
            return 0.10
        elif self.total_quantity() >= 3:
            return 0.05
        return 0.0
    
    def total_price_with_discount(self, ingredients: dict[str, Ingredient]) -> float:
        total = self.total_price(ingredients)
        discount = total * self.discount_rate()
        return total - discount

    def to_text(self, ingredients: dict[str, Ingredient]) -> str:
        lines = ["Информация о заказе:"]

        for item in self.items:
            ingredients_names = [ingredients[key].name for key in item.recipe.ingredient_keys]
        
            lines.append(f"Наименование: {item.recipe.name}")
            lines.append(f"Количество: {item.quantity} шт.")
            lines.append("Состав:")

            for name in ingredients_names:
                lines.append(f"- {name}")

        discount_value = self.total_price(ingredients) * self.discount_rate()
        final_total = self.total_price(ingredients) - discount_value

        lines.append(f"Сумма без скидки: {self.total_price(ingredients)} руб.")

        if self.discount_rate() > 0:
            lines.append(f"Скидка: {int(self.discount_rate() * 100)}% (-{discount_value} руб.)")

        lines.append(f"Итого к оплате: {final_total} руб.")

        lines.append(f"Способ оплаты: {self.payment_type}")

        return "\n".join(lines)

# -----------------------------------------------

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Оплата наличными выполнена на сумму {amount} руб."

class CardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Оплата картой выполнена на сумму {amount} руб."

# -----------------------------------------------

class FileOrderSaver:
    def __init__(self, filename: str = "order.txt"):
        self.filename = filename

    def save(self, order: Order, ingredients: dict[str, Ingredient]):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(order.to_text(ingredients))
            file.write("\n" + "-" * 50 + "\n")

def create_ingredients():
    return {
        "bun": Ingredient("Булочка", "bun", 40, 10),
        "sausage": Ingredient("Сосиска", "sausage", 100, 30),
        "mayonnaise": Ingredient("Майонез","mayonnaise", 50, 20),
        "mustard": Ingredient("Горчица", "mustard", 30, 10),
        "ketchup": Ingredient("Кетчуп", "ketchup", 40, 15),
        "onion": Ingredient("Лук", "onion", 50, 20),
        "jalapeno": Ingredient("Халапеньо", "jalapeno", 70, 30)
    }

def create_stock() -> dict[str, int]:
    return {
        "bun": 10,
        "sausage": 10,
        "mayonnaise": 10,
        "mustard": 10,
        "ketchup": 10,
        "onion": 10,
        "jalapeno": 10
    }

def get_topping() -> list[str]:
    return [
        "mayonnaise",
        "mustard",
        "ketchup",
        "onion",
        "jalapeno"
    ]

def create_custom_recipe(inventory: Inventory) -> HotDogRecipe:
    builder = HotDogBuilder()

    print("Создание своего хот-дога: ")
    for key in get_topping():
        ingredient = inventory.ingredients[key]

        choice = input(f"Хотите добавить {ingredient.name}? ") # да/нет
        if choice == "да":
            builder.add_ingredient(ingredient.key)
    
    return builder.build()

# -----------------------------------------------

class Inventory:
    def __init__(self, ingredients: dict[str, Ingredient], stock: dict[str, int]):
        self.ingredients = ingredients
        self.stock = stock

    def has_enough(self, ingredients_keys: list[str], quantity: int) -> bool:
        for key in ingredients_keys:
            if self.stock.get(key, 0) < quantity:
                return False
        return True
    
    def reduce_stock(self, ingredients_keys: list[str], quantity: int):
        for key in ingredients_keys:
            self.stock[key] -= quantity

    def show(self):
        print("Наличие ингредиентов:")

        for key, count in self.stock.items():
            ingredient = self.ingredients[key]
            print(f"{ingredient.name}: {count}")
    
    def get_missing_ingredients(self, ingredients_keys: list[str], quantity: int) -> dict[str, int]:
        missing = {}

        for key in ingredients_keys:
            available = self.stock.get(key, 0)
            required = quantity

            if available < required:
                missing[key] = required - available

        return missing
    
    def print_missing(self, missing: dict[str, int]):
        print("Недостаточно ингредиентов!")

        for key, count in missing.items():
            ingredient = self.ingredients[key]
            print(f"Нужно докупить: {ingredient.name} — {count} шт.")

class SalesReport:
    def __init__(self):
        self.profit = 0
        self.revenue = 0
        self.sold_count = 0

    def add_order(self, order: Order, ingredients: dict[str, Ingredient]):
        self.sold_count += sum(item.quantity for item in order.items)
        self.revenue += order.total_price(ingredients)
        self.profit += order.total_profit(ingredients)

    def show(self):
        print("Отчет")
        print(f"Продано хот-догов: {self.sold_count} шт.")
        print(f"Выручка: {self.revenue} руб.")
        print(f"Доход: {self.profit} руб.")

def show_menu():
    print("1. Создать заказ.")
    print("2. Отчет.")
    print("3. Наличие ингредиентов.")
    print("4. Выход.")

def show_standart_recipes(recipes: dict[int, HotDogRecipe], ingredients: dict[str, Ingredient]):
    print("Стандартные хот-доги:")

    for number, recipe in recipes.items():
        print(f"{number}. {recipe.name}")

        price = sum(ingredients[key].price for key in recipe.ingredient_keys)
        print(f"Цена за штуку: {price} руб.")

    print("0. Создание своего хот-дога")

def choice_recipes(recipes: dict[int, HotDogRecipe], ingredients: dict[str, Ingredient], inventory: Inventory):
    while True:
        choice = int(input("Выберите вариант: "))
        if choice == 0:
            return create_custom_recipe(inventory)
        if choice not in recipes:
            print("Такого варианта нет!")
            continue
        return recipes[int(choice)]
        
def choose_payment():
    print("Выберите способ оплаты:")
    print("1 - Наличные")
    print("2 - Карта")

    while True:
        choice = input("Выберите: ")

        if choice == "1":
            return CashPayment(), "Наличные"
        elif choice == "2":
            return CardPayment(), "Карта"
        
        print("Выберите мужду 1 и 2 вариантом")

def create_order(ingredients: dict[str, Ingredient], inventory: Inventory, report: SalesReport, file_saver: FileOrderSaver):
    recipes = RecipeFactory.get_standart_recipes()
    items: list[OrderItem] = []

    while True:
        show_standart_recipes(recipes, ingredients)

        recipe = choice_recipes(recipes, ingredients, inventory)
        quantity = int(input("Введите количество: "))

        missing = inventory.get_missing_ingredients(recipe.ingredient_keys, quantity)

        if missing:
            print("Недостаточно ингредиентов!")

            for key, count in missing.items():
                name = ingredients[key].name
                print(f"Нужно докупить: {name} — {count} шт.")

            return
        
        items.append(OrderItem(recipe, quantity))

        more = input("Добавить еще один вид хот-дога? ")

        if more == "нет":
            break

    payment_strategy, payment_type = choose_payment()

    order = Order(items, payment_type)

    for item in items:
        inventory.reduce_stock(item.recipe.ingredient_keys, item.quantity)

    # Сумма заказа
    amount = order.total_price_with_discount(ingredients)

    # Оплата
    print(payment_strategy.pay(amount))

    # Сохранение заказа в файл
    file_saver.save(order, ingredients)

    # Добавление заказа в отчет
    report.add_order(order, ingredients)

def main():
    ingredients = create_ingredients()
    stock = create_stock()

    inventory = Inventory(ingredients, stock)
    report = SalesReport()
    file_saver = FileOrderSaver()

    while True:
        show_menu()

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            create_order(ingredients, inventory, report, file_saver)
        elif choice == "2":
            report.show()
        elif choice == "3":
            inventory.show()
        elif choice == "4":
            break

main()