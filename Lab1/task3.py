#Напишите  скрипт,  который  позволяет  ввести  с  клавиатуры  номер дебетовой карты (16 цифр) и выводит номер в
# скрытом виде:первые и последние 4 цифры отображены нормально, а между ними –символы «*»
# (например, 5123 **** **** 1212)


def task3(card_numb):
    if len(card_numb) != 16:
        print('Введен некоректный номер карты')
    else:
        print(card_numb[:4], ' **** ' * 2, card_numb[12:])


card_numb = input('Введите номер кредитной карты: ')
task3(card_numb)