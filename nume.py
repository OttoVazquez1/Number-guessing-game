import random

#Generate a random 4 digit number to guess.
x = random.randint(1000,9999)

#Number of tries.
tries = 10

#Print name of the game
print(".__   __.  __    __  .___  ___.  _______ ")
print("|  \ |  | |  |  |  | |   \/   | |   ____|")
print("|   \|  | |  |  |  | |  \  /  | |  |__   ")
print("|  . `  | |  |  |  | |  |\/|  | |   __| ")
print("|  |\   | |  `--'  | |  |  |  | |  |____ ")
print("|__| \__|  \______/  |__|  |__| |_______|")

print(" ")
try:
    while tries > 0:
        #Asking the user to enter a guess.
        guess = input("Try your luck! Enter a 4 digit number: ")
    
        #Cheking if is a 4 digit number.
        if not guess.isdigit() or len(guess) != 4:
            print("Invalid input, i told you it whas 4 digit only!! Try again")
            continue
        
        #Leave a space for easier reading
        print(" ")

        #Convert the guess into a list
        guess_list = [int(digit) for digit in guess]
    
        #If the user guesses, the game ends.
        if guess == str(x):
            print("The motherf*cka did it. You are amaizing, i mean, HOW!? JUST HOW DID YOU DO IT!?")
            break

        #Create a correct guess list, so that we can inform the user of this
        correct_guesses = []
        #Incorrect position guesses
        incorrect_guess= []

        #Check for digits in the correct position
    
        #**********MATHEMATICAL WAY***********
        #for i in range(4):
            #if guess_list[i] == x // 10**(3-i) % 10:
                #correct_guesses.append(guess_list[i])
        
        #***********STRING WAY***************
        for i, digit in enumerate(str(x)):
            if int(digit) == guess_list[i]:
                correct_guesses.append(int(digit))
        
        #Check for numbers in the incorrect position
        for numbers in guess_list:
            if numbers in correct_guesses:
                continue
            if str(numbers) in str(x):
                incorrect_guess.append(numbers)


        if incorrect_guess:
            print("Almost! There are " + str(len(incorrect_guess)) + " numbers in an incorrect position. Come on!")
        if correct_guesses:
            print("You are getting closer! You've got " + str(len(correct_guesses)) + " correct. Keep it up!")
        else:
            print("You didn't get a single one right? Try again")
        #Lower the number of tries every loop.
        tries -= 1

        #End the game if the number of tries reaches zero.
        if tries == 0:
            print("You coudn't do it. I told you it was hard and you didn't listen. I mean, you could always try again i guess. The number was " + str(x) + " btw.") 
        
        #Leave a space for aesthetic pourposes 
        print(" ")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(" ")
except:
    print("Goodbye!")



