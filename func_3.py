def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.sort()
    print(f"{my_list[1]} + {my_list[2]} = {my_list[1]+my_list[2]}")


a = int(input("Укажите число a "))
b = int(input("Укажите число b "))
c = int(input("Укажите число c "))
my_func(a, b, c)
