#This Is A Guess The Number Game.
import random

guessesTaken = 0

print('Hello! What Is Your Name?')
myName = input()

number = random.randint(1,20)
print('Well,'+ myName +',I Am Thinking Of A Number Between 1 And 20.')

for guessesTaken in range(6):
    print('Take A Guess.')#Four Spaces In Front Of "print"
    guess = input()
    guess = int(guess)
    
    if guess < number:
        print('Your Guess Is Too Low.')
        
    if guess > number:
        print('Your Guess Is Too High.')
        
    if guess == number:
        break
        
    
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Great Job, ' + myName + '! You Guessed My Number In ' + guessesTaken + ' Guesses!')
    
if guess != number:
    number = str(number)
    print('Nope. The Number I Was Thinking Of Was ' + number + '.') 
