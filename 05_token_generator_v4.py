"""COmponent 3  (random tokens) V2
Calculate percentages to ensure the odds favour the house
5% unicorn 30%donkey and the remaining 65% horses/zebra
"""

import random


STARTING_BALANCE=100
balance= STARTING_BALANCE

# Testing loop to generate 20 tokens
for item in range(10):
    number= random.randint(1,100)

    #adjust balance
    # if the random number is between 1 and 5
    #user gets a unicorn(add $4 to balance)
    if 1<= number <=5:
        token = "unicorn"
        balance += 4

    #if the random number is between 6 and 36
    #user gets a donkey (minus %1 from the balance)

    elif 6 <= number <= 36:
        token="donkey"
        balance-=1
    #if not any of the others i t will = horse or zebra
    #(minus $0.5 from balance
    else:
        #if number is even set token to zebra
        if number % 2== 0:
            token= "zebra"
            balance-=0.5
        #otherwise set horse as token
        else:
            token ="horse"
            balance -=.5


    #output
    print(f"Token: {token}, Balance: ${balance:.2f}")


print(f"starting balance =$ {STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")