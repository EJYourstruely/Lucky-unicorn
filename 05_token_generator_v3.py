"""COmponent 3  (random tokens) V2
Calculate user balance based on random selection of tokens"""

import random

tokens = ["unicorn",
"horses","horses","horses",
"donkey", "donkey", "donkey",
"zebra", "zebra", "zebra"]


STARTING_BALANCE=100
balance= STARTING_BALANCE

# Testing loop to generate 20 tokens
for item in range(100):
    token = random.choice(tokens)

    #adjust balance
    if token == "unicorn":
        balance+= 4
    elif token == "donkey":
        balance-= 1
    else:
        balance-=.50

#output
print(f"starting balance =$ {STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")