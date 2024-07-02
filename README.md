# Staff of Elementia
Project written in Python featuring a text-based, object-oriented adventure game. 
This is the web version and runs with Flask and SocketIO.

# ----- Vision for the game ----- #

This is a text-based RPG. The player guides a witch through a forest. The witch explores the forest, together with her 
familiar (if she has one), collects ingredients that she can brew potions with, overcomes obstacles by defending 
against enemies with spells and solving puzzles. Each forest has a level. 
With each level, the size and difficulty of the forest increases. 

The game can be saved and loaded and has a graphic interface.

# ----- Goals ----- #

The goal of the witch is to find the Staff of Elementia at the end of the game after successfully completing all 
available levels.

# ----- Structure ----- #
FILE STRUCTURE
- The root directory contains the main gameplay script and packages for classes, debugging tools and texts.
- Each class has its own script inside the classes directory.
- The texts directory contains more elaborate texts and lists for the gameplay, that have been exported to avoid 
cluttering the main script.
- The debugging directory contains a configuration file, a file with functions for debugging as well as a file for 
the testing of classes.

GAME STRUCTURE
- Since this game is supposed to be object-oriented, most of its functions are contained in its classes and the main 
gameplay script is kept as minimalistic as possible. 
- The Witch class contains, next to its native attributes and methods, also objects of the type Forest, one of the 
Pets, a Pouch and a Spellbook. 
- The Forest class contains a Grid, which is a collection of Cells for a specific level. 
- The Pouch contains a collection of Ingredients and Potions. 
- The Spellbook is a collection of Spells. 
- The Cat and Dog classes that can be imported into the Witch class are children of the parent class Pet. 
Therefore, Pet is an abstract class, since Pet cannot reasonably exist by itself. 
The Witch does not have to have a pet, though.
- The Game class contains the current state of the game.
- The Player class contains the identity of the current player. This will become relevant for the saving and 
loading the game later on.
- Potions can be created by brewing them with Ingredients.
- Spells can be learned by drinking Potions.
- The Witch can also heal and restore herself by drinking Potions or casting Spells.
- The Witch can interact with her Pet at any time during a running game.
- The game can be ended by choosing the corresponding action during a running game.

GAME FLOW
- The game is introduced with its title and a short description of its contents and goal. 
Then the player is asked for confirmation to proceed. The game can end here, if the player chooses so. 
- If the player is willing to play, an identificator is created. This will be necessary for the implementation of 
the game loading feature later on and will be expanded upon. Since this is not implemented yet at this point, 
the player is asked whether to start a new game. The game can end here, if the player chooses so. 
- Since this is the start of a new game, the forest of the first level is created.
- The process of creating the witch character and her pet begins. The player can customize the witch’s name, 
choose whether she should have a pet and customize the pet’s species, name, age, color and sex. 
- The actual game begins now and the player is asked whether they want to enter the forest. If so, 
the witch is placed into her starting position. The game can end here, if the player chooses so. 
- The game loop begins at this point. The player is presented with a menu of actions to choose from. 
Based on the player’s choice, the game reacts. 
- Within the main menu there is a submenu for pet interactions to avoid presenting the player with a too long list 
of actions. 
- The witch can interact with her pet, if she has one - otherwise opening the submenu is not an option.
- The witch can move around and explore the forest. Guardrails are in place preventing her from going off the grid. 
- The witch can cycle through her actions indefinitely, until the player chooses to quit the game. 
This option is included in any of the two menus. 

DEBUGGING TOOLS
- Different functions for debugging have been used in this game to better illustrate the program flow and help 
find potential errors.
- The output of those functions can be toggled on and off by setting the DEBUG constant in the config file to 
either True or False, so the player won’t have to see the output when the game is released out of the development 
stage. 
