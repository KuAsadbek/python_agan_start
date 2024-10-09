i = 1
while i < 5:
    print(i)
    i += 1  # увеличиваем значение i на 1

i = 1
while i < 10:
    print(i)
    if i == 5:
        break  # цикл завершится, когда i станет равно 5
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # пропускаем шаг, если i равно 3
    print(i)

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("Цикл завершен")

i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("Цикл завершен")

i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1

i = 1
while i < 5:
    print(i)  # бесконечный цикл, так как i всегда будет меньше 5


while True:
    print("Этот цикл будет выполняться бесконечно")

