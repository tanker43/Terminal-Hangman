'''
This is a hangman game in console
Zach Grasso
'''
import random


#Will start and come back to main if wanting to play the game.
def main():
    wordList = open("hangman.txt", "r")
    print("Hello welcome to a game of hangman. Are you feeling lucky?")
    lives = int(input("How many tries are you going to need? "))
    play(lives)
#Keeps track of the position in the word the guessing char is and replaces it in fake_word
def replaceLetter(word, char, fake_word):
    position = []
    for n in range(len(word)):
        if word[n] == char:
            position.append(n)
    for x in range(len(position)):
        fake_word[position[x]] = char
    return fake_word
#Is the check to see if the guess was correct or not
def check(fake_word, word, length):
    for i in range(length):
        if word[i] == fake_word[i]:
            continue
        else:
            return False
    return True
#Play for hangman it is messy but works may refine
def play(lives):
    tries = lives
    word = random.choice(open("hangman.txt").readlines())
    length = len(word)-1
    fake_word = ["_"] * length
    guesses = []

    print("I have your word. It is", length, "characters long")

    while tries > 0:
        for i in fake_word:
            print(i, end=" ")
        print("\n") 
        guess = input("Try guessing a letter: ")
        guesses.append(guess)
        print("You have guessed:", guesses)
        if guess not in word:
            tries -= 1
            if tries == 0:
                print("Your out of tries. Consider yourself hung. The word was", word)
                break
            else:
                print("Wrong you have", tries, "left\n")
            
        else:
            replaceLetter(word, guess, fake_word)
            if check(fake_word, word, length) == True:
                print("You win")
                break
                    

    
    playAgain = input("If you wan to play again type yes: ")
    if playAgain == "yes":
        main()

    
wordList.close()    
main()
