# ================================================
# Day 2 - Functions, Dictionaries & Conditionals
# Aerospace Engineer learning Python
# ================================================

# --- FUNCTIONS ---
# A function is a reusable block of code you define once and call anytime

def hello():
    print('Hello')

def greet():
    name = input('What is your name? ')
    hello()        # calling another function inside a function
    print(name)

greet()            # calling the function to run it

# --- FUNCTIONS WITH RETURN VALUES ---
# Functions can take inputs and send back a result

def squared(n):
    return pow(n, 2)   # returns n to the power of 2

def calculate():
    x = int(input('What is x? '))
    print('x squared is', squared(x))

calculate()

# --- LISTS ---
# A list stores multiple items in one variable

family = ["Elinam", "Kekeli", "Naa"]
school = ["CS50", "KNUST", "Kotoka"]

# --- DICTIONARIES ---
# A dictionary links a key to a value (like a real dictionary links a word to its meaning)
# Format: key : value

family = {
    "Elinam": "CS50",
    "Kekeli": "KNUST",
    "Naa": "Kotoka"
}

for f in family:
    print(f, family[f], sep=" - ")

# --- LIST OF DICTIONARIES ---
# More powerful — each item in the list is its own dictionary

family = [
    {"name": "Elinam",  "school": "CS50",   "programme": "Python programming"},
    {"name": "Kekeli",  "school": "KNUST",  "programme": "Fashion design"},
    {"name": "Naa",     "school": "Kotoka", "programme": "Surgeon"}
]

for f in family:
    print(f["name"], f["school"], f["programme"])

# --- CONDITIONALS ---
# Making decisions in code based on conditions

x = int(input('What is x? '))
y = int(input('What is y? '))

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x is equal to y')

# Combining conditions with OR
if x < y or x > y:
    print('x is not equal to y')

# Shorthand using != (not equal to)
if x != y:
    print('x is not equal to y')