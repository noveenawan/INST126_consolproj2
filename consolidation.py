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
    number_of_players = int(input("How many players: "))
    total_players = number_of_players

    print("Now choosing word...")
    time.sleep(3)
    print("The word has been chosen. Hint: it has", len(chosen_word), "letters")
    



# word guessing game test case 
word_guessing_game()