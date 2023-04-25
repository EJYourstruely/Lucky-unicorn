"""COmponent 2 (How much) V1
Ask how much they want to play with and check that the input is valid interger between 1 and 10 if it is, this amount
becomes the balance in there account"""

user_balance=int(input("How much money will use to play must be between $1-$10 and is also a whole number"))

#Keep asking until is a valid amount ($1-$10)
while not 1<= user_balance <= 10:
    print("try again, please enter a whole number between 1-10")
    #ask for input
    user_balance= int(input("how much would you like to play with"))

print(f"you are playing with ${user_balance}")