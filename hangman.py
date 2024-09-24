import random

def hangman():
    words_list = ["apple", "pineapple", "grapes", "kiwi", "mango", "orange", "chickoo", "banana", "papaya"]

    random_word = random.choice(words_list)
    word = ["_"]* len(random_word)
    attempts = 6
    correct_attempts = 0
    guessed_letters = set()


    while attempts>0 and "_" in word:
        print("Word to guess", "".join(word))
        print("\nattempts left", (attempts))
        print("\nletters guessed till now:", "".join(sorted(guessed_letters)))
        correct_attempts +=1

        guess = input("\nGuess a letter: ").lower()
        if guess in guessed_letters:
            print("\nYou have already guessed the letter, please guess a different letter\n")
            print("--------------------------")
        elif guess in random_word:
            print("\nYou guessed the correct word\n")
            print("--------------------------")
            for index, letter in enumerate(random_word):
                if letter == guess:
                    word[index] = guess
        else:
            attempts-=1
            print("\nYou guessed incorrect letter\n")
            print("--------------------------")
        guessed_letters.add(guess)

    if "_" not in word:
        print(""+random_word)
        print("Congratulations you guessed the full word", random_word, f"in total {str(correct_attempts)} guesses")
        start()
    else:
        print("You\'ve run out of attempts, the word was", random_word)
        start()

def start():
    print("Welcome to Hangman game, here you will have to guess letters of a word")
    print("The word will be from fruits name")
    play = input("Do you wanna play the game (y/n): ")
    if play.lower() == "y" or play == "yes":
        hangman()
    else:
        print("Sorry to see you go :(")
        quit()

start()