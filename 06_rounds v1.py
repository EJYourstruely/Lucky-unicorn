"""Component 4- game mechanics and looping v1
based on 05_token generator_v4 but hard-wired to only allocate donkeys gives
user feedback about number of rounds and maintains balance .
test amount set $5
"""
import random

# Main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT
rounds_played = 0

# Ask the user if they want to play again
play_again = input("Press <Enter> to play... ").lower()
while play_again != "x" and balance > 0:
    # Increase the number of rounds played
    rounds_played += 1

    # Generate a random number between 1 and 100
    token = ""
    token_num = random.randint(6, 36)

    # If the number is between 1 and 5, give the user a unicorn (add $4 to balance)
    if 1 <= token_num <= 5:
        token = "Unicorn"
        balance += 4
    # If the number is between 6 and 36, give the user a donkey (subtract $1 from balance)
    elif 6 <= token_num <= 36:
        token = "Donkey"
        balance -= 1
    # If the number is even, give the user a zebra (subtract $0.5 from balance)
    elif token_num % 2 == 0:
        token = "Zebra"
        balance -= 0.5
    # Otherwise, give the user a horse (subtract $0.5 from balance)
    else:
        token = "Horse"
        balance -= 0.5

    # Output
    print(f"Round {rounds_played}. Token: {token}. Balance: ${balance:.2f}")
    if balance < 1:
        play_again = input("Press <Enter> to play again, or 'X' to quit: ").lower()
        print("\nSorry, you ran out of money!")
        play_again="x"
    else:
        play_again= input("do you want to play another round?\n enter to play again or X to exit ").lower()
        print()


print(("thank you for playing"))
print(f"you started with ${TEST_AMOUNT:.2f}")
print(f"and leave with ${balance:.2f}")
print("cya")