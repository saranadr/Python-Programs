'''Write a program for number guessing game.
Generate random number between 1 to 10
  Get number as input from the user. 
    If number matches,    MSG: "Congrats! You guessed the number in 3 attempts"
    If number is greater, MSG: "You number is greater than actual number. Please guess lower numbers"
    If number is lower,   MSG: "You number is lower than actual number. Please guess greater numbers"
    if not within range,   MSG: "Invalid number, Please enter number between 1 to 10"
  Input:
    Enter the number between 1 and 10: 5
  Output:
    Congrats! You guessed the number in 3 attempts'''
'''
import random
while 1:
    attempt=0
    rn=random.randrange(1,11)
    while True:
        un=int(input('Enter the number between 1 and 10: '))
        attempt+=1
        if un in range(1,11):
            if un>rn:
                print('You number is greater than actual number. Please guess lower numbers')
            elif un<rn:
                print('You number is lower than actual number. Please guess greater numbers')
            else:
                print('Congrats! You guessed the number in {0} attempts'.format(attempt))
                break
        else:
            print('Invalid number, Please enter number between 1 to 10')
'''  
import random
attempt=0
rn=random.randrange(1,11)
while True:
    un=int(input('Enter the number between 1 and 10: '))
    attempt+=1
    if un not in range(1,11):
        print('Invalid number, Please enter number between 1 to 10')
    elif un>rn:
        print('You number is greater than actual number. Please guess lower numbers')
    elif un<rn:
        print('You number is lower than actual number. Please guess greater numbers')
    else:
        print('Congrats! You guessed the number in {0} attempts'.format(attempt))
        break

        
