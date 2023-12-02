import random
from colorama import Fore,Back,Style


print("Welcome to Wordle Unlimited By Jason and Omar")
word_file = open('sgb-words.txt', 'r') # Accessing txt file with all 5 letter words

with open('sgb-words.txt', 'r') as word_file:  # Using with statement for better file handling
    words = [line.strip() for line in word_file.readlines()]


keepGoing = True

while keepGoing:
    random_word = random.choice(words)


    print("You will now be prompted to guess the 5 letter word chosen. Get ready!")
    print("_ _ _ _ _")
    guess_counter = 0
    while guess_counter < 6:
        guess_counter += 1
        while True:
            guess = input("Please enter your guess for the word. Remember this must be a 5 letter word that exists in the English Dictionary! This is guess number " + str(guess_counter) + "\n").lower()

        
            if len(guess) != 5:
                print("Your guess must be exactly 5 letters. Try again.")
                continue

            if guess not in words:
                print("Your guess is not a valid English word or not in the list. Try again.")
                continue

            break
        
        if guess == random_word:
            print(Back.GREEN + random_word + Style.RESET_ALL)
            print("You got it")
            break
        elif guess_counter == 6:
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

    again = input("Play again? Put 'y' for yes or anything else for no:\n")        
    if again == 'y':
        keepGoing = True
    else:
        keepGoing = False    


