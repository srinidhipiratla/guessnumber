#This Is A Guess The Number Game.
import random

guessesTaken = 0

print('Hi! Wat's Ur Name?')
myName = input()

number = random.randint(1,20)
print('Slayyyy!'+ myName +',Im Thinking Of A Number Between 1 And 20.')

for guessesTaken in range(6):
    print('Take A Guess.')#Four Spaces In Front Of "print"
    guess = input()
    guess = int(guess)
    
    if guess < number:
        print('Ur Guess Is Too Low.')
        
    if guess > number:
        print('Ur Guess Is Too High.')
        
    if guess == number:
        break
        
    
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Noice, ' + myName + '! U Guessed My Number In ' + guessesTaken + ' Guesses!')
    
if guess != number:
    number = str(number)
    print('Nawr. The Number I Was Thinking Of Was ' + number + '.') 
