import random

validList = ["Rock", "Paper", "Scissors"]
comChoice = random.choice(validList)
userChoice = input("Choose Rock, Paper, or Scissors")

if userChoice in validList:
    if userChoice == "Rock":
        if comChoice == "Scissors":
            print(userChoice + " defeats " + comChoice + ". You win!")
        elif comChoice == "Paper":
            print(comChoice + " defeats " + userChoice + ". You lose!")
        else:
            print(userChoice + " is the same as " + userChoice + ". You tied!")
    elif userChoice == "Paper":
        if comChoice == "Rock":
            print(userChoice + " defeats " + comChoice + ". You win!")
        elif comChoice == "Scissors":
            print(comChoice + " defeats " + userChoice + ". You lose!")
        else: 
            print(userChoice + " is the same as " + userChoice + ". You tied!")
    else:
        if comChoice == "Paper":
            print(userChoice + " defeats " + comChoice + ". You win!")
        elif comChoice == "Rock":
            print(comChoice + " defeats " + userChoice + ". You lose!")
        else:
             print(userChoice + " is the same as " + userChoice + ". You tied!")
else:
    print("Please choose only Rock, Paper, or Scissors!")
