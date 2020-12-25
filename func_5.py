def sum_numbers(my_list: list, summ):
    for number in my_list:
        if number == "q":
            print(summ)
            exit()
        summ += int(number)
    return summ


summ = 0
while True:
    print("Чтобы выйти из программы введите q")
    numbers = input("Введите строку из чисел ")
    summ = sum_numbers(my_list=numbers.split(), summ=summ)
    print(summ)
