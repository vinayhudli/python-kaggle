'''
Example of loops
'''

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=" ")

# iterate through characters in string
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
for char in s:
    if char.isupper():
        print(char, end="")

# use of range function
for i in range(5):
    print(" number = ", i)

# list comprehensions examples
squares = [n ** 2 for n in range(10)]
print("squares value ", squares)

# list comprehension with if condition
short_planets = [planet for planet in planets if len(planet) < 6]
print("short planets ", short_planets)


# count negative numbers in list using list comprehension
def count_negative(nums):
    return len([num for num in nums if num < 0])


def alternate_count_negative(nums):
    return sum([num < 0 for num in nums])


print("number of negative values ", count_negative([-1, 0, 1, 2, -10]))
print("number of negative values alternative way ", count_negative([-1, 0, 1, 2, -10]))
