"""took components from component 03_v1 as the basis for the new function which
incorporates both yes/no and show instructions"""

#Yes no checker
def yes_no(question_text):
    while True:

        #Ask the user if they have played before
        answer = input(question_text).lower()

        #If they say yes,  output 'program continues'
        if answer == "yes" or answer =="y":
            answer= "Yes"
            return answer

        # if they say no, output 'Display instructions'
        elif answer== "no" or answer=="n":
            answer ="No"
            return answer

        #Otherwise- show error
        else:
            print("please answer yes or no")

#function to display instructions
def instructions():
    print("**** How To PLay ****")
    print()
    print("THe rules of the game will go here")
    print()
    print("program continues")
    print()

#Main routine go here...
played_before= yes_no("have you plated before")

if played_before== "No":
    instructions()