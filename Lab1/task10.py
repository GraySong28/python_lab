# Напишите  скрипт,  позволяющий  определить  надежность  вводимого пользователем  пароля.Это  задание  является
# творческим: алгоритм определениянадежности разработайте самостоятельно.


def task10(password):
    password_strength = 0
    symbols = ['~', '`', '!', '&', '%', '^', '&', '*', '[', ']', '<', '>', '_']
    for i in password:
        if i.isdigit():
            password_strength += 1
            break
    for i in password:
        if i.isalpha():
            password_strength += 1
            break
    for i in password:
        for j in symbols:
            if i == j:
                password_strength += 1
                break
        break
    for i in password:
        if i.islower():
            password_strength += 1
            break
    for i in password:
        if i.isupper():
            password_strength += 1
            break
    if len(password) > 12:
        password_strength += 1
    if password_strength > 4 and password_strength <= 6: print('Пароль - надёжный')
    if password_strength > 2 and password_strength <= 4: print('Пароль - средней надёжности')
    if password_strength <= 2: print('Пароль - слабый')
    print(password_strength)


task10(input('Введите пароль: '))