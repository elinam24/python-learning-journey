# Combined lessons of list, functions, strings, ...
# Learnt how to create a letter structure

def main():                                      # A function main
    names = ["Denzel", "William", "Alexander"]   # list of names of receivers
    for name in names:
        print(letter(name, "Julius Annan"))      # two arguments for function letter

def letter(receiver, sender):                    # Function letter with two areguments  
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+    # Letter write-up
    Subject: Letter of Promotion                  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Dear {receiver},

    I am honored to send in my request of the 
    office of the Managing Director.
    With my qualification and level of commitment over
    the years, I have proven to be the right fit for
    this position.
    Thank you so much for your time and consideration
    on my request.
    
    Yours Sincerely,
    {sender}
    """

main()                                         # function call

#