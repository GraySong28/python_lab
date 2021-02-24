# Напишите генератор  frange как  аналог range() с  дробным  шагом.
# Пример вызова:
# for x in frange(1, 5, 0.1):
# print(x)
# выводит 1 1.1 1.2 1.3 1.4... 4.9


def frange(start, end, step):
    Start = start
    start = float(start)
    end = float(end)
    step = float(step)
    array = []
    array.append(start)
    end = int((end - start) / step)
    for i in range(Start, end):
        array.append(array[i - 1] + step)
    return array


for i in frange(1, 5, 0.1):
    print(round(i, 2))