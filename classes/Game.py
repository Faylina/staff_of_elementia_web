#---------------------------------------#
#------------- GAME CLASS --------------#
#---------------------------------------#

"""The class for the creation of a game"""

#---------- IMPORTS -----------#
from debugging import debug_functions


#---------- CLASS -----------#
class Game:
    """
        This class represents the characteristics of the game.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, level=1, end_of_level=False, game_over=True) :
        """
        Creates a Game object with information about the state of the game.

        :param __level          :int    = 1         current level of the game
        :param __end_of_level   :bool   = False     indicates whether the player has reached the end of a level
        :param __game_over      :bool   = True      indicates whether the game is running
        """
        debug_functions.debugClass(self)

        if level != '' and level is not None:
            self.set_level(level)
        if end_of_level != '' and end_of_level is not None:
            self.set_end_of_level(end_of_level)
        if game_over != '' and game_over is not None:
            self.set_game_over(game_over)


    # ------ GETTER & SETTER --------#

    # level
    def set_level(self, value: int or str) -> None:
        """Defines the level of the game."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the game level must be an integer.')
        else:
            if value < 1:
                print('This is not a valid game level.')
            else:
                self.__level = value

    def get_level(self) -> None or int:
        """Fetches the level of the game."""
        try:
            return self.__level
        except AttributeError:
            print('ERROR: Failed to get game level.')


    # end_of_level
    def set_end_of_level(self, value: bool) -> None:
        """Defines whether the player has reached the end of a level."""
        self.__end_of_level = value

    def get_end_of_level(self) -> None or bool:
        """Indicates whether the player has reached the end of a level."""
        try:
            return self.__end_of_level
        except AttributeError:
            print("ERROR: Failed to get game's level status.")

    # game_over
    def set_game_over(self, value: bool) -> None:
        """Defines whether the game is running."""
        self.__game_over = value

    def get_game_over(self) -> None or bool:
        """Indicates the state of the game."""
        try:
            return self.__game_over
        except AttributeError:
            print("ERROR: Failed to get game's status.")


    # ------ METHODS --------#

    def quitGame(self) -> None:
        """Ends the game."""
        debug_functions.debugMethod(self)
        self.set_game_over(True)

    def startNewGame(self) -> None:
        """Starts the game."""
        debug_functions.debugMethod(self)
        self.set_game_over(False)

    def startNewLevel(self):
        """Starts the next level."""
        debug_functions.debugMethod(self)
        self.set_game_over(False)
        # TODO: write startNewLevel method

    def loadGame(self):
        """Loads a previous game."""
        debug_functions.debugMethod(self)
        # TODO: write loadGame method
