'''
String examples
'''

hello = "hello " \
        "world"

print(hello)

triple_quote_string = '''hello world'''

print(triple_quote_string)

# in string comparison actual values are compared
print("both strings are same ? ", hello == triple_quote_string)

# string is considered to be list of characters
planet = 'Pluto'
print("first element ", planet[0])
print("last 3 characters ", planet[-3:])
print("length of string ", len(planet))

print(" characters are ", [char+"!" for char in planet])

#string as character array is immutable
#planet[0] = "B"

concatenation = planet+" used to be 9th planet"
print(concatenation)

position = 9
#contenating other data type to string, they have to be cast to string first
concatenation = planet+" used to be "+str(position)+"th planet"
print(concatenation)

#for better readability
result = "{} used to be {}th planet".format(planet, position)
print(result)

#formatting example
pluto_mass = 10.313 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
statement = " {} weighs about {:.2} kg ({:.3%} of earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass, pluto_mass/earth_mass, population)
print(statement)

# Referring to format() arguments by index, starting from 0
str = """ Pluto's a {0} .
No, it's a {1} .
{0} !
{1} !""".format("planet", "dwarf planet")
print(str)
print("Pluto's a {0} .\n No, it's a {1} .\n {0} ! \n {1} !".format("planet", "dwarf planet"))
