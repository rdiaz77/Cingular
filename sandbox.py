import requests
import json
# from array import array
# from sys import getsizeof
# from pprint import pprint


# # print("hello world")
# # print("Sofia " * 20)

# # x = 2
# # y = 9
# # print(x+y)
# # print(x / y)
# # print(x % y)
# # print(12 / 3)
# # print(12 % 3)
# # fruit = "Apple"
# # print(fruit[-1])
# # for number in range(1, 10, 3):
# #     print("Attempt", number)

# # count = 0
# # for x in range(1, 10):
# #     if x % 2 == 0:
# #         count += 1
# #         print(x)
# # print(f"we have {count} even numbers")


# # def multiply(*numbers):
# #     total = 1
# #     for number in numbers:
# #         total *= number
# #     return total


# # print(multiply(1, 2, 3, 4, 5, 10))

# # value = multiply(1, 2, 3, 4, 5, 10)
# # print(f'this is the result: {value}')

# # def fizz_buzz(number):
# #     if number % 3 == 0 and number % 5 == 0:
# #         return "fizz_buzz"
# #     if number % 3 == 0:
# #         return "fizz"
# #     if number % 5 == 0:
# #         return "buzz"
# #     return number


# # print(fizz_buzz(7))

# # number_list = list(range(1, 21))
# # print(number_list)

# # letters = list("hello")

# # print(letters)


# items = [("P1", 10), ("P2", 20), ("P3", 45), ("P4", 5)]
# prices = []
# products = []

# # for item in items:
# #     prices.append(item[1])
# # print(prices)

# # prices = list(map(lambda item: item[1], items))

# # print(f'lambda fuction: {prices}')

# # high_price = []

# # for item in items:
# #     if item[1] >= 10:
# #         high_price.append(item)

# # print(f' this is the long way {high_price}')

# # h_price = list(filter(lambda item: item[1] >= 10, items))
# # print(f'thi is the short way {h_price}')

# # point = (1, 22, 3, 4, 5, 6)
# # print(type(point))
# # point_list = list(point)
# # print(point_list)
# # print(type(point_list))

# numbers = array("i", [1, 2, 3, 4, 5])

# numbers.append(9)
# print(numbers)
# print(numbers[1])


# points = dict(x=3, t=10, z=8, y=7)
# print(type(points))

# for x in points:
#     print(x)

# print(points["t"])
# print(points.get("a"), 0)

# for key, value in points.items():
#     print(value)


# values = []

# for x in range(5):
#     values.append(x * 2)

# print(values)
# # in list comprehension syntax [expression for item in iterable if condition == True]
# # expression =  do something
# # item = loop variable

# values = [x * 2 for x in range(5)]
# print(values)

# # generated objects in ()

# # values_2 = (x * 2 for x in range(10000000))
# # print(values_2)
# # print(f'the size of value is {getsizeof(values_2)}')

# # numbers_3 = [1, 2, 3, 4, 5]
# # print(numbers_3)
# # print("value", numbers[0])
# # # unpacking operator *

# # print(*numbers_3)

# # values_3 = [*range(5), *"hello world", *{1, 2, 8, 9}]
# # print(values_3)


# sentence = "this is a common interview question"  # the most iterative letter


# frequency = {}

# for item in sentence:
#     if item in frequency:
#         frequency[item] += 1
#     else:
#         frequency[item] = 1
# print(frequency)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# # the __str__ magic method allows printing certain values from the class. Note that "f" is outside the parenthesis when using return

#     def __str__(self):
#         return f'({self.x} and {self.y})'


# # class method is useful to zero-out a class for example, and get back to preset/original values

#     @classmethod
#     def zero(cls):
#         return (0, 0)

#     def draw(self):
#         print(f"point x: {self.x} and point y: {self.y}")


# point = Point(1, 4)

# point.draw()
# print(f'y = {point.y}')

# point_zero = Point.zero()

# print(point_zero)

# # Chat Gpt List methods, magic methods

# print(str(point))

# tags = {"python": 3, "java": 4, "js": 5}

# print(type(tags))

# for tag in tags.values():
#     print(tag)


# class Animal:
#     def eat(self):
#         print("eat")


# class Bird(Animal):
#     def fly(self):
#         print("fly")


# panther = Animal()

# print(panther.eat())
d = requests.get("http://ergast.com/api/f1/2019/drivers.json")
d = d.json()
print(d)
# drivers = d["MRData"]["DriverTable"]["Drivers"]
# print(f'this is drivers {drivers}')