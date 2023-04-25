"""Based on 06_rounds_V2
COnverting V2 into function
"""

import random


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
        elif 6 < number <= 36:
            token = "donkey"
            balance -= 1
        elif number % 2 == 0:
            token = "zebra"
            balance -= 0.5
        else:
            token = "horse"
            balance -= 0.5

        # output token and balance
        print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")

        if balance < 1:
            print("\nSorry but you have run out of money")
            break
        else:
            play_again = input("Do you want to play another round?\n<enter> to play again or 'X' to exit ").lower()

    return balance


# Main routine
starting_balance = 5
closing_balance = generate_token(starting_balance)
print("Thanks for playing!")
print(f"You started with ${starting_balance:.2f} and leave with ${closing_balance:.2f}")
print("Goodbye!")
