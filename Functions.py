'''
All about functions
'''

help(abs)

def least_difference(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return: least difference between 2 numbers
    """
    diff_a_and_b = abs(a-b)
    diff_a_and_c = abs(a - c)
    diff_b_and_c = abs(c - b)
    return min(diff_a_and_b, diff_a_and_c, diff_b_and_c)

help(least_difference)
print("minimum difference is ",least_difference(5,1,7))

def greet(who = "Vinay"):
    print("Hello ",who)

greet()
greet("World")
greet("Kaggle")

'''
passing functions as arguments
'''
def multiply_by_five(num):
    return num*5

def call_fn(fn, arg):
    return fn(arg)

def squared_call(fn, arg):
    return fn(fn(arg))

print("2 multiply by 5 ",call_fn(multiply_by_five, 2), sep=" - ")
print("square of 5 ", squared_call(multiply_by_five, 1), sep=" - ")