# Number-Guessing-game

This project is a Python-based number guessing game designed to enhance my understanding of Python fundamentals such as conditionals, loops, input handling, and working with built-in libraries. The game uses an algorithm to determine the maximum number of guesses a player can have based on a user-defined range.

## Features 
* Python Basics: The game demonstrates fundamental Python syntax, including conditionals (if, else), loops (while), and user input.
* Random Number Generation: Utilizes the random library to generate a random number within a specified range.
* Mathematical Operations: Implements the math library to calculate the maximum number of guesses using the formula:
    ```maximum_number_guesses = math.log2(upper_bound_value - lower_bound_value + 1)```
* Customizable Difficulty: Players define the lower and upper bounds of the range, which affects the difficulty of the game.

## Prerequistes
  * Python 3.x
  * `math` and `random` librairies

## Running the game
1. Clone this repository
   ```
     git clone <repo-url>
    ```
2. Navigate to Project directory
   ```
     cd Number-Guessing-game
   ```
3. Run the game
   ```
   python Number-Guessing-game.py
   ```
