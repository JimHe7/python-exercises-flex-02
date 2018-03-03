#step 1


secretNum = 5
print ("Yo dawg im thinking of a number between 1 and 10, ya feel")
guess = int(input("What's the digit brah "))

while guess != secretNum:
    print("No man")
    print ("Yo dawg im thinking of a number between 1 and 10, ya feel")
    guess = int(input("What's the digit brah "))
    
    
print("YES! YOU WIN BRAH")


#step 2
secretNum = 5
print ("Yo dawg im thinking of a number between 1 and 10, ya feel")
guess = int(input("What's the digit brah "))

while guess != secretNum:
    
    if guess < secretNum:
        print(guess,"is too low")
    else:
        print(guess,"is too high")
        
    guess = int(input("What's the digit brah "))
    
    
print("YES! YOU WIN BRAH")

#step 3

import random
secretNum= random.randint(1, 10)


print ("Yo dawg im thinking of a number between 1 and 10, ya feel")
guess = int(input("What's the digit brah "))

while guess != secretNum:
    
    if guess < secretNum:
        print(guess,"is too low")
    else:
        print(guess,"is too high")
        
    guess = int(input("What's the digit brah "))
    
    
print("YES! YOU WIN BRAH")



#step 4
import random
secretNum= random.randint(1, 10)
guessLeft = 5

print ("Yo dawg im thinking of a number between 1 and 10, ya feel")
print ("you have",guessLeft,"guesses left.")
guess = int(input("What's the digit brah "))

while guess != secretNum and guessLeft > 1:
    
    if guess < secretNum:
        print(guess,"is too low")
    else:
        print(guess,"is too high")
    guessLeft +=-1
    print ("you have",guessLeft,"guesses left.")    
    guess = int(input("What's the digit brah "))
    
if guess == secretNum:
    print("YES! YOU WIN BRAH")
else:
    print("YOU SUCK LOSER")

#step 5

import random
secretNum= random.randint(1, 10)
guessLeft = 5
again = "Y"

print ("Yo dawg im thinking of a number between 1 and 10, ya feel")
print ("you have",guessLeft,"guesses left.")
guess = int(input("What's the digit brah "))


while again == "Y":
    while guess != secretNum and guessLeft > 1:
    
        if guess < secretNum:
            print(guess,"is too low")
        else:
            print(guess,"is too high")
        guessLeft +=-1
        print ("you have",guessLeft,"guesses left.")    
        guess = int(input("What's the digit brah "))
    
    if guess == secretNum:
        print("YES! YOU WIN BRAH")
    else:
        print("YOU SUCK LOSER")
        
    again = input("do you want to try again? (Y or N)")
    if again == "Y":
        secretNum= random.randint(1, 10)
        guessLeft =5
        print ("Yo dawg im thinking of a number between 1 and 10, ya feel")
        print ("you have",guessLeft,"guesses left.")
        guess = int(input("What's the digit brah "))
        
    else:
        print("Bye")