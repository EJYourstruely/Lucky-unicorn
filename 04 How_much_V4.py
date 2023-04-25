# Component 2 (How much) V1
# Use Try/accept and pull error message out of the loop

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

# Main routine
user_balance = num_check("How much would you like to play? ", 1, 10)
print(f"You are playing with {user_balance}")
