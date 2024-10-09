class Car:
    """Класс для представления автомобиля"""
    
    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """Вывод информации об автомобиле"""
        print(f"{self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Вывод: 2020 Toyota Corolla

my_car.color = "red"  # добавление нового атрибута
print(my_car.color)    # Вывод: red

class Car:
    # предыдущий код...
    
    def start_engine(self):
        print(f"{self.make} {self.model} engine started.")

my_car.start_engine()  # Вывод: Toyota Corolla engine started.

class ElectricCar(Car):
    """Класс для представления электрического автомобиля"""
    
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)  # вызов конструктора родительского класса
        self.battery_size = battery_size
    
    def display_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_electric_car = ElectricCar("Tesla", "Model S", 2022)
my_electric_car.display_info()      # Вывод: 2022 Tesla Model S
my_electric_car.display_battery()   # Вывод: This car has a 75-kWh battery.

class Car:
    wheels = 4  # поле класса
print(Car.wheels)  # Вывод: 4

class Person:
    """Класс для представления человека"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.greet()  # Вывод: Hello, my name is Alice and I am 30 years old.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Вывод: Woof!
animal_sound(cat)  # Вывод: Meow!

class Example:
    def __init__(self):
        self._protected = "protected"
        self.__private = "private"
    
    def get_private(self):
        return self.__private

example = Example()
print(example._protected)  # Вывод: protected
# print(example.__private)  # Ошибка: AttributeError
print(example.get_private())  # Вывод: private
