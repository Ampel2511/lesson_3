def info(name, surname, phone, email, date_of_birth, city):
    print(name, surname, date_of_birth, city, phone, email)


a = input("Укажите ваше имя: ")
b = input("Укажите вашу фамилию: ")
c = input("Укажите вашу дату рождения: ")
d = input("Укажите ваш город проживания: ")
e = input("Укажите ваш телефон: ")
f = input("Укажите ваш email: ")
info(name=a, surname=b, date_of_birth=c, city=d, phone=e, email=f)
