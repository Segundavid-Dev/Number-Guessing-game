import math
import random

print("Guessing correctly a number in a max amount of guessing time!!")
print("The compiler will generate a random number between the range(upper bound, lower bound)\n")

lower_bound_value = int(input("Enter a lower bound value:-- "))
upper_bound_values = int(input("Enter a upper bound value:-- "))



maximum_number_guesses = math.log2(upper_bound_values - lower_bound_value + 1) #formular to calculate minimum number of guesses

print(f"maximum number of guesses for the game:-- {math.floor(maximum_number_guesses)}\n")

#Guess number through Random Library
computer_guess = random.randint(lower_bound_value, upper_bound_values)
print(computer_guess)

count = 0 

while True:
    player_guess = int(input("Enter your guess :: "))
    count += 1 #Increment functionality


    if count > maximum_number_guesses:  #Conditional statement to control the amount of player guessing power 
        print("""You've exceeded the minimum amount of guesses, 
                Better luck next time😢""")
        break
  
    if player_guess == computer_guess:  #Conditional statement to check Win and Fail conditions
        print(f"You guessed correctly in {count} try, YOU WIN!!🎉")
        break
    else:
        print("You guessed wrongly, pls try again\n")