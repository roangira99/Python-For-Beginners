# Python functions
# Functions are a good way to minimize code duplication
# Programs that have smaller functions are more readable and maintainable

# # function with no arguments
# def rocket_parts():
#     print("payload, prepellent, structure")

# # rocket_parts()

# # assigning output to a variable
# output = rocket_parts() # value of output variable is 'None' since the functions doesn't explicitly return a value
# print(output) 

# # updating the function to return the string instead of printing causes
# # the output variable to have a different value
# def rocket_parts():
#     return "payload, propellent, structure"

# output = rocket_parts()
# print(output)

# if you need to use the vlue of a function, tht function must return 
# explicitly otherwise 'None' will be returned

# required and optional arguments **run in python console**
# an example of a built-in function that requires n argument is any()
# the any() function takes an iterable and returns True if any item in the
# iterable is True, otherwise it returns False
# any([True, False, False]) # returns True 

# an example of a built-in function that allows the use of optional
# arguments is str(). This function creates a srting from an argument
# str()
# str(15)


# Using function arguments in Python
# requiring an argument
# def distance_from_earth(destination):
#     if destination == 'Moon':
#         return "238,855"
#     else:
#         return "Unable to compute that destination."
    
# print(distance_from_earth("Moon"))

# # multiple required arguments
# def days_to_complete(distance, speed):
#     hours = distance/speed
#     return hours/24

# print(days_to_complete(238855, 75))

# functions as arguments
# you can assign the function to a variable and then pass the variable 
# to another function
# total_days = days_to_complete(238855, 75)
# print(round(total_days))
# OR
# pass the function directly to another function
# print(round(days_to_complete(238855, 75)))


# Use keyword arguments in Python
# optional arguments require a default value assigned to them
# These named arguments are called keyword arguments
# when you are calling a function that's defined with keyword arguments, it
# isn't necessary to use them at all

from datetime import timedelta, datetime

def arrival_time(hours=52):
    now = datetime.now
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

# >>> arrival_time() # run in console

# even though the function defines a keyword argument, it allows not passing 
# one when you're calling a function.
# >>> arrival_time(hours=0) # run in console

# mixig arguments and keyword arguments