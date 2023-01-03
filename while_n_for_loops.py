# # Using while loops
# while loops are used in scenarios where looping for an unknown number of 
# times is required
# # variable for the user input
# user_input = ''

# # list that stores the user input
# inputs = []

# # while loop
# while user_input.lower() != 'done':
#     # Check if there's a value in user_input
#     if user_input:
#         # store the value in the list
#         inputs.append(user_input)
#     # prompt user for a new value
#     user_input = input('Enter a new value, or done when done: ')

#Types that can be looped over in Python are known as iterables E.g. lists
# Using for loops
# For loops are used with iterables where you'll loop a known number of times
# once for each item in the iterable
from time import sleep

countdown = [5, 4, 3, 2, 1]

for number in countdown:
    print(number)
    sleep(1) # Wait 1 second
print("Take off! 🚀")

