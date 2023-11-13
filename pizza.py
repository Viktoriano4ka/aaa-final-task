class Pizza:
    """Pizza Entity Class"""
    def __init__(self):
        self.name = ''
        self.ingredients = []
        self.icon = ''

    def dict(self) -> dict:
        """Outputs a pizza recipe"""
        pizza_dict = {
            'name': self.name,
            'icon': self.icon,
            'ingredients': self.ingredients
        }
        return pizza_dict

    def __eq__(self, other) -> bool:
        """Compares pizzas by their toppings"""
        if self.name == other.name:
            print('There are no differences between pizzas')
            return True
        else:
            print(f'Differences between two pizzas - {self.name} and {other.name}:', '\n',
                  '- the first pizza doesn\'t have the', ', '.join(set(other.ingredients) - set(self.ingredients)),
                  'ingredient from the second pizza', '\n',
                  '- but it contains the', ', '.join(set(self.ingredients) - set(other.ingredients)), 'ingredient')
            return False


class Margherita(Pizza):
    """Child of the Pizza class, Margherita Entity Class"""
    def __init__(self):
        super().__init__()
        self.name = 'Margherita'
        self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        self.icon = '🧀'
        self.size = ['L', 'XL']
        self.tariff = {'L': 400, 'XL': 500}
        self.price = int()

    def get_price(self, pizza_size: str) -> int:
        """Gets the price from the selected pizza size"""
        self.price = self.tariff[pizza_size]
        return self.price

    def choose_size(self, s: str) -> str:
        """Selects the pizza size from the list"""
        self.size = s
        self.price = Margherita().get_price(self.size)
        return self.size


class Pepperoni(Pizza):
    """Child of the Pizza class, Pepperoni Entity Class"""
    def __init__(self):
        super().__init__()
        self.name = 'Pepperoni'
        self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        self.icon = '🍕'
        self.size = ['L', 'XL']
        self.tariff = {'L': 500, 'XL': 600}
        self.price = int()

    def get_price(self, pizza_size: str) -> int:
        """Gets the price from the selected pizza size"""
        self.price = self.tariff[pizza_size]
        return self.price

    def choose_size(self, s: str) -> str:
        """Selects the pizza size from the list"""
        self.size = s
        self.price = Pepperoni().get_price(self.size)
        return self.size


class Hawaiian(Pizza):
    """Child of the Pizza class, Hawaiian Entity Class"""
    def __init__(self):
        super().__init__()
        self.name = 'Hawaiian'
        self.ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        self.icon = '🍍'
        self.size = ['L', 'XL']
        self.tariff = {'L': 500, 'XL': 600}
        self.price = int()

    def get_price(self, pizza_size: str) -> int:
        """Gets the price from the selected pizza size"""
        self.price = self.tariff[pizza_size]
        return self.price

    def choose_size(self, s: str) -> str:
        """Selects the pizza size from the list"""
        self.size = s
        self.price = Hawaiian().get_price(self.size)
        return self.size


def greet_choose() -> Margherita | Pepperoni | Hawaiian:
    print('''"Welcome to Victoria's Pizzeria
                 We hope you have already read our menu
                    What kind of pizza do you want?"''')  # Приветствие, запрос на выбор пиццы
    pizza = None
    pizza_types = {1: 'Margherita', 2: 'Pepperoni', 3: 'Hawaiian'}
    pizza_type = int()
    while pizza_type not in (1, 2, 3, 4):
        print('1. Margherita', '2. Pepperoni', '3. Hawaiian', '4. I want to compare pizzas', sep='\n')
        pizza_type = int(input())
    if pizza_type == 1:
        pizza = Margherita()
    elif pizza_type == 2:
        pizza = Pepperoni()
    elif pizza_type == 3:
        pizza = Hawaiian()
    elif pizza_type == 4:  # Блок сравнения пицц
        compare()
        while pizza_type not in (1, 2, 3):
            print('What kind of pizza do you want?')
            print('1. Margherita', '2. Pepperoni', '3. Hawaiian', sep='\n')
            pizza_type = int(input())  # Возврат к выбору пиццы
            if pizza_type == 1:
                pizza = Margherita()
            elif pizza_type == 2:
                pizza = Pepperoni()
            elif pizza_type == 3:
                pizza = Hawaiian()
    print(f'Ok, the pizza you have chosen is {pizza_types[pizza_type]}')
    return pizza


def compare() -> bool:
    pizza1 = int()
    while pizza1 not in (1, 2, 3):
        print('Choose the first pizza you want to compare')
        print('1. Margherita', '2. Pepperoni', '3. Hawaiian', sep='\n')
        pizza1 = int(input())  # Выбор первой пиццы для сравнения
    if pizza1 == 1:
        pizza1 = Margherita()
    elif pizza1 == 2:
        pizza1 = Pepperoni()
    elif pizza1 == 3:
        pizza1 = Hawaiian()
    pizza2 = int()
    while pizza2 not in (1, 2, 3):
        print('Choose the second pizza you want to compare')
        print('1. Margherita', '2. Pepperoni', '3. Hawaiian', sep='\n')
        pizza2 = int(input())  # Выбор второй пиццы для сравнения
    if pizza2 == 1:
        pizza2 = Margherita()
    elif pizza2 == 2:
        pizza2 = Pepperoni()
    elif pizza2 == 3:
        pizza2 = Hawaiian()
    return pizza1 == pizza2


def pricing(pizza: Margherita | Pepperoni | Hawaiian) -> None:
    pizza_sizes = {1: 'L', 2: 'XL'}
    print('What size of pizza do you want?', '1. L', '2. XL', sep='\n')
    size = int(input())  # Выбор размера пиццы
    while size not in (1, 2):
        print('What size of pizza do you want?', '1. L', '2. XL', sep='\n')
        size = int(input())
    print(f'Ok, the pizza size you have chosen is {pizza_sizes[size]}')
    pizza.choose_size(pizza_sizes[size])
    print(f'Price - {pizza.price}')  # Вывод цены пиццы


def final() -> None:
    answer = int()
    while answer not in (1, 2):
        print('Are we starting to cook? Our pizza makers are ready!', '1. Yes', '2. Not sure', sep='\n')
        answer = int(input())
    if answer == 1:
        print('Keep track the preparation and delivery of your order')
    elif answer == 2:
        print('We are sorry that this time you will not try the best pizza in the city')


if __name__ == '__main__':
    selected_pizza = greet_choose()
    pricing(selected_pizza)
    final()
