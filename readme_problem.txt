I am rephrasing questions so that it will be harder to be found on the web.

Dice game as follows:
A number of 6 sided dices (not necessary a conventional die of value 1 - 6) are listed.

When the dices are chosen, we will simulate 10000 throws.
Each time your number is greater, you get $1 from your opponent.
Conversely, each time your number is smaller, you pay $1 to your opponent.

The problem to solve is to implement a strategy to win money from this game.

Function 1: count_wins(dice1,dice2)
This function takes input of 2 dice (in the form of a list with the numbers on the sides) and calculates all possible
combinations of 2 dice and outputs the counts the number of wins on each die.

Function 2: find_the_best_dice(dices)
This function takes a list of dices and checks whether there is dice (in this list) that is better than all other dices.
Outputs the index of the die which triumph over all other dices in the list and -1 if there is no such die.

Function 3: compute_strategy(dices)
Implement a function that takes a list of dices (possibly more than three) and returns a strategy.
The strategy is a dictionary which tells the player which whether to choose the die fist: (if there is a die which
triumph over all other dice), or to choose second if the wins are in a cyclical order (for example each die win exactly
the same number of die/dice as every other die)

Edit: Yes I know there is a way to avoid double counting numbers. I will come back to this when I have the time.