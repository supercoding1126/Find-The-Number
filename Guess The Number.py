# Find the number
# By SuperCoding
# Python 3.8.5
# Mac os

import random


number = random.randint(0, 101)
guesses = 0


your_guess = int(input('Guess a number between 0 and 101 press [Enter] to exit : '))
guesses += 1

while your_guess != '':
   while your_guess != number:
      if your_guess > number:
         print('Your guess: ',your_guess,' is to high. ')
         guesses += 1
      if your_guess <= number:
         print('Your guess: ',your_guess,'is to low. ')
         guesses += 1

      your_guess = int(input('Guess again:'))



   print('You got it the number was', number, '!! You did: ',guesses,' guesses.')
   
   if guesses < bestscore:
      biggestscore = guesses


   your_guess = int(input('Guess a number between 0 and 101 press [Enter] to exit: '))
   
   number = random.randint(0, 101)

   guesses = 0
