# Consolidation Project 2: WORD GUESSING GAME   
# 5/1/2023

import random
import time 

def word_guessing_game():
    # connecting the random words file
    chosen_word = ""
    try:
        with open("random_word.txt", "r") as file_connection:
            random_words = file_connection.readlines()
        
        # removing the white space, so that it won't count as a guess 
        random_words_stripped = []
        for word in random_words:
            random_words_stripped.append(word.strip())

        chosen_word = random.choice(random_words).lower().strip()

    except ValueError:
        print("Unable to connect file")
    

    # welcoming user the game + getting number of players
    print("Welcome to the Word Guessing Game!")
    total_players = int(input("How many players: "))

    print("Now choosing word...")
    time.sleep(3)
    print("The word has been chosen. Hint: it has", len(chosen_word), "letters")

    # storing the player letter and word guesses in a dictionary
    player_scores = {player: {"letter_guesses" : 0, "word_guesses" : 0} for player in range(1, total_players + 1)}

    # loop through the players + setting up player turns/switching
    game_over = False
    player = 1

    while not game_over:
        print(f"It is now Player {player}'s turn to guess: ")
        attemps = 3
        guessed_letters = []
        guessed_word = False

        while attemps > 0 and not guessed_word:
            underscore_word = ''
            for letter in chosen_word:
                if letter in guessed_letters:
                    underscore_word += letter
                else:
                    underscore_word += "_"
            print("Guess the word:", ' '.join(underscore_word))
            guess_word_option = input("Would you like to guess the entire word? Enter 'yes' or 'no': ").lower()

            if guess_word_option == 'yes':
                word_guess = input("Guess the entire word: ").lower()
                if word_guess == chosen_word:
                    print("You have guessed the word correctly!!!")
                    guessed_word = True
                    game_over = True
                else:
                    print("Your guess is incorrect. Try again :(")
                    attempts -= 1
                    player_scores[player]["word_guesses"] += 1
                    if attempts == 0:
                        print("You have no more attempts. Try again next time!")
            elif guess_word_option == 'no':
                letter_guess = input("Guess a letter: ").lower()
                if len(letter_guess) == 1:
                    if letter_guess in guessed_letters:
                        print("You have already guessed that letter. Try again.")
                    else:
                        guessed_letters.append(letter_guess)
                        player_scores[player]["letter_guesses"] += 1
                        letter_count = chosen_word.count(letter_guess)
                        print(f"The letter '{letter_guess}' appears {letter_count} times in the word.")
                else:
                    print("Invalid input. Please enter a single letter.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

# what isn't working in the program:
    # players are unable to switch turns
    # players are unable to end the game
            # final score needs to be presented when game ends
    # players need an option to guess the word completely 
    # game needs to track the amount of guesses each player has + same for the word guesses (limited to 3)

# what is working in the program:
    # the guessing process works well

# extra features to add:
    # theme for words in word bank - should program tell the user?
        
# word guessing game test case 
word_guessing_game()
