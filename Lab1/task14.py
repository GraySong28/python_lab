# Напишите декоратор non_empty,который  дополнительно проверяет списковый результат любой функции: если в нем
# содержатся пустые строки илизначениеNone, то они удаляются. Пример кода:
# @non_empty
# def get_pages():
#   return ['chapter1', '', 'contents', '', 'line1']


def non_empty(func):
    def wrapper():  # Обертка
        print(func)
        new_array = func()
        for i, data in enumerate(new_array):
            if data == ' ' or data == '':
                del new_array[i]
        print(new_array)
    return wrapper()


@non_empty
def get_pages():
    return ['chapter1', ' ', 'contents', '', 'line1']