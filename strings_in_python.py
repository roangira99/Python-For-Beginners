# using quotation marks
# fact = "The Moon has no atmosphere."
# two_facts = fact + " No sound can be heard on the Moon."
# print(two_facts)

# moon_fact = 'The "near side" is the part of the Moon that faces the Earth'
# print(moon_fact)
# moon_fact2= "We only see about 60% of the Moon's surface"
# print(moon_fact2)
# combination_of_moonfacts = """We only see about 60% of the Moon's surface, this is known as th "near side"."""

# multiline text
# multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
# print(multiline)
# OR
# multline = """"Facts about the Moon:
#   There is no atmosphere.
#   There is no sound."""
# print(multline)


# String methods in Python
# using a method with the string directly
# moon_info = "temparatures and facts about the moon".title()
# print(moon_info)

# using a string method on a varible
# heading = "temparatures and facts about the moon"
# print(heading.title())

# split a string
# top_speeds = "Maserati: 340kmph Lamborghini: 360kmph"
# print(top_speeds.split())

# top_speeds = """Maserati: 340kmph 
# Lamborghini: 360kmph"""
# print(top_speeds.split('\n'))

# search fro a string
# The 'in' operator can be used to search whether a given word, charcter, or
# group of chracters exits in a string

# we can also use the find method to search for a specific word in a string
# dailylife = """A full stack MERN application that allows users to post 
# interesting events that happened in their lives"""
# print(dailylife.find("MERN"))
# print(dailylife.count("that")) # count returns the total number of occurences of a certain word

# # converting string to all lowercase
# lowercase = "The Italian Mafia Takeover".lower()
# print(lowercase)

# # converting string to all uppercase
# uppercase = "The Italian Mafia Takeover".upper()
# print(uppercase)


# Check content
# extracting a specific string
# temparatures = "Mars Average Temparatures: -60 C"
# parts = temparatures.split(':') # splits the string where there is a colon
# print(parts)
# print(parts[-1]) # returns the last item after splitting

# checking content of irregular text
# mars_temparature = "The highest temparature on Mars is about 28 - 30 C"
# for text in mars_temparature.split():
#   if text.isnumeric():
#     print(text)

# the startswith method can be used to detected the first character of a string
# check = "-60".startswith('-')
# print(check)

# the endswith method can be used to detected the last character of a string:
# if "30 C".endswith("C"):
#   print("The temparature is in Celsius")

# Transform text
# the replace method can be used to find and replace occurences of a character
# or a group of characters
# replace = "Saturn has a daytime temparature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")
# print(replace)

# using lower method to normalize text when doing a case-insensitive search
# text = "Temparatures on the Moon can vary wildly".lower()
# if "temparatures" in text:
#   print("True")

# using the join method to put parts of a string together. This method
# requires an iterable, such as a Python list as an argument
# car_details = ["The new GT Camaro were shipping in is maroon in color. ", "There is also a grey Audi thats going to arrive in a month."]
# print('\n'.join(car_details))


# String format in python
# percentage sign formtting
# mass_percentage = "1/6"
# print("On the Moon, you would way about %s of your weight on earth" % mass_percentage)

# The format method
# mass_percentage = "1/6"
# print("On the Moon, you would way about {} of your weight on earth".format(mass_percentage))
# print("""You are lighter on the {moon}, because on the {moon}
# you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

#f-strings
# mass_percentage = "1/6"
# print(f"On the Moon, you would way about {mass_percentage} of your weight on earth")
# print(f"On the Moon, you would way about {round(100/6, 1)}% of your weight on earth")

subject = "interesting facts about the moon"
print(f"{subject.title()}")



