# Lists

# # creating a list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# # accessing list items by index
# print("The first planet is", planets[0])
# print("The second planet is", planets[1])

# modifying values in a list
# planets[3] = "Red Planet"
# print("Mars is also known as the", planets[3])

# getting the length of a list
# number_of_planets = len(planets)
# print("There are", number_of_planets, "planets in the solar system.")

# add values to lists
# planets.append("Pluto")
# number_of_planets = len(planets)
# print("There are actually", number_of_planets, "planets in the solar system")

# remove values from lists
# planets.pop() # will remove pluto
# number_of_planets = len(planets)
# print("No, there are definitely", number_of_planets, "planets in the solar system.")

# use negative indexes
# print("The last planet is", planets[-1])
# print("The penultimate planet is", planets[-2])

# find a value in a list
# jupiter_index = planets.index("Jupiter")
# print("Jupiter is the", jupiter_index + 1, "planet from the sun")


# # Store numbers in lists
# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
# print(gravity_on_planets[0])

# bus_weight = 12650 # in kilograms on Earth
# print("On Earth, a double-decker bus weighs", bus_weight, "kg")
# print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0])

# # use min() and max() with lists
# bus_weight = 12650
# print("On Earth, a double-decker bus weighs", bus_weight, "kg")
# print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg.")
# print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg.")


# Manipulate list data
# slice lists
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# planets_before_earth = planets[0:2]
# print(planets_before_earth)

# planets_after_earth = planets[3:8]
# print(planets_after_earth)

# # join lists
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_group = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_group
# print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# # sorting lists
# regular_satellite_moons.sort()
# print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True) # sorts the list in reverse order
print("The regular satellite moons of Jupiter are", regular_satellite_moons)