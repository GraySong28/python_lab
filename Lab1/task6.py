# Напишите  программу,  позволяющую  ввести  с  клавиатуры  текст предложенияивывестина консоль
# все символы, которые входят в этот текст ровно по одному разу.


def task6(str):
    print('Символы вхдящие в текст один раз: ')
    for i in str:
        if i == ' ': continue
        if str.count(i) == 1:
            print(i + ' ')


task6(input('Введите текст: '))