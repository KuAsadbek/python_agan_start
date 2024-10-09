# Создание кортежа с использованием круглых скобок
my_tuple = (1, 2, 3)

# Создание кортежа без круглых скобок (с помощью запятых)
my_tuple = 1, 2, 3

# Создание кортежа с разными типами данных
mixed_tuple = (1, "Hello", 3.14, True)

# Создание пустого кортежа
empty_tuple = ()

single_element_tuple = (1,)  # Это кортеж
not_a_tuple = (1)             # Это просто число

my_tuple = (10, 20, 30, 40)

print(my_tuple[0])  # Вывод: 10
print(my_tuple[2])  # Вывод: 30

print(my_tuple[-1])  # Вывод: 40
print(my_tuple[-2])  # Вывод: 30

my_tuple = (10, 20, 30, 40, 50)

print(my_tuple[1:4])  # Вывод: (20, 30, 40)
print(my_tuple[:3])    # Вывод: (10, 20, 30)
print(my_tuple[2:])    # Вывод: (30, 40, 50)

my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)  # Создание нового кортежа
print(new_tuple)  # Вывод: (1, 2, 3, 4, 5)

tuple1 = (1, 2, 3)
tuple2 = (4, 5)

# Конкатенация
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Вывод: (1, 2, 3, 4, 5)

# Повторение
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Вывод: (1, 2, 3, 1, 2, 3)

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1])      # Вывод: (3, 4)
print(nested_tuple[1][0])   # Вывод: 3

my_list = list(my_tuple)  # Преобразование кортежа в список
my_tuple_from_list = tuple(my_list)  # Преобразование списка в кортеж

my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))  # Вывод: 3

print(my_tuple.index(2))  # Вывод: 1


def get_coordinates():
    return (10, 20)  # Возвращаем кортеж с координатами

x, y = get_coordinates()  # Распаковка кортежа
print(f"X: {x}, Y: {y}")  # Вывод: X: 10, Y: 20
