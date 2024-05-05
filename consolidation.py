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
    player_scores = {}
    game_over = False

    while not game_over:
    # loop through the players + setting up player turns/switching
        for player in range(1, total_players + 1):
            player_scores[player] = {"letter_guesses": 0, "word_guesses": 0}
            print(f"It is now Player {player}'s turn to guess: ")
            attemps = 3
            guessed_letters = []
            guessed_word = False

            while (attemps > 0):
                underscore_word = ''
                for letter in chosen_word:
                    if (letter in guessed_letters):
                        underscore_word += letter
                    else:
                        underscore_word += '_'
                print("Guess the word:", ' '.join(underscore_word))
        
                # the users guess and attempts 
                player_guess = input("Guess a letter: ").lower()

                # user guess must be 1
                if (len(player_guess) == 1):
                    if player_guess in guessed_letters:
                        print("You have already guessed that letter. Try again.")
                    
                    else:
                        guessed_letters.append(player_guess)
                        player_scores[player]["letter_guesses"] += 1
                        letter_count = chosen_word.count((player_guess))
                        print(f"The letter '{player_guess}' appears {letter_count} times in the word.")

                elif ((len(player_guess)) == len(chosen_word)):
                    if (player_guess == chosen_word):
                        print("You have guessed the word correctly!!!")
                        guessed_word = True
                        break
                    else:
                        print("You guess is incorrect. Try again :( )")
                        attemps -= 1
                        player_scores[player]["word_guesses"] += 1
                        if attemps == 0:
                            print("You have no more attempts. Try again next time!")
                            break
                else:
                    print("Please re-enter your input.") 
            
            if guessed_word or attemps == 0:
                game_over = True
                break

        
# word guessing game test case 
word_guessing_game()
