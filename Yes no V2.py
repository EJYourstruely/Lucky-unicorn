#Ask the user if they have played before
show_instructions= input("Have you played this game before?").lower()

#If they say yes,  output 'program continues'
if show_instructions== "yes"or show_instructions=="y":
    print("program continues")

# if they say no, output 'Display instructions'
elif show_instructions== "no" or show_instructions=="n":
    print("Display instruction")

#Otherwise- show error
else:
    print("please answer yes or no")
print(f"you entered {show_instructions}")