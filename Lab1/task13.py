# Напишите собственную версию генератора enumerate под  названием extra_enumerate. Пример вызова:
# for i, elem, cum, fracin extra_enumerate(x):
#  print(elem, cum, frac)


def extra_enumerate(array):
    i = 0
    cum = 0
    for elem in array:
        yield i, elem
        i += 1
        cum = cum + elem
        print("(", elem, ',', cum, ',', cum * 0.1, ")")


array = [1, 3, 4, 2]
for i in extra_enumerate(array):
    print()
