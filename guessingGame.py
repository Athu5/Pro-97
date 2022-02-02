guess = (input("guess a number between (1 to 9) : "))
guess = int(guess)
chances = 0
number = 5
    
    

while guess!=number and chances<5:
    
    guess = input(" Enter your guess:- ")
    guess = int(guess)
    chances += 1

    if (guess>number):
        print("the number you typed is higher: the number is lower than",guess)
    
    if (guess<number):
        print("the number you typed is too low: the number is higher than",guess)

  
    if (guess>number):
        print("the number you typed is higher: the number is lower than",guess)

    if guess == number:
        print("Congratulation YOU WON ! ! !")



    