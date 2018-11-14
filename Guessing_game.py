''' Developer: Jason Poitras
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''


from random import randint

#computer random guess
cpu_number = randint (1,10)
guess = 0
count = 0

# while guess does not equal number and does not want to exit game
while guess != cpu_number and guess != "exit":
    guess = input("Please enter a guess betwee 1-10 and exit to end: ")
#if wants to exit, break   
    if guess == "exit":
        break

    guess = int(guess)
    count +=1
    
#logic for too low, high or good guess
    if guess < cpu_number:
        print("Too low, try again")
    elif guess > cpu_number:
        print ("Too high, try again")
    else:
        print ("You got it")
        print ("It only took you" ,count, "tries")
