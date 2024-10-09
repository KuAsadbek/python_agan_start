
fruits = ["яблоко", "банан", "вишня"]
print(len(fruits))  # 3

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15

num = -10
print(abs(num))  # 10

numbers = [5, 2, 9, 1]
print(sorted(numbers))  # [1, 2, 5, 9]

letters = ['a', 'b', 'c']
print(list(reversed(letters)))  # ['c', 'b', 'a']


numbers = [True, True, True]
print(all(numbers))  # True

numbers = [False, True, False]
print(any(numbers))  # True

names = ["Asadbek", "John"]
ages = [20, 25]

result = zip(names, ages)
print(list(result))  # [('Asadbek', 20), ('John', 25)]

numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4]

print(pow(2, 3))  # 8

number = 3.14159
print(round(number, 2))  # 3.14

print(divmod(10, 3))  # (3, 1)

print(type(5))  # <class 'int'>
print(type([1, 2, 3]))  # <class 'list'>

print(isinstance(5, int))  # True
print(isinstance(5.5, int))  # False

a = 5
print(id(a))  # Выведет уникальный идентификатор переменной a

expression = "2 + 3"
print(eval(expression))  # 5


numbers = [1, 2, 3, 4, 5]
print(max(numbers))  # 5
print(min(numbers))  # 1

help(print)  # Выведет справочную информацию по функции print
