
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

text = "hello"
for char in text:
    print(char)

for i in range(5):  # создаст числа от 0 до 4
    print(i)

for i in range(2, 10, 2):  # от 2 до 9 с шагом 2
    print(i)

person = {'name': 'Alice', 'age': 25}
for key, value in person.items():
    print(key, ":", value)

for i in range(5):
    if i == 3:
        break  # завершает цикл, если i равно 3
    print(i)

for i in range(5):
    if i == 3:
        continue  # пропускает итерацию, если i равно 3
    print(i)

for i in range(3):
    for j in range(2):
        print(i, j)

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Цикл завершен без прерываний")

for i in range(5):
    print(i)
else:
    print("Цикл завершен")
