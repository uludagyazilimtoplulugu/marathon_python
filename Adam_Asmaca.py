import random

def random_words():
    words = ['apple','house','pen','key','eraser','mirror','pizza','clock','telephone']
    return random.choice(words)
    

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    tries = 5
    guessed_letters = []
    word = random_words()
    
    print("Welcome to Hangman")
    

    while tries >= 0:
        current_display = display_word(word, guessed_letters)
        print(f"Word: {current_display}")

        if (word) == (current_display):
            print("Congratulations")
            break

        guess = input("guess a letter: ")
        print(guess)
        if guess in word:
            guessed_letters.append(guess)
            print("true,you got it")
        else:
            print("wrong,try again")
            tries -= 1
    
        if(tries) == 0:
            print("unlucky you lose")

hangman()
