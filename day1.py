# ================================================
# Day 1 - User Input, Strings & Type Conversion
# Aerospace Engineer learning Python
# ================================================

# --- GETTING USER INPUT ---
name = input('What is your name? ')
print('Hello, ' + name)
print(f"Hello, {name}")  # f-string method (cleaner)

# --- CLEANING USER INPUT ---
# Problem 1: user may add extra spaces
name = name.strip()         # removes extra spaces

# Problem 2: name may not be capitalised
name = name.capitalize()    # capitalises first letter only
name = name.title()         # capitalises first letter of each word

# Best practice - do it all in one line
name = input('What is your name? ').strip().title()

# --- SPLITTING FIRST AND LAST NAME ---
first, last = name.split(" ")  # splits name into two parts
print(f"Hello, {first}")       # greets user by first name only

# --- TYPE CONVERSION ---
# Input always returns a string, even if user types a number
# So we convert it to an integer before doing math

x = int(input('What is x? '))
y = int(input('What is y? '))

print(x + y)  # now this adds numbers, not joins strings