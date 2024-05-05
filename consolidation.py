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
                if (player_guess == 1):
                    if player_guess in guessed_letters:
                        print("You have already guessed that letter. Try again.")
                        continue
                    
                    # going through each position to see if player guess matches an index of the chosen word
                    correct_position = 0
                    wrong_position = 0
                    correct_guess_wrong_position = 0

                    for i in range(len(chosen_word)):
                        char = chosen_word[i]
                        if char == player_guess:
                            if underscore_word[i] == "_":
                                correct_position += 1
                            else:
                                correct_guess_wrong_position += 1
                    for char in underscore_word:
                        if char == '_':
                            if char != player_guess:
                                wrong_position += 1
                    
                    if correct_position > 0:
                        print(f"The letter {player_guess} is in the correct position {correct_position} times")
                    
                    
                

                            






# word guessing game test case 
word_guessing_game()