# Выберите  произвольную  дифференцируемую  и  интегрируемую функцию одной переменной.
# С помощью модуля symPyнайдите и отобразите  еепроизводную  и  интеграл  в  аналитическом  и графическом  виде.
# Напишите  код  для  решения  произвольного нелинейного урванения и системы нелинейных уравнений.


from sympy import *


# Производная и интеграл
def derivative_integral():
    x = Symbol('x')
    function = cos(x)
    print('Функция: ', str(function))
    print('Производная: ', diff(function))
    print('Интеграл: ', integrate(function))


def solution(*equalities):
    if len(equalities) == 1:
        return solve(equalities[0])
    return solve_poly_system(equalities)


# Решение ситиемы и уровнения
def equation():
    x, y = symbols('x y')
    eq1 = Equality(3, x**2 - y)
    eq2 = Equality(9, x*(y**3))
    eq3 = Equality(2/x, -8)
    pprint(solution(eq1, eq2))
    pprint(solution(eq3))


derivative_integral()
equation()
