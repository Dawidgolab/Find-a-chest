# Find-a-Chest Game

## Welcome to the Exciting World of Treasure Hunting!

Are you ready for an adventure like no other? Dive into the captivating realm of the "Find-a-Chest" game, 
a Python-based treasure hunt that will test your luck, strategy, and intuition. 
In this game, you are given the opportunity to uncover hidden treasures and amass points, but beware, your chances are limited!


<br><br><br><br><br><br>


## Gameplay
### Starting Moves: 

* Your treasure-hunting journey begins with 5 moves, and your objective is to make the most of each move.

### Move Forward or Quit: 

* At the start of each turn, you'll have a critical decision to make. Do you wish to move forward in your quest, or will you choose to end the game? The choice is yours to make.

### Discovering Your Fate: 

* Opting to move forward means you will leave your fate in the hands of destiny. A roll of the virtual dice determines your outcome:

### 60% Chance of Finding a Chest: 

* With a 60% probability, you may uncover one of the precious chests hidden in the game.

### 40% Chance of Finding Nothing: 

* Unfortunately, luck may not always be on your side, and you may discover nothing on some of your moves.

### Chest Points: 

* If you're fortunate enough to stumble upon a chest, your score will increase, and the color of the chest will dictate the number of points you earn:

### Green Chest: 

* Uncover a green chest, and you'll receive a rewarding 1000 points.

### Orange Chest: 

* Orange chests are worth 4000 points, a valuable discovery.

### Purple Chest: 

* Purple chests are even more valuable, offering an astonishing 9000 points.

### Gold Chest: 

* The ultimate treasure is the gold chest, adding a remarkable 16000 points to your score.

### Keep an Eye on Your Score:

* As you proceed through your 5 moves, don't forget to keep a close watch on your score. The final tally will be revealed once you've used all your chances.


<br><br><br><br><br><br>


## How to Run the Game
### Prerequisites: 

* Ensure you have Python installed on your local system. If not, you can download and install it from Python's official website.

### Get the Game: 

* Download or clone this repository to your computer.

### Run the Game: 

* Open your terminal and navigate to the game's directory. Execute the game by entering the command python Find-a-Chest.py.


<br><br><br><br><br><br>


# Code description

1.It imports the random module to introduce randomness into the game.

2.myAccount is initialized to keep track of the player's total score.

3.Prize is a list containing two messages:

- "Congratulations! You've found a chest!"
- "Unfortunately, you found nothing."

4.There are four dictionaries, Chest1 to Chest4, each representing a different chest with color and points. These chests have different point values based on their color.

5.Chests is a list that contains the four dictionaries representing the different chests.

6.The game starts with a welcoming message, and the player is informed that they have 5 moves to uncover treasure.

7.The gamerChoice variable is initialized to 1, and there's a while loop that runs while gamerChoice is less than or equal to 5, meaning the player has 5 moves.

8.In each iteration of the loop, it displays the move number using the gamerChoice variable and asks the player if they want to move forward by typing 'yes' or end the game by typing 'no'.

9.If the player chooses to move forward ('yes'), the script simulates the outcome using randomness. It uses the random.choices function to simulate a 60% chance of finding a chest and a 40% chance of finding nothing. The result is stored in stepYesOrNo.

10.If the result is "Congratulations! You've found a chest!", the script simulates the discovery of a chest by using the random.choices function to determine which chest the player found. It displays the color of the chest and adds the points to myAccount.

11.If the player makes more than 5 moves, the script displays the total points scored and the game ends.

12.If the player chooses to end the game ('no'), a goodbye message is displayed, and the loop is terminated.

13.If the player inputs anything other than 'yes' or 'no', an error message is displayed, and the player can try again.
