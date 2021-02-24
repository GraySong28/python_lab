# Напишите собственную версию генератора enumerate под названием extra_enumerate. Примервызова:
# for i, elem, cum, fracin extra_enumerate(x):
# print(elem, cum, frac)


def extra_enumerate(array, start):
    start_1 = start
    cum = 0
    for elem in array:
        yield start_1, elem
        start_1 += 1
        cum = cum + elem
        print("(", elem, ',', cum, ',', cum * 0.1, ")")


x = [1, 3, 4, 2]
for i in extra_enumerate(x, 0):
    print()