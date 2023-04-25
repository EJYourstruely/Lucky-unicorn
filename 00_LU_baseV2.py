import random
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

def generate_token(balance):
    rounds_played = 0
    play_again = ""

    # Testing loop to generate tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
        number = random.randint(1, 100)

        # adjust balance based on token type
        if 1 < number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("!", "congratulations you got a unicorn"))
            print()
        elif 6 < number <= 36:
            token = "donkey"
            balance -= 1
            print(formatter("?", " you got a donkey"))
        elif number % 2 == 0:
            token = "zebra"
            balance -= 0.5
            print(formatter("%", "you got a zebra"))
        else:
            token = "horse"
            balance -= 0.5
            print(formatter("?", "you got a horse"))

        # output token and balance
        print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")

        if balance < 1:
            print("\nSorry but you have run out of money")
            break
        else:
            play_again = input("Do you want to play another round?\n<enter> to play again or 'X' to exit ").lower()

    return balance

def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


#Main routine go here
print(formatter("-","welcome to lucky unicorn"))
print()
played_before = yes_no("have you played before")

if played_before== "No":
    instructions()



#ask the user how much they want to play with
starting_balance= num_check("how much you want to play with $", 1,10)


print(f"you are playing with {starting_balance}")
closing_balance = generate_token(starting_balance)
print("Thanks for playing!")
print(f"You started with ${starting_balance:.2f} and leave with ${closing_balance:.2f}")
print(formatter("*", "Goodbye"))
