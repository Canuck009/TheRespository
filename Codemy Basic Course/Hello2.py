# Clears the screen
import os
import name_mod
os.system('cls')
######
############
##################### Date: 17Mar2022
############
######

# # # NOTES BY ME

# %s "is used to perform a 'concatenation' of strings together. It is used to incorporate another string within a string."
# *www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/*
# its used to insert a variable sting into another string.
# In this case, the value for 'baby' can be changed and the resulting script would always reflect that.
# the %s is placed where the desired string is to be inserted and after the closing quotations a % is places followed by the name of the variable.
# Same can go for numbers

baby = 'Olivia'
print("The baby's name is %s" % baby)
# A: The baby's name is Olivia

total = 9
print('The little girl just turned %s' % total)
# A: The little girl just turned 9

# or multiple
print('%s is turning %s today' % (baby, total))
# A: Olivia is turning 9 today

# this also works via a dictionary
fam = {
	'dad': 'Bear',
	'mom': 'Bunny',
	'daughter': 'Alyxis',
	'son': 'Thomas',
	'baby': 'Trent'
}

family = '%(dad)s %(mom)s %(daughter)s %(son)s %(baby)s' % fam
print(family)


# # # # # FUNCTIONS!!!!!

# A little program that runs within the code - anything ended by brackets

#print is a function

# Def defines the function and need to be in the script BEFORE the actual function is used.
# Its like a little box. So def f_name(firstname) means that we are defining the contents of f_name as 'firstname'.
# eg. when f_name is encountered, its contents will be recognised as the variable 'firstname'


def f_name(firstname):
	print('Hello %s' % firstname)

# this above will produce NOTHING - because its just defying the contents of f_name.


# Now.... using f_name in our code, calls back upon our original definition and follows the listed instruction we detailed... in this case, print.
f_name('Bear')
# Its been named
# A: Hello Bear

## this can also be done with multiple entries.

def full_name(forename, surname):
	print('Hello %s' % forename, surname)

full_name('Sean', 'Kennedy')
# A: Hello Sean Kennedy

# This can also be done with math

def values(num1, num2, num3):
	print(num2 * num1 / num3)

values(9, 2, 6)
# 2*9=18/6=3
# A: 3.0




######
############
##################### Date: 20Mar2022
############
######

# # # # # Functions 2!!!!!

# So a function, as the name suggests are NOT variables.
# they are methods of creating a set of instructions for a value.

def namer(subject):
	return ("My fav subject in uni is %s" % subject)

# in the above code i have used "return" which doesn't display anything, like "print" does, it just sets the value for later use.

F_Sub = namer ("Design")

print(F_Sub)
# A: My fav subject in uni is Design

# In the above code, i define the function "name" and that when encountered, to take the contents of its bracket and returning the result. I have then created a variable hich will be the result of my function, and then was able to "print" it.




######
############
##################### Date: 27Mar2022
############
######

# # # # # MODULES!!!!!

# Modules are programs/scripts that can be imported and used in my code.
# like in line 2 of this code, modules need to be imported. They are also all listed here https://docs.python.org/3/py-modindex.html where explanations and their respective codes can be looked at.

# They can be created.

# I have made a script and saved it in the same folder as this one, called "name_mod" and then ive added a line to line 3 importing that module/script.

# I originally tried to put it here is this days work, but it cleared all in the CMD after i ran it.

# the new mod can now be called on.

print (name_mod.name("Jetta"))
# A: My fav car is a Jetta

# so now i can just set values and it will use the module to seek answers.



# # # # # CLASSES

# A class is  blueprint that produces something, and can be altered. eg a house blueprint. The class has the blueprint for a house and you can give it some inputs for colour and size and it will spit out a house. Basic blueprint is the same, but can accept inputs.

# 2 main parts
# Class
# Initialization

# Kind of like a function where it had to be "Called upon", i have to create the class and then initialize it (use it/ call on it) further down in my scritp.

class Circle:
	pass

my_Circle = Circle()
# taking the output for the class and puttig it in this variable. this still produces nothing as there is no instructions or values in the class yet.

# Functions inside classes are called methods
# First method you need to creat within a new class is an initialisation method.
# This is done by def, 2 underscores, init (short for initialise), 2 underscores, and then brackets to pass in peramiters with, starting with "self" (which allows it to do things inside itself), any other perameters you want to use.

# For this example we used side length, as its a square.

class Triangle:
	def __init__(self, side_len):
		self.side_len = side_len # This is saying to use this variable within itself

my_Triangle = Triangle(10)
print(my_Triangle.side_len)
# A: 10
# Because we used a number in this example, we can do any of the number functions
print(my_Triangle.side_len + 12.2 - 2.2)
# A: 20.0

class Square:
	def __init__(self, side_length):
		self.side_length = side_length

	def area(self):
		area = self.side_length * self.side_length
		return ("Shape Area = %sm^2" % area)

	def perimeter(self):
		perimeter = self.side_length * 4
		return ("Perimeter = %sm" % perimeter)

	def Report(self):
		print("Side Length: %sm" % self.side_length)
		print("Area: %s" % self.area())
		print("Perimeter: %s" % self.perimeter())


my_Square = Square(10)
print(my_Square.area(), my_Square.perimeter())
my_Square.Report()
