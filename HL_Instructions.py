# functions go here
def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    print("""
***** Instructions *****
To win Higher or Lower you need to guess the correct number.

Input a number between 1-(and your choice) and I'll tell you 
if it's higher or lower than the number you inputted 😊

But look out! You only have 5 guesses! 
    """)


# Main routine
print()
print("⬆️⬆️⬆️ Welcome to the Higher Lower Game 🔽🔽🔽")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the usr wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")