# Beginner Series #1 School Paperwork

# KATA_1
# Your classmates asked you to copy some paperwork for them. You know that there are 'n'
# classmates and the paperwork has 'm' pages.#
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
# # Example:
# n= 5, m=5: 25
# n=-5, m=5:  0

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m

# KATA_2
# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.
# # Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return string * repeat

# KATA_3
# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

# KATA_4
#Summation
# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.

# For example:

# summation(2) -> 3
# 1 + 2

# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):
    return sum(range(int(num) + 1))

# KATA_5
# Can you find the needle in the haystack?
# # Write a function findNeedle() that takes an array full of junk but containing one "needle"
# # After your function finds the needle it should return a message (as a string) that says:
# # "found the needle at position " plus the index it found the needle, so:
#
# Example(Input --> Output)
# # ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
# Note: In COBOL, it should return "found the needle at position 6"

def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

# KATA_6
# After a hard quarter in the office you decide to get some rest on a vacation.
# So you will book a flight for you and your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation. T
# he manager of the car rental makes you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total.
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).

def rental_car_cost(d):
    if 3 <= d <= 6:
        return d * 40 - 20
    elif 7 <= d:
        return d * 40 - 50
    else:
        return d * 40

# KATA_7
# DESCRIPTION:
# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language )
# that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
# # Examples (Input -> Output)
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# Notes
# You may consider that there will not be any empty arrays/vectors.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# KATA_8
#