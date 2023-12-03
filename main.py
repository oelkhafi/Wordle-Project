import random
from colorama import Fore,Back,Style



print("Welcome to Wordle Unlimited By Jason and Omar")

def main():
    keepGoing = True
    while keepGoing:
        while True:
            choice = input("Which word length would you like to play? Enter 4 for 4 letter words, 5 for five letter words, or 6 for 6 letter words:\n")
            try:
                choice = int(choice)
                if choice not in [4, 5, 6]:
                    print("Sorry, this is not a valid game mode. Please try again")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

       
        word_file = open(str(choice) + '_letter_word.txt', 'r') # Accessing txt file with all 5 letter words
        with open(str(choice) + '_letter_word.txt', 'r') as word_file:  # Using with statement for better file handling
            words = [line.strip() for line in word_file.readlines()]
        gameLogic(choice,words)
        
        again = input("Play again? Put 'y' for yes or anything else for no:\n")        
        if again == 'y':
            keepGoing = True
        else:
            keepGoing = False
            return

def gameLogic(choice,words):
 
        random_word = random.choice(words)


        print("You will now be prompted to guess the " + str(choice) + " letter word chosen. Get ready!")
        print("_ " * choice)
        guess_counter = 0
        while guess_counter < (choice + 1):
            guess_counter += 1
            while True:
                guess = input("Please enter your guess for the word. Remember this must be a "+ str(choice) + " letter word that exists in the English Dictionary! This is guess number " + str(guess_counter) + "\n").lower()

            
                if len(guess) != choice:
                    print("Your guess must be exactly "+ str(choice) + " letters. Try again.")
                    continue

                if guess not in words:
                    print("Your guess is not a valid English word or not in the list. Try again.")
                    continue

                break
            
            if guess == random_word:
                print(Back.GREEN + random_word + Style.RESET_ALL)
                print("You got it")
                break
            elif guess_counter == choice + 1:
                print("Sorry you did not get it!")
                print("The word was", random_word)
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


        return   
main()