

#Function go here...
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



#Main routine go here...
question= yes_no("have you played this game before?")
print(f"you entered {question}")
print()
having_fun= yes_no("have you had fun?")
print(f"you entered {having_fun}")