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
# In this simple assignment you are given a number and have to make it negative.
# But maybe the number is already negative?
# # Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative(number):
    if number >= 0:
        return number * (-1)
    else:
        return number

# KATA_9
# Grade book
# Complete the function so that it finds the average of the three scores passed to it and
# returns the letter value associated with that grade.
#
# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values
# or values greater than 100.

def get_grade(s1, s2, s3):
    get_grade = (s1 + s2 + s3) / 3
    if 90 <= get_grade <= 100:
        return 'A'
    elif 80 <= get_grade <= 90:
        return 'B'
    elif 70 <= get_grade <= 80:
        return 'C'
    elif 60 <= get_grade <= 70:
        return 'D'
    return "F"


# KATA_10
# Find the odd integers
# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
#
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return(i)
    return None


# KATA_11
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    for n in set(arr):
        if arr.count(n) == 1:
            return n   # n: unique number in the array


# KATA_12
# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).
# # Examples:
# # solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    return string.endswith(ending)  # https://pythonstart.ru/string/endwith-python
# solution('abcde', 'abc') => False
# solution('abcde', 'cde') => True
# solution('abcde', '') => True
