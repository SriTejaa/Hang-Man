import random
import time
group = ('1','2','3','4')
print("WELCOME TO HANGMAN!")
while True:
     print()
     print('**MENU**')
     print('1: fruits')
     print('2: vegetables')
     print('3: countries')
     print('4: cities')
    
     print()
     
     choose=int(input('enter your option:'))
     print(choose)
    
     if True:
        break
    
     else:
        print()
        print('option is not available')
        
        if choose == '1':
            fruits = ["apple", "banana", "grape", "orange", "mango"]
            choosenWord = random.choice(fruits)
            #choosenWord = apple
        elif choose == '2':
            vegetables = ["bringal","tomato","carrot","radish","capsicum"]
            choosenWord = random.choice(vegetables)
        elif choose == '3':
            countries = ["china","france","mexico","finland","nigeria"]
            choosenWord = random.choice(countries)
        else :
            cities = ["kolkata","mumbai","hyderabad","delhi","chennai"]
            choosenWord = random.choice(cities)
guessing = set()
tries = 6
while tries > 0:
    display = "".join(letter if letter in guessing else " _" for letter in choosenWord)  #apple
    print("Word:", display)

    if " _" not in display:  
        print("Congratulations! You guessed the word:", guessing)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessing:
        print("You already guessed that letter.")
        continue

    guessing.add(guess)

    if guess not in group:
        tries -= 1
        print("Wrong guess! Tries left:",tries)

if tries == 0:
    print("Game Over! The word was:", group)