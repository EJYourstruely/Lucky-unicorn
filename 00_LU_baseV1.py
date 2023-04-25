
#function goes here
def yes_no(question_text):
    while True:

        #Ask the user if they have played before
        answer= input("Have you played this game before?").lower()

        #If they say yes,  output 'program continues'
        if answer== "yes"or answer=="y":
            return answer

        # if they say no, output 'Display instructions'
        elif answer== "no" or answer=="n":
           return answer

        #Otherwise- show error
        else:
            print("please answer yes or no")


#function to display instructions
def instructions():
    print("How to play")
    print()
    print("The rules of the game")
    print()
    print("Program continues")

#number checking
def num_check(question, low, high):
    error = "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1,10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # Check if the amount is too high/low
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


#Main routine go here
played_before = yes_no("have you played before")

if played_before== "No":
    instructions()



#ask the user how much they want to play with
user_balance= num_check("how much you want to play with $", 1,10)
print(f"you are playing with {user_balance}")