######
############
##################### Date: 22Feb22
############
######

# Clears the screen
import os
os.system('cls')

# This is a variable and string. Variable in the same respects as Matlab where you can just name something to refer to later. CASE matters.
first_name = "bear"

print (first_name)

######
############
##################### Date: 23Feb22
############
######

# # # # # DATA TYPES

#Strings
first_name = "Bear"

# Multiline srtings need to start ith a triple ' = '''
#eg.
st_joke = '''what's black and white,
black and white, black and white and green?
3 skunks fighting over a pickle'''

print (st_joke)

# Numbers
# This is still a variable (like matlab) but note the lack of quotations. Quotations can still be put around the number, but then it turns into a string.
Age = 39

# Lists (arrays in other programming languages)
# A list of variables sperated by a comma. When writing code to refer to any item within that list, they are numerically listed starting at 0. eg (my_kids = ["0", "1"])
my_kids = ["Alyxis", "Thomas"]
print (my_kids[0])
# This will display Alyxis' name.

# Tuple
# Like a list but cannot be changed. Act the same way but cannot be added to or taken from. You can tell them apart by the normal brackets vs the square ones.
not_my_kids = ("Jim", "Sam")
print (not_my_kids[1])
# This will display Sam

# Dictionaries  (Hashes in other programming languages)
# Like a list but has a "key": "value", for eack listed item.
baby_names = {
	"boy": "Trent",
	"girl": "Olivia",
	"Code": "Python"
}
# To ues this, use their "key" and will display the "value"
print (baby_names["girl"])
# This will display Olivia

######
############
##################### Date: 24Feb22
############
######

# # # # # STRINGS

# The quotation marks box in the string. you can use either single ' or double " and even mix them. It is the one you start with that you have to end with.
# eg. Talking = "my wife said, "lets walk the dogs"" <- This wont work and will produce errors.
Talking = 'my wife said, "lets walk the dogs"'

print (Talking)

# There is also something called and "escape characters" - a backslash - \ - which pretty much tells the computer to treat the following character as NOT-code... eg. to follow
Talking_to = "my wife said, \"lets walk the dogs\""

print (Talking_to)

# both those will produce the same result.

# In your string, if you want something to be pushed to the next line, the escape character \n can be used before the text
Talking_3 = "my wife said, \n\"lets walk the dogs\""

print (Talking_3)



# # # # # STRING MANIPULATION

string_mn = "My name is Sean Kennedy"

print(string_mn)
# Space after print is optional

# putting a period after the variable name allows you to manipulate it. eg. to make the string all CAPS ".upper()" is used. *note this is done in the print function.
print (string_mn.upper())
# Same for lower case
print (string_mn.lower())
# And to capitalize the first letter
print (string_mn.capitalize())
# to capitalize the first letter of every word
print (string_mn.title())
# or to swap the cases of the original string
print (string_mn.swapcase())

# Another function len with tell you the length of a string.
print (len(string_mn))
# A: 23

# Individual characters can also be called up, simular to the lists above
print (string_mn[11])
# A: S

# A range can also be recalled
print (string_mn[11:15])
# A: Sean

# If you want the range to be the end of the string (rather than counting out how many characters there are) you can enter the len function from before. (like matlab)
# like above the "11" is the fist caracter of the range so 11:Len(means the length of the string)
print (string_mn[11:len(string_mn)])
# A: Sean Kennedy

# The string can also be split up, and you can specify the character to use to split it. like in the case of the below example, a space is used.
print (string_mn.split(" "))
# The result looks like a list .
# A: ['My', 'name', 'is', 'Sean', 'Kennedy']

# The above split string can then also be called upon like a list.
print (string_mn.split(" ")[4])
# A: Kennedy

# It can be further manipulated - so the string will be split, called upon  one portion and then it can be CAPS'd
print (string_mn.split(" ")[4].upper())
# A: KENNEDY



# # # # # MATH!!!!!!!!!! :(

# So very Simular to matlab... So far. print function is used so we can see answers in the CMD window.
print (234+345)
# Exponents though... ** double star ... 3^3 (three cubed)
print (3**3)

# There is something called the "modulus" % discribed as the remainder after division. so in eg. 10 / 3
print (10%3)
# A: 1 as 3 devides into 10 3 times (9) and has 1 remainder
print (10%2)
# A: 0 cause there are no remainders

# B.E.D.M.A.S. works!
print (3+1*4)
# A: 7
print ((3+1)*4)
# A: 16



# # # # # NUMBERS: FLOATS (decimal) & INTS (Integers - whole number)!!!!!!!!!

# used to differnciate whole and fractions of numbers
nnum1 = 10
nnum2 = 3
print (nnum1/nnum2)
# A: 3.3333333333333335  -  Gives us the real answer

print (int(nnum1/nnum2))
# A: 3  -  as it rounds to the nearest whole

# You can also ask it to round to a specific decimal
print (round((nnum1/nnum2),2))
# A: 3.33  -  the 2 being the required decimals



# # # # # ASSIGNMENT OPPERATORS!!!!!!

# A character or function that assigns something (string, number etc.) to a variable. eg. the equals sign is the assignment opperator

nnum3 = 12

# Math functions can be opperators too, when put together with an = equal sign.

#+=   Means add and assign
#-=   Means subtract and assign
#*=   Means multiply and assign
#/=   Means devide and assign
#**=   Means exponent and assign
#%=   Means modulus and assign

# How is this useful?
# If you needed somthing to count sequentually it could look like this:
nnum3 = nnum3 + 1
# This takes the original value, adds one and then rewrites nnum3 as the new number. when run the code the value of nnum3 would increase by 1.
# This is exctly the same as doing this:
nnum2 += 1

print (nnum3, nnum2)
# A: 13 4



# # # # # LIST!!!!!!!


# Lists are very versitile, and lists can refer to lists, that refer to list, that refer to variables.

LBaby = "Olivia"

Lnum = [1,2,3,4,5]

Lfamily_names = ["Sean", "Laura", "Alyxis", "Thomas", LBaby, 9, Lnum]
# Lists can contain a mixture of strings, numbers, variables etc.

print (Lfamily_names)
# A: ['Sean', 'Laura', 'Alyxis', 'Thomas', 'Olivia', 9, [1, 2, 3, 4, 5]]

# Next is how to change one something on the list.
Lfamily_names[0] = "Bear"

print (Lfamily_names)
# A: ['Bear', 'Laura', 'Alyxis', 'Thomas', 'Olivia', 9, [1, 2, 3, 4, 5]]

# You can delete them
del Lfamily_names[5]

print (Lfamily_names)
# A: ['Bear', 'Laura', 'Alyxis', 'Thomas', 'Olivia', [1, 2, 3, 4, 5]]

# You can add to your list with .append
Lfamily_names.append("Trent")

print (Lfamily_names)
# A: ['Bear', 'Laura', 'Alyxis', 'Thomas', 'Olivia', [1, 2, 3, 4, 5], 'Trent']


# lists are rarely going to be this small. so the len command from earlier can be used to determine the amount of things in your list.
print (len(Lfamily_names))
# A: 7  -  As it counts the list of numbers as a single item on the list.
# but the items are counted from zero, so if you wanted it to display the last item...

print (Lfamily_names[len(Lfamily_names)-1])
# A: Trent  -  This says print from list[position] - in position it is [len(list)-1]




######
############
##################### Date: 06Mar22
############
######

# # # # # TUPLES!!!!!!

# A list but cannot be changed once created. This is done by using () vs []
tuple_1 = ('Sean', 'Laura', 'Alyxis', 'Thomas')

print (tuple_1)
# A: ('Sean', 'Laura', 'Alyxis', 'Thomas')

# Why use a tuple?
# Tuples are faster to process and read.
# thought they cannot be changed, there are backdoor ways of altering them.
# eg. to add an entry to a tuple, a second tuple can be created and then the 2 can be "added" to eachother.

tuple_2 = ('Olivia',)

tuple_3 = tuple_1 + tuple_2

print (tuple_3)
# A: ('Sean', 'Laura', 'Alyxis', 'Thomas', 'Olivia')

# it is also possible to subtract entries out as well, by using the range function
# 0:4 = 0 Being the first term and the 4 being "up to, but not including the 5th term"
tuple_4 = tuple_3[0:4]

print (tuple_4)
# A: ('Sean', 'Laura', 'Alyxis', 'Thomas') - removed the last enrty

# and same kinda thing to replace entries.
tuple_5 = ('Trent',) # DONT FORGET COMMA ON SINGLE LIST AND TUPLE ENTRIES
tuple_6 = tuple_4[0:4] + tuple_5
# this will create a new tuple with olivia removed and replaced with trent.

print (tuple_6)
# A: ('Sean', 'Laura', 'Alyxis', 'Thomas', 'Trent')



# # # # # DICTIONARY!!!!!!

# Reminder - Dict are identified by {} and are formatted 'KEY': 'VALUE',
D_fav_pizza = {
	'Sean': 'cheese',
	'Laura': 'bbq',
	'Alyxis': 'pepperoni',
	'Thomas': 'pepperoni',
	'Ash': 'beef',
	'Bailey': 'fish'
}
# Dont forget commas!!

print (D_fav_pizza)

# When calling up information, we only need to use the key.
print (D_fav_pizza['Laura'])
# A: bbq

# To add or remove
del D_fav_pizza['Ash']
# deletes ash AND his favourite pizza

print (D_fav_pizza)

# To ammend - enter the key and then = the new value.
D_fav_pizza['Bailey'] = 'beef'

print (D_fav_pizza)

# To add to the bottom of our dictionary
D_fav_pizza.update({'Ash': 'hamburger'})

print (D_fav_pizza)



# # # # # COMPARISON OPPERATORS

# Used to compare things - asks the question
# '==' is a comparison opperator and askes the question 'does this equal that'

# eg.
print (10 == 10)
# A: True

print (9 == 10)
# A: False

# And the '!=' asking the question 'deoes this NOT equal that?'
# Eg.
print (9 != 10)
# A: True

print (10 != 10)
# A: False

print (10 <= 11)
# A: True

print (11 <= 10)
# A: False

# And works with strings.
print ('john' == 'tim')
# A: False

# Workes with lists too
print ([1,2,3] == [1,2,3])
# A: True


#  == does it equal
#  != does it NOT equal
#  >  greater than
#  <  less than
#  >= greater or equal to
#  <= less than or equal to



######
############
##################### Date: 09Mar2022
############
######

# # # # # CONDITIONAL STATEMENTS

# If
# Else
#Elif

# If is just as you'd expect. using the if statement, followed by the ('variable' and 'comparison operator' and the 'check' - the value your comparing to)
# After the closing bracket, the colon is used to identify the next step. eg. if cs_num IS greater than or equal to 10..... THEN WHAT?
# As you can see below

cs_num = 9
if (cs_num >= 10):
	print ('your number is greater than or equal to 10')

# An else statement can be also attached to this - stating "if variable " - if cs_num IS NOT greater than or equal to 10..... THEN WHAT?
else:
	print ('your number does\'t fall in the required range')

# There is also elif. it is a intermediary. if it was a yes/no (2 answer issue) then you'd only need if and else. if there us more than 2 conclusions, then you need elif.

cs_num2 = 5
if (cs_num2 >= 6):
	print ('your number is too high')

elif (cs_num2 in range(1, 5)):
	print ('your number is too low')

elif (cs_num2 == 5):
	print ('your number is ideal')

else:
	print ('your number is out of range')

# Did a bit of self-exploring and came up with what you see above. Discovered the range and 'in' command.
# This meant i could make look into a range of number and to give specific answers. AWESOME!



# # # # # MULTIPLE CONDITIONAL STATEMENTS

# This is adding additional statements onto a single line with if or else - using 'and' and 'or'

# Using the 'and' you can add multiple conditions that have to be met to trigger certain outcomes.
mcs_num = -1
if (mcs_num >= 56) and (mcs_num <= 100):
	print ('number range too high')

elif (mcs_num >=1) and (mcs_num <= 44):
	print ('number range too low')

elif (mcs_num >=45) and (mcs_num <= 55):
	print('number in range')

else:
	print ('ERROR! your number is out of range')

# using 'or' means that only 1 of the conditions you set has to be true to trigger the outcome



# # # # # WHILE LOOPS

# does a task over and over until a condition is met.
# lots of types of loops - this is focusing on 'while loop'

# This 'while loop' looks at this counter and says 'does this variable meet the condition stated (<= 10)' - if yes, it triggers the next line.
# If no, it ignores the next line and carries on to the next. Once it finishes the intented instruction, it restarts. in this case, in the
# indented instructions, i wrote, if it doesnt meet the initial condition, add 1 to the counter... and then it restarts.

wl_counter = 0
while (wl_counter <= 10):
	print ('The counter is: %s' % wl_counter)
	wl_counter += 1



# # # # # FOR LOOP

# above, a while loop contiues until the condition is met... A FOR loops through things. eg. Lists, Dictionaries, variables...

f_loop = 'bears'
# after the 'for' function, a variable is used - in this case 'x' - though anything can be used.
for x in f_loop:
    print(x)
# A:
#
# b
# e
# a
# r
# s

# Now lets try with tha list.

f_looplst = ['bear', 'bunny', 'bebebear1', 'bebebear2']
for y in f_looplst:
    print (y)
# A:
#
# bear
# bunny
# bebebear1
# bebebear2

# This can also be done with dictionaries.
bebenames = {
    'boy': 'Trent',
    'girl': 'Olivia',
    'other': 'brian'
    }

# for this one, because there is 2 values, 2 variables are used - coulb be anything - x, y - a, b - key, value.
# We also use the
for key, value in bebenames.items():
    print (value)
# The variable put into the print subject, will list all the respective items.
# A:
#
# Trent
# Olivia
# brian

# # # # # JUST PLAYING AROUND

# Password = 'none'
# while Password != ('Superman'):  # this is saying 'Password does NOT EQUAL (!=) Superman. which is a true statement, so it triggers the next line.
    # Password = input('Enter Password: ')  # so from above, if passowrd doesnt equal superman, then allow an input for variable 'password' with the .input command.
    # if Password != ('Superman'):   # this if statement says 'password enterered DOESNT equal superman' and if that statement is true, triggers the next line
        # print ('Your Password is Incorrect')  # if the above if statement is true, this is triggered.
# print ('Password Correct')  # this one, plays back to the 'while' at the top of this experiment, becasuse by entering 'Superman' as the password, it makes the 'while' statement false,
#thus skipping all the way down to this print command.

# print (Password)



# # # # # JUST PLAYING AROUND 2

# Password2 = 'none'
# while Password2 != ('Superman') and Password2 != ('Bunny') and Password2 != ('Alyx') and Password2 != ('Mr.T'):
    # Password2 = input('Enter Password: ')
    # if Password2 != ('Superman') and Password2 != ('Bunny') and Password2 != ('Alyx') and Password2 != ('Mr.T'):
        # print ('Password Incorrect')
    # if Password2 == ('Superman'):
        # print ('Welcome Sean')
    # if Password2 == ('Bunny'):
        # print ('Welcome, your Highness')
    # if Password2 == ('Alyx'):
        # print ('Welcome Alyxis')
    # if Password2 == ('Mr.T'):
        # print ('Welcome Mr. Sir')


# This one will take some explaining. I wanted to create a unique greeting for the 4 people who could enter their passwords.
# i originally used 'while Password2 != ('Superman') or ('Bunny') or ('Alyx') or ('Mr.T'): - This did NOT work.
# After a bit of googling, i saw i had to be more specific with each condition. I also realized my mistake in using the 'or' instead of the 'and'.



######
############
##################### Date: 10Mar2022
############
######

# # # # # FIZZ BUZZ

fb_num = 0
while (fb_num <= 99):
    fb_num += 1
    if (fb_num % 3 == 0) and (fb_num % 5 == 0):
        print ('%s - Fizzbuzz' %fb_num)
    elif (fb_num % 3 == 0):
        print ('%s - Fizz' %fb_num)
    elif (fb_num % 5 == 0):
        print ('%s - Buzz' %fb_num)
    else:
        print (fb_num)
