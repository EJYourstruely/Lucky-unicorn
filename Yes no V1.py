#Ask the user if they have played before
show_instructions= input("Have you played this game before?")

#If they say yes,  output 'program continues'
if show_instructions== "yes":
    print("program continues")

# if they say no, output 'Display instructions'
elif show_instructions== "no":
    print("Display instruction")

#Otherwise- show error
else:
    print("please answer yes or no")
