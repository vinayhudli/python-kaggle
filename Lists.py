'''
Examples of lists and tuples
'''

planets = ["this", "is", "mixed", 4, "list"]
print("printing mixed data type list - ", planets, " length - ", len(planets))

# Cannot sort integer and string
# sorted(planets)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print("Sorted list - ", sorted(planets), " original list - ", planets)

primes = [2, 3, 5, 7]
print("sum of primes - ", sum(primes), " max number  - ", max(primes))

num = 12
help(num.bit_length)

planets.append('Pluto')
help(list.append)

planets.pop()
if "Earth" in planets:
    print("Earth is one of the planets at ", planets.index("Earth"))
    print("index entry 0 ", planets[0])

help(planets)

t = (1, 2, 3)
print("tuple is ", t)

'''
tuple is immutable that is they cannot be modified
t[0] = 100
'''

x = .125
numerator, denominator = x.as_integer_ratio()
print("example of function returning multiple values as tuple ", numerator, denominator)

# python trick of swapping variables
a = 1
b = 2
a, b = b, a
