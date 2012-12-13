'''
Created on Dec 10, 2012

@author: Mike
'''
#
# comparisons01.py
#
# This script shows how to compare two integers
#
# First we enter some instructions to the user. The
# more the user knows how to work the program the less
# likely it is that the user will make a mistake.

#
import sys

print sys.argv[1:]
print "Enter two integers and I will tell you"
print "the relations they satisfy"
#
# Make 2 vraiables, number1 and number2. Ask the user to
# input two numbers. Assign them to our two variables and
# convert them from strings to integers.
# The comparisons that we demonstrate here are comparisons
# of NUMBERS. These comparisons will not work if the
# variables remain as strings. Strings can be compared but
# not in the ways we show here.
#
number1 = raw_input( "Please enter the first integer: " )
number1 = int(number1)

number2 = raw_input( "Please enter the second integer: " )
number2 = int(number2)

if number1 == number2:
    print "%d is equal to %d" % (number1, number2)
    
if number1 != number2:
    print "%d is not equal to %d" % (number1, number2)
    
if number1 < number2:
    print "%d is less than %d" % (number1, number2)
    
if number1 > number2:
    print "%d is greater than %d" % (number1, number2)
    
if number1 <= number2:
    print "%d is less than or equal to %d" % (number1, number2)
    
if number1 >= number2:
    print "%d is greater than or equal to %d" % ( number1, number2 )

dummy=raw_input()