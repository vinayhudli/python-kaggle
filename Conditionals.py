'''
conditional examples
'''

x = True
print(x)
print(type(x))

def legal_to_drink(age):
    #is this age eligible to drink
    return age >= 18

print("can 16 year old drink beer ", legal_to_drink(16),sep=" - ")

def is_odd(num):
    return num%2 != 0

print("Is 100 odd - ",is_odd(100))

def can_drink_run_for_president(age, is_natural_born_citizen):
    return age>=35 and is_natural_born_citizen

print(" Can run for president - ",can_drink_run_for_president(36, True))

def inspect(x):
    if x == 0:
        print("number is 0")
    elif x > 0:
        print("number is positive")
    elif x < 0:
        print("number is negative")
    else:
        print("I don't recognize this")

inspect(3.412)

def quiz_result(grade):
    result = "passed" if grade > 50 else "failed"
    print("Your quiz result is - ",result)

quiz_result(40)
