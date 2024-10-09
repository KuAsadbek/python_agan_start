def greet():
    print("Hello, world!")
greet()  # Вывод: Hello, world!

def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # Вывод: Hello, Alice!

def add(a, b):
    return a + b
result = add(3, 5)
print(result)  # Вывод: 8

def greet(name="stranger"):
    print(f"Hello, {name}!")
greet()          # Вывод: Hello, stranger!
greet("Alice")   # Вывод: Hello, Alice!

def multiply(a, b):
    return a * b
result = multiply(4, 5)
print(result)  # Вывод: 20

def no_return():
    print("This function returns nothing")

result = no_return()  # Вывод: This function returns nothing
print(result)  # None

def greet(name):
    """Эта функция приветствует человека по имени."""
    print(f"Hello, {name}!")
print(greet.__doc__)  # Вывод: Эта функция приветствует человека по имени.

def my_function(*args):
    for arg in args:
        print(arg)
my_function(1, 2, 3)  # Вывод: 1 \n 2 \n 3

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
my_function(name="Alice", age=25)  # Вывод: name = Alice \n age = 25

def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from nested function")  # Вывод: Hello from nested function

multiply = lambda a, b: a * b
print(multiply(2, 3))  # Вывод: 6

def is_even(number):
    """Проверяет, является ли число четным."""
    return number % 2 == 0
print(is_even(4))  # True
print(is_even(7))  # False