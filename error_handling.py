# Python error handling
# Handling exceptions
# Try and except blocks
# try:
#     open('config.txt')
# except FileNotFoundError:
#     print("Couldn't find the config.txt file!")

# # Traceback error demo
# def main():
#     open("/pth/to/mars.jpg")

# if __name__ == '__main__':
#     main()

# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")

# if __name__ == '__main__':
#     main()

# when errors are of a similar nature and there's need to handle them 
# individually, you can group the exceptions together as one using 
# parantheses in the except line

# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")
#     except (BlockingIOError, TimeoutError):
#         print("Filesystem under heavy load, can't complete the reading configuration file")

# if you need to access the error that's associated with the exception, you 
# must update the except line to include the as keyword
# when a raised exception will be reused or inspected, the as err statement
# can help
# try:
#     open("mars.jpg")
# except FileNotFoundError as err:
#     print("got a problem trying to read the file:", err)

# this technique is used to access attributes of an error directly
try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couldn't read it")

# def water_left(astronuts, water_left, days_left):
#     for argument in [astronuts, water_left, days_left]:
#         try:
#             # if an argument is an int, the following operation will work
#             argument / 10
#         except TypeError:
#             # TypeError will be raised only if it isn't the right type
#             # Raise the same exception but with a better message
#             raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
#     daily_usage = astronuts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     if total_water_left < 0:
#         raise RuntimeError(f"There is not enough water for {astronuts} astronauts after {days_left} days!")
#     return f'The total water left after {days_left} days is: {total_water_left} liters'

# print(water_left(5, 100, None))