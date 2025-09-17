import random
computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice Snake, Water or Gun ? : ")
youLower = youStr.lower()[0]

if not (youLower== "s" or youLower == "w" or youLower == "g"):
    print ("Error Please try again !!")

else:
    youDict = {"s": 1, "w": -1, "g": 0}
    you = youDict[youLower]
    compDict = {1: "Snake", -1: "Water", 0: "Gun"}
    comp = compDict[computer]

    print(f"You chose \033[1m{compDict[you]} \033[0m and Computer chose \033[1m{comp} \033[0m!")

    if computer == you:
        print("That's a draw!")
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You lose!")
    else:
        print("something went wrong !! please try again")

    #Alternative method:
    # if (computer == you):
    #
    #     print("That's a draw!")
    # elif (computer - you) == -1 or (computer - you == 2):
    #     print("You Lose!")
    # else:
    #     print("You Win!")
