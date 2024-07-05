#import random module
import random
from english_words import get_english_words_set

#gcide - Words found in GNU Collaborative International Dictionary of English ; exist in file format
#web2 -  list of all possible words

#define a function named hangman
def hangman():
    words_list = list(get_english_words_set(['web2'], lower=True)) 
    loop = int(input("Enter the no of words you want in the list: "))
    word = random.choice(words_list)
    turn = 10
    guess_made = "" #guessed word
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')
    length_of_random_word = len(word)
    print(f"Number of letters to guess is : {length_of_random_word}")
    
    while len(word)>0 :
        guessed_word = ""
        
        for letter in word:
            if letter in guess_made:
                guessed_word += letter
            else:
                guessed_word += "_ "

        #adding the rightly guessed letter in the empty string
        if guessed_word == word:
            print(word)
            print("Hurray!! You did it!!")
            break
            
        print(f"\nGuess the letters in the word: {guessed_word}")
        guess = input()

        #valid entry
        if guess in valid_entry:
            guess_made += guess
        else:
            print("Enter a valid character: ")
            guess = input()

        #hangman condition
        if guess not in word:
            turn -= 1

            if turn == 9 :
                print("You are left with 9 turns")
                print("-------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("         ________|_____  ")
                
            elif turn == 8 :
                print("You are left with 8 turns")
                print("-------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("         ________|_____  ")                 

            elif turn == 7 :
                print("You are left with 7 turns")
                print("-------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("            |    |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("         ________|_____  ")
                
            elif turn == 6 :
                print("You are left with  6 turns")
                print("--------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("            |    |       ")
                print("            O    |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("         ________|_____  ")                 

            elif turn == 5 :
                print("You are left with 5 turns")
                print("-------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("            |    |       ")
                print("            O    |       ")
                print("            |    |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("         ________|_____  ")                 

            elif turn == 4 :
                print("You are left with 4 turns")
                print("-------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("            |    |       ")
                print("            O    |       ")
                print("           /|    |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("         ________|_____  ")                 

            elif turn == 3 :
                print("You are left with 3 turns")
                print("-------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("            |    |       ")
                print("            O    |       ")
                print(r"          /|\   |       ")
                print("                 |       ")
                print("                 |       ")
                print("                 |       ")
                print("         ________|_____  ")                 

            elif turn == 2 :
                print("You are left with 2 turns")
                print("-------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("            |    |       ")
                print("            O    |       ")
                print(r"          /|\   |       ")
                print("            |    |       ")
                print("                 |       ")
                print("                 |       ")
                print("         ________|_____  ")                 

            elif turn == 1 :
                print("You are left with 1 turns!! ")
                print("----------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("            |    |       ")
                print("            O    |       ")
                print(r"          /|\   |       ")
                print("            |    |       ")
                print("           /     |       ")
                print("                 |       ")
                print("         ________|_____  ")

            elif turn == 0 :
                print("Ohh no!! You are left with no turns!! You let a good man die")
                print("------------------------------------------------------------")
                print("            _____        ")
                print("            |    |       ")
                print("            |    |       ")
                print("            |    |       ")
                print("            O    |       ")
                print(r"          /|\   |       ")
                print("            |    |       ")
                print(r"          / \   |       ")
                print("                 |       ")
                print("         ________|_____  ")
                break

print("\nWelcome to Hangman Game!!")
print("-------------------------")
name=input("Enter your name: ")
print(f"\nHello {name}! Hope you will have a good time...\n\nTry to guess the word in less than 10 wrong attempts\n")
hangman()
print(f"\nNice to have you {name}!!")

                    
                    

                
    
































