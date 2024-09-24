import random

r = random.randint(1,100)

def game(rand, guesses):
    while True:
        if (guesses <=8 ):
            user_guess = int(input(f"Enter guess {str(guesses)}: "))
            if (user_guess<r):
                print("Guess a higher number")
                guesses +=1
                continue
            elif(user_guess>r):
                print("Guess a lower number")
                guesses +=1
                continue
            else:
                print(f"You've Guessed the correct number - {str(rand)} in {str(guesses)} guesses")
                game_start()
                break
        else:
            print("Oh! Its seems you've used all the eight guesses :(")
            print("The number was", r)
            game_start()
        

def game_start():

    start = input("Do you wanna play the game (y/n): ")
    if(start=="y"):
        game(r, 1)
    else:
        print("Sorry to see you go :(")
        quit()

print("Welcome to the game! In this game you have to guess a number between 0-100, you will get 8 guesses.")
game_start()