import numpy
from numpy.linalg import det, inv


# 1) умножение произвольных матриц А (размерности 3х5) и В (5х2)
first_matrix = numpy.arange(3 * 5).reshape((3, 5))
second_matrix = numpy.arange(5 * 2).reshape((5, 2))
print('Первая матрица:\n', first_matrix)
print('Вторая матрица:\n', second_matrix)
print('Умножение:\n', first_matrix @ second_matrix)
print()

# 2) умножение матрицы на вектор
matrix = numpy.arange(2 * 3).reshape((3, 2))
vector = numpy.array([1, -1], dtype=float)
print('Матрица:\n', matrix)
print('Вектор:\n', second_matrix)
print('Умножение матрицы на вектор: ', matrix @ vector)
print()

# 3) решение произвольной системы линейных уравнений
# x - y = 7
# 3x + 2y = 16
matrix = numpy.array([[1., -1.], [3., 2.]])
vector = numpy.array([7., 16.])
print('Система:\nx - y = 7\n3x + 2y = 16')
answer = numpy.linalg.solve(matrix, vector)
print('x: ', answer[0], 'y: ', answer[1])
print()

# 4) расчет определителя матрицы
matrix = numpy.arange(5 * 5).reshape((5, 5))
print('Матрица: ', matrix, '\n', 'Определитель: ', det(matrix))
print()

# 5) получение обратной и транспонированной матриц
a = numpy.array([[0, 4, 2], [4, 6, 6], [7, 9, 10]])
print('Исходная матрица:\n', a)
print('Обратаня матрица:\n', inv(a))
print('Транспонированная матрица:\n', a.transpose())
