from simple_calc import *


def sum_of_two(x,y):
    calc = Calculator()
    return calc.add(x,y)


def sum_of_three(x,y,z):
    calc = Calculator()
    return calc.add(calc.add(x,y),z)


def multiply(x,y):
    s=0
    for in range(y):
        s = sum_of_two(s,x)
        return s
    
    def start(x,y,z):
        s = []
        s.append(sum_of_two(x,y))
        s.append(sum_of_three(x,y,z))
        s.append(multiply(x,y))
        return s