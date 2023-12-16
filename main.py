import random
from colorama import Fore,Back,Style
import time
import os

print("Welcome to...")
time.sleep(2)
print("""
 __      __            .__       .___.__            ____ ___      .__  .__        .__  __             .___
/  \    /  \___________|  |    __| _/|  |   ____   |    |   \____ |  | |__| _____ |__|/  |_  ____   __| _/
\   \/\/   /  _ \_  __ \  |   / __ | |  | _/ __ \  |    |   /    \|  | |  |/     \|  \   __\/ __ \ / __ | 
 \        (  <_> )  | \/  |__/ /_/ | |  |_\  ___/  |    |  /   |  \  |_|  |  Y Y  \  ||  | \  ___// /_/ | 
  \__/\  / \____/|__|  |____/\____ | |____/\___  > |______/|___|  /____/__|__|_|  /__||__|  \___  >____ | 
       \/                         \/           \/               \/              \/              \/     \/ 
      """)
time.sleep(2)
print("by Omar Elkhafif and Jason McCauley")
time.sleep(1)

def main():
    keepGoing = True
    while keepGoing:
        while True:
            choice = input("Which word length would you like to play? Enter the corresponding number.\n (4) Four Letter Words\n (5) Five Letter Words\n (6) Six Letter Words\n")
            try:
                choice = int(choice)
                if choice not in [4, 5, 6]:
                    print("Sorry, the number you entered is not a valid game mode. Please try again.")
                    time.sleep(2)
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
                time.sleep(2)

        word_file = open(str(choice) + '_letter_word.txt', 'r') # accessing txt file with all 'choice' letter words
        with open(str(choice) + '_letter_word.txt', 'r') as word_file:  # using with statement for better file handling
            words = [line.strip() for line in word_file.readlines()]
        random_word = random.choice(words) #generating random word from the accessed file

        while True:
            multiplayer = input("Would you like to play local multiplayer?\n (y) Yes\n (n) No\n")
            if multiplayer == 'y':
                print("Player one, get ready. It's your turn!")
                time.sleep(2)
                player1_counter = gameLogic(choice, words, random_word)
                time.sleep(2)
                os.system('cls')

                print("Player two, get ready. It's now your turn!")
                time.sleep(2)
                player2_counter = gameLogic(choice, words, random_word)
                
                # Checking for Winner!
                if player1_counter > player2_counter and player2_counter:
                    print("Player 2 guessed the word in less attempts!")
                elif player2_counter > player1_counter and player1_counter:
                    print("Player 1 guessed the word in less attempts!")
                elif player1_counter == 8 and player2_counter == 8: # a counter value of 8 means the word wasn't guessed
                    print("Neither of you guessed the word correctly!")
                else:
                    print("You both guessed it in the same amount of tries!!")
                break
            elif multiplayer == 'n':
                gameLogic(choice, words, random_word)
                break
            else:
                print("Please enter a valid choice.")
                time.sleep(2)
                continue
    
        while True:
            again = input("Would you like to play again?\n (y) Yes\n (n) No\n")        
            if again == 'y':
                keepGoing = True
                break
            elif again == 'n':
                keepGoing = False
                print("Thanks for playing!")
                break
            else:
                print("Please enter a valid choice.")
                time.sleep(2)
                continue

def gameLogic(choice, words, random_word):
        print("You will now be prompted to guess the chosen " + str(choice) + " letter word. Good luck!")
        print("_ " * choice)
        guess_counter = 0
        time.sleep(3)
        print("Please enter your guess for the word. Remember this must be a "+ str(choice) + " letter word that exists in the English Dictionary.")
        time.sleep(2)

        while guess_counter < (choice + 1):
            guess_counter += 1
            while True:
                guess = input("This is guess number " + str(guess_counter) + ".\n").lower()
 
                if len(guess) != choice:
                    print("Remember, your guess must be exactly "+ str(choice) + " letters. Please try again.")
                    continue

                if guess not in words:
                    print("Your guess is either not a valid English word or not in the list. Please try again.")
                    continue
                break
            
            if guess == random_word:
                print(Back.GREEN + random_word + Style.RESET_ALL)
                print("Congratulations! You correctly guessed the word!")
                time.sleep(2)
                break
            elif guess_counter == choice + 1:
                print("Sorry, you did not guess the word in time!")
                time.sleep(2)
                print('The word was "' + str(random_word) + '".')
                time.sleep(2)
                guess_counter = 8 # Placeholder guess counter value for not guessing the word
                break
            else:
                modified_guess = []
                matched_indices = set()
                for i, letter in enumerate(guess):
                    if letter == random_word[i]:
                        modified_guess.append(Back.GREEN + letter + Style.RESET_ALL)
                        matched_indices.add(i)
                    else:
                        modified_guess.append(None)  # Placeholder for second pass

                # Second pass for yellow matches
                for i, letter in enumerate(guess):
                    if modified_guess[i] is None:  # Check only non-green letters
                        found = False
                        for j in range(len(random_word)):
                            if letter == random_word[j] and j not in matched_indices:
                                modified_guess[i] = Back.YELLOW + letter + Style.RESET_ALL
                                matched_indices.add(j)
                                found = True
                                break
                        if not found:
                            modified_guess[i] = letter

                modified_guess_str = ''.join(modified_guess)
                print(modified_guess_str)

        return  guess_counter 
main()