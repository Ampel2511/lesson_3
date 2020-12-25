def my_func(num_1, num_2):
    print(f"{num_1**num_2}")


def power():
    x = input("Укажите действительное положительное число x ")
    y = input("Укажите целое отрицательное число y ")
    try:
        while int(x) < 0 or int(y) > 0:
            print("Неавильно указаны числа")
            x = int(input("Укажите действительное положительное число x "))
            y = int(input("Укажите целое отрицательное число y "))
        my_func(int(x), int(y))
    except:
        print("Ошибка")


power()
