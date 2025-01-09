import random
words = ['computer', 'programmer', 'science', 'technology', 'money', 'laptop', 'monitor', 'iphone', 'airpods']
word = random.choice(words)
lives = 12
correct_guesses = 0
correct_letters = []
guesses = []
print('In this game you will have to guess the word by asking if a letter is in it')
print(f'You have only {lives} lives')
print('Good luck!')
print(word)
while lives > 0 and correct_guesses < len(word): # To make a loop until the total of the lives reaches 0
    guess = str(input('Enter a letter here: ')).lower()
    if guess.isalpha() and len(guess) <= 1 : # To check if the given input is only a letter
        if guess not in word and guess not in guesses :
            lives = lives - 1 # If the user guesses an incorrect letter a life is taken away
            if lives == 0 :
                print('You lost')
            elif lives > 0 :
                print("The letter isn't in the word")
                print(f"You have {lives} lives left")
                guesses.append(guess)  # To make alist of the guesses of the user to then check if an input is repeated
        elif guess not in guesses and guess in word:
            if guess in word:
                correct_guesses += 1
                times = word.count(guess) # To check how many times the entered letter is in the word
                if times > 1 :
                    repetition = str('times') # To change the output to be "times" or "time"
                else :
                    repetition = str('time')
                    print(f"The letter {guess} is in the word {times} {repetition}") # To print ho many times the entered letter is in the word
                    print(f"You have {lives} lives left") # To print how many lives the user has left
                    guesses.append(guess)  # To make a list of the guesses of the user to then check if an input is repeated
                    correct_letters.append(guess)
                    print(f"Correct letters: {correct_letters}")
        else :
            print("You already tried this letter")
            guesses.append(guess)  # To make alist of the guesses of the user to then check if an input is repeated
    else :
        print('Invalid guess')
print(f"You have won!!!!the word was {word}")