# Напишите генератор  frange как  аналог range() с  дробным  шагом.
# Пример вызова:
# for x in frange(1, 5, 0.1):
# print(x)
# выводит 1 1.1 1.2 1.3 1.4... 4.9


def frange(start, stop, inc):
    start -= inc
    while True:
        if start > stop and inc < 0:
            if start + inc <= stop:
                break
        else:
            if start + inc >= stop:
                break
        start += inc
        yield round(start, 2)


for i in frange(1, 5, 0.1):
    print(round(i, 2))
for i in frange(5, 1, -0.1):
    print(round(i, 2))