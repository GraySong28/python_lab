# Напишите параметризированный декоратор pre_process, который осуществляет  предварительную  обработку  (цифровую  фильтрацию)
# списка  по  алгоритму: s[i]  = s[i]–a∙s[i–1].Параметр  а  можно  задать  в коде (по умолчанию равен 0.97).
# Примеркода:
# @pre_process(a=0.93)
# def plot_signal(s):
#   for sample in s:
#       print(sample)


def pre_process(a = 0.97):
    def wrapper():
        for i in range(len(array)):
            array[i] = array[i] - a * array[i - 1]
        print(array)
    return wrapper()


array = [1.3, 0.1, 14.8, 28.06]


@pre_process(a=0.93)
def plot_signal(array):
    print()
