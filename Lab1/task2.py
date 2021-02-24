#Написать  скрипт,  который  выводит  на  экран «True»,  если  элементы программно  задаваемого  списка представляют
#собой  возрастающую последовательность, иначе –«False».
import random


def task2(array):
    false, true = 0, 0
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            false += 1
    print(array)
    if (false > 0): return False
    else: return True


array = []
for i in range(0, 10):
    array.append(random.randint(0, 10))
print(task2(array))
print(task2([1, 2, 3, 4, 5, 6, 7, 8]))