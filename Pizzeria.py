class Pizza:    def __init__(self, name: str, dough: str, sauce: str, toppings: str, price: str) -> None:
        self.name = name        self.dough = dough
        self.sauce = sauce        self.toppings = toppings
        self.prie = price
    def __str__(self):        return f"PepperoniPizza( name={self.name}, dough={self.dough}, sauce={self.sauce}, toppings={self.toppings}"
    def prepare(self) -> None:    
        print(            f"Пдготовка {self.name} c тестом {self.dough}, соусом {self.sauce} и начинкой {self.toppings}"
        )         
    def bake(self) -> None:        print(
            f"Выпекаем {self.name}"        )
    def cut(self) -> None:
        print(            f"C нарезками {self.dough}, {self.toppings}"
        )        
    def box(self) -> None:               print(
            f"Упаковка {self.name}"        )
class PepperoniPizza(Pizza):
    def __init__(self, name, dough, sauce, toppings, price) -> None:        super().__init__(name, dough, sauce, toppings, price)
    def __str__(self):
        return f"PepperoniPizza( name={self.name}, dough={self.dough}, sauce={self.sauce}, toppings={self.toppings}"
    def prepare(self) -> None:               print(super().bake())
    def bake(self) -> None:
        print(super().cut())
    def cut(self) -> None:        print(super().box())
    def box(self) -> None:  
        print(super().prepare())
class BBQPizza(Pizza):    def __init__(self, name, dough, sauce, toppings, price) -> None:
        super().__init__(name, dough, sauce, toppings, price)
    def __str__(self):        return f"PepperoniPizza( name={self.name}, dough={self.dough}, sauce={self.sauce}, toppings={self.toppings}"
    def prepare(self) -> None:       
        print(super().bake())
    def bake(self) -> None:        print(super().cut())

    def cut(self) -> None:        print(super().box())
    def box(self) -> None:  
        print(super().prepare())  
    def add_topping(self, topping: str) -> None:        choice = input(f"Хотите добавить ингредиент {topping}? (да/нет)")
        if choice.lower() == "нет"            return
        if choice.lower() == "да"            if topping in self.toppings:
                print(f"Ингредиент {topping} уже есть в {self.name}        self.topping.append(topping)
        return        
class SeafoodPizza(Pizza):    def __init__(self, name, dough, sauce, toppings, price) -> None:
        super().__init__(name, dough, sauce, toppings, price)
    def __str__(self):        return f"PepperoniPizza( name={self.name}, dough={self.dough}, sauce={self.sauce}, toppings={self.toppings}"
    def prepare(self) -> None:       
        print(super().bake())
    def bake(self) -> None:        print(super().cut())
    def cut(self) -> None:
        print(super().box())        
    def box(self) -> None:               print(super().prepare())
class Order:
    def __init__(self) -> None:        self.pizzas: list[Pizza] = []
    def add_pizza(self, pizza: Pizza) -> None:
        self.add_pizzas.append(pizza)
    def calculate_total(self) -> int:        return sum(pizza.price for pizza in self.pizzas)
class Terminal:
        def __init__(self) -> None:
        self.menu: dict[int, Pizza]= {            1: PepperoniPizza,
            2: SeafoodPizza,            3: BBQPizza
        }        self.order: Order | None = None
    def display_menu(self):
        print("Меню:", "=" * 80, sep="\n")    for key, pizza in self.menu.items():
        print(f"{key}. {pizza.name} - {pizza.price} тенге" )
    def take_order(self) -> None:
        self.order = Order()        while True:
            self.display_menu()            choice = input(
                "=" * 80                + "\nВведите номер пиццы, которую хотите добавить в заказ (0 для завершения)"
                + "=" * 80                + "\n"
            )            if choice == "0":
                break            if choice == "2":
                topping = self.menu[int(choice)].ask_topping()                self.menu[int(choice)].add_topping(topping)
            if int(choice) in self.menu:
self.order.add_pizza(self.menu[int(choice)])
                print(f"{self.menu[int(choice)].name} добавлена в ваш заказ.")            else:
                print("Не верный набор. Поалуйста, выберите пиццу из меню")                continue
    def confirm_order(self) -> bool:
        if self.order:            print(f"Итого к оплате: {self.order.calculate_total()} тенге.")
            confirmation = input("Вы хотите подтвердить ваш заказ? (да.нет): ")            if confirmation.lower() == "да":
                print("Заказ подтвержден.")                return True
            else:                print("Заказ отменен.")
                self.order = None                return False
        else:            print("Нет заказа для подтверждения.")
            return False        
    def take_payment(self) -> None:        if self.order:
            print("Оплата принята. Ваш заказ готовиться.")            for pizza in self.order.pizzas:
                pizza.prepare()                pizza.bake()
                pizza.cut()                pizza.box()
            print("Спасибо за ваш заказ!")
if name == "__main__":
    terminal  =Terminal()    terminal.take_order()
    if terminal.confirm_order():        terminal.take_payment()

    Pepperoni = PepperoniPizza("Пепперони", "тонкое тесто", "сырный соус", "колбаса", "3500 тенге")
    BBQ = BBQPizza("Барбекю", "толстое тесто", "томатный соус", "колбаса", "2500 тенге")
    Seafood = SeafoodPizza("Дары моря", "тонкое тесто", "сырный соус", "колбаса", "4500 тенге")