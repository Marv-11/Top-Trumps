Project Brief: Top Trumps

In this project I have created a small game where players compare stats using Pokemon API, similar to the Top Trumps card game. The basic flow of the games is:

1. You are given a random card with different stats
2. You select one of the card's stats
3. Another random card is selected for your opponent (the computer)
4. The stats of the two cards are compared
5. The player with the stat higher than their opponent wins


How does the code work?
1. Generate a random number between to use as the Pokemon ID number
2. Using the Pokemon API get a Pokemon based on its ID number
3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (★
https://pokeapi.co/)
4. Get a random Pokemon for the player and another for their opponent
5. Ask the user which stat they want to use (id, height or weight)
6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins


Resources: ★ https://hp-api.herokuapp.com/

ENJOY PLAYING THE GAME!!
