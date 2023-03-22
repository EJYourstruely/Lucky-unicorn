"I am making a gambling game in"


Money=10
if Money!=0:
    play=int(input("would you like to spend $1 to gamble\n"
                  "If yes press 1\n"
                  "if not press 0\n"))
if play==0:
    print(f"You have ${Money}")
if play==1:
    Money-1
    import random
    animal= random.randint(1,4)
    print(animal)
if animal==1:
    print(f"you got a unicorn {Money}")