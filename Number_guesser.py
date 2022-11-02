import random

print("Welcome to my computer quiz!")

while True:

    play = input("Would you like to play a quiz or a game?")

    if play.lower() == "quiz":
        print("Great! Let's play!")
        
        while True:
            FirstAnswer = input("What does 'www' stand for?")
            if FirstAnswer == "World Wide Web":
                print("Correct!")
                break
            else:
                print("Sorry, that's not correct. Try again.")
            
        while True:
            SecondAnswer = input("What state is Area 51 in?")
            if SecondAnswer == "Nevada":
                print("Correct!")
                break
            else:
                print("Sorry, try again")

        while True:
            ThirdAnswer = input("What Gemoetric shape is generally used for stop signs?")
            if ThirdAnswer == "Octagon":
                print("Correct!")
                break
            else:
                print("Sorry, try again")

        while True:
            FourthAnswer = input("How many colors are there in the rainbow?")
            if FourthAnswer == "7":
                print("Correct!")
                break
            else:
                print("Sorry, try again")

        while True:
            FifthAnswer = input("Who is depicted on the 100 dollar bill?")
            if FifthAnswer == "Benjamin Franklin":
                print("Correct!")
                break
            else:
                print("Sorry, try again")

        while True:
            SixthAnswer = input("Who is depicted on the 2 dollar bill?")
            if SixthAnswer == "Thomas Jefferson":
                print("Correct!")
                break
            else:
                print("Sorry, try again")
        
        while True:
            SeventhAnswer = input("True or False - An eggplant is a vegetable?")
            if SeventhAnswer == "True":
                print("Correct!")
                break
            else:
                print("Sorry, try again")

    if play.lower() == "game":
        print("Let's play a game :D")
        num = random.randint(1, 10)

        while True:
            RandomNum = float(input("Choose a number between 1 and 10: \n"))
            if RandomNum == num:
                print("You guessed correct!")
                Question = input("Play again? y/n \n")
                if Question == "y":
                    num = random.randint(1, 10)
                    continue
                elif Question == "n":
                    print("Cya!")
                    break
                else:
                    print("Invalid input. Try again.")


            else: 
                print("Sorry, try again!")


    if play.lower() == "quit":
        print("Thanks for playing!")
        break






   


