def func(a, b):
    print(f"a/b = {a/b}")
    print(f"b/a = {b/a}")


a = int(input("Укажите число a "))
b = int(input("Укажите число b "))
while a == 0 or b == 0:
    print("Нельзя указать 0, введите заново")
    a = int(input("Укажите число a "))
    b = int(input("Укажите число b "))
func(a, b)
