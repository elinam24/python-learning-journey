# Errors Errors Errors 
#Errors are a part of programming. They are inevitable. They are also a part of learning.

# NameError - Call me Abena? Who is Abena, I don't know her
try:
    print(y)
except NameError:  
    print('y is not defined')


#ValueError - Python can only convert strings that lool like number. e.g. "9"
try:
    x = int("nine")
except ValueError:
    print('x is not an integer')

#Syntax error - When you are not speaking the proper language of pyhon
# Incorrect indentation, mission punctautions, misspelling, wrong case, etc