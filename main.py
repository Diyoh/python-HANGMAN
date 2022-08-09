
import random
import hangman_words
from hangman_words import word_list
import hangman_art
from hangman_art import stages
from hangman_art import logo


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
      
    print(stages[lives])
    
    
    
    #or use this code whiceh has the logo, and other funtionalities to enhance user experience
    
    
    

import random
import hangman_words
from hangman_words import word_list
import hangman_art
from hangman_art import stages
from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"you already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
      print(f"the letter '{guess}' that you chose if not amongst the letters of the mystery word and you lose a life")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
      
    print(stages[lives])

    
    
    #or this
    
    
    import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
