
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

my_dict = dict(name="Alice", age=25, city="New York")

print(my_dict["name"])  # Alice
print(my_dict["age"])   # 25

print(my_dict["country"])  # KeyError: 'country'

print(my_dict.get("country"))  # None
print(my_dict.get("country", "Not Found"))  # Not Found

my_dict["country"] = "USA"  # добавление
my_dict["age"] = 30  # изменение
print(my_dict)

age = my_dict.pop("age")# удаляет элемент по ключу и возвращает его значение.
print(age)  # 30
print(my_dict)  # {'name': 'Alice', 'city': 'New York', 'country': 'USA'}

del my_dict["city"]
print(my_dict)  # {'name': 'Alice', 'country': 'USA'}

my_dict.clear()
print(my_dict)  # {}

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, ":", value)

dict1 = {"name": "Alice", "age": 25}
dict2 = {"age": 30, "city": "New York"}
dict1.update(dict2)
print(dict1)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

if "name" in my_dict:
    print("Ключ 'name' существует")

keys = my_dict.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])

values = my_dict.values()
print(values)  # dict_values(['Alice', 30, 'New York'])

items = my_dict.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nested_dict["person1"]["name"])  # Alice

students = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "Los Angeles"}
}

for student, info in students.items():
    print(f"{student} живет в {info['city']} и ему {info['age']} лет.")
