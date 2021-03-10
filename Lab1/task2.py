#Написать  скрипт,  который  выводит  на  экран «True»,  если  элементы программно  задаваемого  списка представляют
#собой  возрастающую последовательность, иначе –«False».
import random


def task2(array):
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            print(array)
            return False
    print(array)
    return True


array = []
for i in range(0, 10):
    array.append(random.randint(0, 10))
print(task2(array))
print(task2([1, 2, 3, 4, 5, 6, 7, 8]))