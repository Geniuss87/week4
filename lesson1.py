# lamda function

# decorators

# sq_number = lambda x: x ** 2
# print(sq_number(3))
#
# upper_str = lambda x: x.upper()
# print(upper_str("ffff"))
#
# sum_list = lambda x: sum(x)
# print(sum_list([1, 2, 3]))
#
# sum_numb = lambda x, y: x * y
# print(sum_numb(3, 7))


# dict comprehension

# kpi = {
#     "math": [1, 2, 3],
#     "python": [4, 5, 6],
#     "java": [7, 8, 9]
# }
# dict_numbers = {key: sum(value) if sum(value) != 15 else None for key, value in kpi.items() if sum(value) > 10}
# print(dict_numbers)


#enumarate

# lists = [2, 4, 5, 6]
# dict_m = dict(enumerate(lists))
# print(dict_m)


# map filter, reduce


# def get_set_factorial(rad):
#     factorial = 1
#     for i in range(1, rad + 1):
#         factorial = factorial * i
#     return factorial
# list_num = [3, 4, 5]
# tuple_fact = tuple(map(get_set_factorial, list_num))
# print(tuple_fact)
#
# def sum_num(a, b):
#     return a + b
#
# lst_num1 = [1, 2, 3, 4]
# lst_num2 = [1, 2, 3]
# sum_lst = list(map(sum_num, lst_num1, lst_num2))
# print(sum_lst)
#
# filter
# lst_str = ["Nurlan", "Marjangul", "Salamat", "Azamat"]
# def get_new_names(a):
#     if len(a) >= 7:
#         return a
# lst_new_names = list(filter(get_new_names, lst_str))
# print(lst_new_names)

# lst_str1 = ["Nurlan", "Marjangul", "Salamat", "Azamat"]
# lst_str2 = ["Aijan", "Marjangul", "Samat", "Azamat"]
# def get_new_names(a, b):
#     if a == b:
#         return a
# lst_names = list(filter(lambda a: a is not None, list(map(get_new_names, lst_str1, lst_str2))))
# print(lst_names)

#reduce
from functools import reduce

lst_num1 = [1, 2, 3, 4]
def get_multiple(num1, num2):
    return num1 * num2
mult = reduce(get_multiple, lst_num1)
print(mult)

#lambda
mult1 = reduce(lambda x, y: x + y, lst_num1, 10)
print(mult1)


#decorator

# def make_hamburger(func):
#     def wrapper():
#         print("up bred")
#         print("mayonez")
#         func()
#         print("cetchup")
#         print("low bred")
#     return wrapper
#
# @make_hamburger
# def make_cotlet_beef():
#     print("beef cotlet")
#
# def make_cotlet_chicken():
#     print("chicken cotlet")
#
# make_cotlet_beef()


