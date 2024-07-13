#---------------------------------------#
#------------ PLAYER CLASS -------------#
#---------------------------------------#

"""The class for the creation of a player of the game."""

#---------- IMPORTS -----------#
from debugging import debug_functions


#---------- CLASS -----------#
class Player:
    """
        This class represents the player of the game.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, name=None):
        """
        Creates a Player object with information about the player's name.

        :param __name      :str       = None    The name of the player of the game
        """
        debug_functions.debugClass(self)

        if name != '' and name is not None:
            self.set_name(name)


    # ------ GETTER & SETTER --------#

    # name
    def set_name(self, value: str) -> None:
        """Defines the name of the player."""
        try:
            value = value.strip().title()
            self.__name = value
        except AttributeError:
            print('This is not a valid name.')

    def get_name(self) -> None or str:
        """Fetches the formatted name of the player."""
        try:
            return self.__name
        except AttributeError:
            print("ERROR: Failed to get the player's name.")


    # ------ METHODS --------#

    def greetPlayer(self) -> str:
        """Greets the player by name."""
        debug_functions.debugMethod(self)

        return f"Greetings, {self.get_name()}!"
