# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
Most of it was difficult for me because i have never coded a class in python. The syntax is very different from java so i had to use ai to help me explain how to write the methods. The hardest method to do was the has won because I knew i could just do 8 if statements to check for a win, but I knew there was probably a faster way so i had to ask chatgpt and it explained a shorter way to do it using a list of tuples.
2. Explain how you would add a computer player to the game.
To add a cpu you could just make a method that checks for any available moves and then the computer chooses that move. It would likely not be a good bot but that is how you could add a computer bot to the game.
3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
You could make a rule based bot, at first it would choose available moves at random. If it has two in a row, place the third move that would allow them to win. If the enemy has two in a row, place the move that blocks them from winning. you would need a function to detect if there are two X's or O's in a row.