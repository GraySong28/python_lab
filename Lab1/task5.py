# Напишите  скрипт,  который  позволяет  ввестис  клавиатуры текст предложения и сформировать новую  строку  на
# основе  исходной,  в которой все  слова,  начинающиеся  с  большой  буквы, приведены  к верхнему регистру.
# Слова могут разделяться запятыми или пробелами. Например,  если пользователь введет строку «город Донецк,река Кальмиус»,
# результирующая  строка  должна  выглядеть  так:  «город ДОНЕЦК,река КАЛЬМИУС».


def task5(str):
    str = str.split(" ")
    for i in range(len(str)):
        if ((str[i])[0]).isupper():
            str[i] = str[i].upper()
    print(" ".join(str))


task5(input('Введите текст: '))