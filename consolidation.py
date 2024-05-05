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

    # loop through the players + setting up counter 
    for player in range(1, total_players + 1):
        attemps = 3
        letter_guess = 0
        word_guess = 0
        guessed_letters = []
        while (attemps > 0):
            underscore_word = ''
            for letter in chosen_word:
                if (letter in guessed_letters):
                    underscore_word += letter
                else:
                    underscore_word += '_'
            print("Guess:", underscore_word)
    
            # the users guess and attempts 
            player_guess = input("Guess a letter: ").lower()
            # user guess must be 1
            if (player_guess == 1):
                if player_guess in guessed_letters:
                    print("You have already guessed that letter. Try again.")
                    continue
                
                correct_position = 0
                wrong_position = 0
                correct_guess_wrong_position = 0

                for i in range(len(chosen_word)):
                    char = chosen_word[i]
                    if char == player_guess:
                        if underscore_word[i] == "_":
                            correct_position += 1
                        else:
                            wrong_position += 1






# word guessing game test case 
word_guessing_game()