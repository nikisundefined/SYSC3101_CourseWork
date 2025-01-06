"""
SYSC 3101 Winter 2024
Lab 1, Part 1, Exercises 1,2 and 3
"""

__author__ = 'Nicholas Nemec'
__student_number__ = '101211060'

# solution to Exercise 1
#-----------------------

def power(x:float, n:int):
    """Return x raised to the power n for n >= 0. """
    # your code goes here
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


# solution to Exercise 2 
#-----------------------
def perrin(n:int):
    # your code goes here
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2
    return perrin(n-2) + perrin(n-3)


# solution to Exercise 3 
#------------------------
def count_in_list(my_list, n, target):
    """Return the count of the number of times target occurs in the first
    n elements of list my_list."""
    # your code goes here
    if n == len(my_list):
        n -= 1
    increment = 0
    if my_list[n] == target:
        increment = 1
    if n == 0:
        return increment
    return increment + count_in_list(my_list, n-1, target)

