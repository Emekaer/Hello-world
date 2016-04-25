"""
PYTHON SYNTAX
"""

"""
1 Comments
	Useful for providing additional information on how a piece/section of code works
"""

# This is a comment. It is a single line comment

# docstrings 


"""
This is a multiline comment
"""

# I can also use the pound / hash / naira [if you love Nigeria so] comment style
# to create a multiline comment
# this is a new line

# boolean =True or False

"""
2 Primitive Data Types
	Every programming language has its specific data types. Which are used for storing information about data [yes you guessed it] which your program needs to run
	For this introduction, we would be looking at the Primitive data types. They do not live in caves [ if you are wondering why they are called primitive]
	They are simply very basic. And pretty much every programming language has them in one form or another
"""

"""
a Numbers 
	We all know what numbers are. Brilliant!
	Python being an interpreted language does not require we explicitly tell it if a variable is a number or not
	Python is smart
	Python knows if a variable is a number or something else without you telling it.
	Be like Python!
"""

# Number Variable Declaration
number1 = 5
number2 = 57.98
number4 = - 8.494

# Invalid Number Declaration
# Even though the value in the quote is a number. Python would interpret it as a string
# To get the numeric value from this, we would need to do a `cast`
notANumber = "1"

# Casting
# casting attempts to convert a variable from its current datatype to the one specified
iAmNowANumber = int(notANumber)

# Oh and by the way, in programming you do not always provide all the data required to run your code
# sometimes that data comes from your users. If you need to verify the datatype of what they send as input
# python has a function for you!
type(iAmNowANumber)

"""
b Operations on Numbers
	Storing data is all good and fine, but that really is the boring part and python would not be popular if that is all it lets you do
	For Numbers python has the usual operators avaialble for manipulating numbers
"""

# addition
b = 2 + 2
a = b + 4
c = a + b
d = 3
d += 9

# subtraction
# pretty much the same as above except you are using `-` instead of `+`

# multiplication
# since `x` is already an alphabet, in most programming languages `*` is used for multiplication
e = 2 * 2
f = e * 2
g = e * f
h = 4
h *= g

# Division
# also same as above with `/` replacing `*`

# a note on division
# we know that a number can be a float (decimal place number) or an interger (whole number)
# when doing division in python if there is a possibility that you might get a float then you
# have to make it clear to python, e.g

# This would give 1 as the answer as opposed to 1.5
print 3/2

# To solve this, one of the operands must be a float number. This can be done in two ways
# 1 Explicitly make one of them a float
print 3.0/2

# 2 The method above works well if you are the one supplying the data. 
# If you do not have control over how the data comes in the you'll love this method
# Good 'Ol Casting
number5 = 3
print float(number5)/2

# Modulus
# Modulus returns the remainder of a division. It is always an integer
# the moduls of 11/4 is 3. Because 11/4 is 2 rem 3
# The python operator for modulus is %
print 11%4

# Comparing Numbers
# Python provides operators [not restricted to numbers as we shall see later] for comparing numbers
# They include the ususal suspects `>` for greater than, `<` for less than, `==` for equality
# `>=` and `<=` represent 'greater than' and 'less than' respectively
# `!` is used for negation
# the result of these comparisons is a boolean value. Meaning that it is can only be either True or False

print 45 > 40
print 56 == 57


# Using the Math library
# import it
import math

"""
2 Strings
	Strings are a very common data type. As there are many real world objects that can be represented with an acceptable
	level of detail in Strings. Some languages even blur the line between numbers and strings, allowing you to represent a number
	as a string [ As we learnt before, this is something that python does not allow]
"""

print 'this is a string'
print "this is also a string"

# combining two strings together in python is as simple as doing
myString = "cool"
yourString = "awesome"

allTogether = myString  + yourString
print allTogether

# you could also `multiply` a string. This would produce a new string which is a repitition of the original string
# and of which the frequency is determined by the other operand.
print allTogether * 2

# You can also compare strings
# ===
#  
print "cool" == "cool"

# remember python is case sensitive
print "cool" == "Cool"

# and more
print "a" > "b"
print "g" < "d"

"""
b String Formatting and special characters
	Python also provides special characters as we shall see in a bit, as well as a nice string formatting SYNTAX
"""

# `\` is called escape 
print "cool\n"
print "cool\n\n"
print "nice\tright ?\n"

# for string formats / placeholders
# %s -> strings
# %d -> numbers
# %.6f
gender = "boy"
print "This is a good %s" % gender

# I can also format with even more variables
print "I am at the %s event. It really is awesome. I should bring %d friends to join" % ("Lake Side Tech Track", 20)

# Who knows the value of PI to the 10th digit ?!
print "The value of PI to the 10th decimal place is %.10f" % (22.0/7)

"""
c Python String Functions
	So far we've learnt some cool stuff about strings and numbers. But python provides powerful functions which operate on a string
	To see these functions we would need to look at the python documentation and play with some of the functions there
"""

# str replace
firststring = "I am going home now"
secondstring = firststring.replace("now", "soon")