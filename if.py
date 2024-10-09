
x = 5
if x > 3:
    print("x больше 3")

x = 2
if x > 3:
    print("x больше 3")
else:
    print("x меньше или равно 3")

x = 5
if x > 10:
    print("x больше 10")
elif x > 3:
    print("x больше 3, но меньше или равно 10")
else:
    print("x меньше или равно 3")

x = 10
if x > 5:
    if x < 20:
        print("x между 5 и 20")

print("x больше 3") if x > 3 else print("x меньше или равно 3")
