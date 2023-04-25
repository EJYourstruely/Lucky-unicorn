"""COmponent 2 (How much) V1
Use Try/accept and pull error message out of the loop """

error="please enter a whole number between 1-10]\n"
Valid=False

#Keep asking until a valid amount (1,10) is entered
while not Valid:
    try:
        #ask for amount
        user_balance=int(input("How much money would you like to put in? $"))

        #Check if the amount is too high/low
        if 0 < user_balance<=10:
            print(f"you are playing with ${user_balance}")
            Valid= True
        else:
            print(error)

    except ValueError:
        print(error)