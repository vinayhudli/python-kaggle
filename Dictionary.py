'''
Examples on dictionary
'''
numbers = {"one": 1, "two": "2", "3": "three"}
print("{} is the value for key 3 ".format(numbers["3"]))

numbers["eleven"] = 11
print("value for eleven is ",numbers["eleven"])

numbers["one"] = "one"
print("changed value of one ",numbers["one"])

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#dictionary comprehensions
planets_to_initials = {planet : planet[0] for planet in planets}
print("planets ", planets_to_initials)

for planet in planets_to_initials:
    print("planet {} initial {}".format(planet, planets_to_initials[planet]))

if( "Jupiter" in planets_to_initials):
    print("Jupiter is a planet")
else:
    print("Not a planet")

# get all the planets from the dictionary , sort them alphabetically and put them in space separated string
print("list of planets from dictionary ", " ".join(sorted(planets_to_initials.keys())))
print("list of initials from dictionary ", " ".join(sorted(planets_to_initials.values())))