"""The map() Function: r = map(func, seq)"""
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celsius, F)
temperatures_in_Fahrenhei = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenhei))
print(temperatures_in_Fahrenhei)
print(temperatures_in_Celsius)

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
print(list(map(lambda x,y,z: x+y+z,a,b,c)))

"""
Exercises 1:
Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

Order Number    Book Title and Author              Quantity     Price per Item
34587           Learning Python, Mark Lutz             4          40.95
98762           Programming Python, Mark Lutz          5          56.80
77226           Head First Python, Paul Barry          3          32.95
88112           Einführung in Python3, Bernd Klein     3          24.99
Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity.
The product should be increased by 10,- € if the value of the order is smaller than 100,00 €.
Write a Python program using lambda and map.
"""
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],
           ["98762", "Programming Python, Mark Lutz", 5, 56.80],
           ["77226", "Head First Python, Paul Barry", 3, 32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]]
min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), map(lambda x: (x[0],x[2] * x[3]), orders)))
print(invoice_totals)


"""Mapping a List of Functions"""
print("Mapping a List of Functions")
from math import sin, cos, tan, pi
def map_functions(x, functions):
     return [ func(x) for func in functions ]

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))

"""Filtering"""
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)

"""Reduce
reduce(func, seq)
continually applies the function func() to the sequence seq. It returns a single value.
"""
from functools import reduce
reduce(lambda x,y: x+y, [47,11,42,13])

f = lambda a,b: a if (a > b) else b
reduce(f, [47,11,42,102,13])

