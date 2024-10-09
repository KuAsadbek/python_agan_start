
my_list = [1, 2, 3, 4]

mixed_list = [1, "hello", 3.14, True]

my_list = [10, 20, 30, 40]
print(my_list[0])  # 10
print(my_list[2])  # 30

print(my_list[-1])  # последний элемент (40)
print(my_list[-2])  # предпоследний элемент (30)

my_list[1] = 25
print(my_list)  # [10, 25, 30, 40]

my_list.append(50)
print(my_list)  # [10, 25, 30, 40, 50]

my_list.insert(1, 15)  # добавляет 15 на позицию с индексом 1
print(my_list)  # [10, 15, 25, 30, 40, 50]

my_list.extend([60, 70]) #добавляет элементы другого списка или итерируемого объекта в конец текущего списка.
print(my_list)  # [10, 15, 25, 30, 40, 50, 60, 70]

my_list.remove(25)
print(my_list)  # [10, 15, 30, 40, 50, 60, 70]

my_list.pop(2)  # удаляет элемент с индексом 2 (30)
print(my_list)  # [10, 15, 40, 50, 60, 70]

my_list.clear()
print(my_list)  # []

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # 5

if 3 in my_list:
    print("3 есть в списке")

for element in my_list:
    print(element)

sub_list = my_list[1:4]  # элементы с 1 по 3 индексы (не включая 4)
print(sub_list)  # [2, 3, 4]

sub_list = my_list[::2]  # каждый второй элемент списка
print(sub_list)  # [1, 3, 5]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # [1, 2, 3, 4, 5, 6]

repeated_list = list1 * 2
print(repeated_list)  # [1, 2, 3, 1, 2, 3]

print(my_list.index(3))  # 2
print(my_list.count(3))  # 1

my_list.reverse()
print(my_list)  # [5, 4, 3, 2, 1]

my_list.sort()
print(my_list)  # [1, 2, 3, 4, 5]

nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1])  # [3, 4]
print(nested_list[1][0])  # 3
