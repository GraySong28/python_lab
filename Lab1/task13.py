# Напишите собственную версию генератора enumerate под  названием extra_enumerate. Пример вызова:
# for i, elem, cum, frac in extra_enumerate(x):
#  print(elem, cum, frac)


def extra_enumerate(array):
    cum = 0
    summa = sum(array)
    for elem in array:
        cum += elem
        frac = round(cum / summa, 1)
        yield elem, cum, frac


array = [1, 3, 4, 2, 5]
for i in extra_enumerate(array):
    print(i)
