#---------------------------------------#
#------------ CELL CLASS ---------------#
#---------------------------------------#

"""The class for the creation of a cell in the forest's grid."""

#---------- IMPORTS -----------#
from debugging import debug_functions
from texts     import gameplay_snippets


#---------- CLASS -----------#
class Cell:
    """
        This class represents a cell in a forest's grid.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, coordinates=None, level=None, content=None, occupied=False, env_descriptions=None):
        """
        Creates a Cell object with information about its coordinates, level, content, whether the
         witch is currently there and a list of descriptions of all cell's environments.

        :param __coordinates      :tuple    = None    The coordinates of the cell on the grid
        :param __level            :int      = None    level of the world
        :param __content          :str      = None    Content of the Cell (ingredient, enemy, scenery)
        :param __occupied         :bool     = False   True if the witch is in this Cell
        :param __env_descriptions :dict     = None    List of all description of the environment
        """
        debug_functions.debugClass(self)

        if coordinates != '' and coordinates is not None:
            self.set_coordinates(coordinates)
        if level != '' and level is not None:
            self.set_level(level)
        if content != '' and content is not None:
            self.set_content(content)
        if occupied != '' and occupied is not None:
            self.set_occupied(occupied)

        self.set_env_descriptions(env_descriptions)

    # ------ GETTER & SETTER --------#

    # coordinates
    def set_coordinates(self, value: tuple) -> None:
        """Defines the coordinates of the cell on the grid."""
        if type(value) is tuple:
            if type(value[0]) == int and type(value[1]) == int:
                self.__coordinates = value
            else:
                print('Those are not valid coordinates for a cell.')
        else:
            print('Those are not valid coordinates for a cell.')

    def get_coordinates(self) -> None or tuple:
        """Fetches the coordinates of the cell."""
        try:
            return self.__coordinates
        except AttributeError:
            print('ERROR: Failed to get cell coordinates.')


    # level
    def set_level(self, value: int or str) -> None:
        """Defines the world level of the cell."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the cell level must be an integer.')
        else:
            if value < 1:
                print('This is not a valid cell level.')
            else:
                self.__level = value

    def get_level(self) -> None or int:
        """Fetches the world level of the cell."""
        try:
            return self.__level
        except AttributeError:
            print('ERROR: Failed to get cell level.')


    # content
    def set_content(self, value: str) -> None:
        """Defines what the witch will encounter in the cell."""
        value = value.strip().lower()
        if value != 'ingredient' and value != 'enemy' and value != 'scenery':
            print('This is not a valid content for the cell.')
        else:
            self.__content = value

    def get_content(self) -> None or str:
        """Fetches the content of the cell."""
        try:
            return self.__content
        except AttributeError:
            print('ERROR: Failed to get content of the cell.')


    # occupied
    def set_occupied(self, value: bool) -> None:
        """Defines whether the witch is in this cell."""
        self.__occupied = value

    def get_occupied(self) -> None or bool:
        """Indicates whether the witch is in the cell."""
        try:
            return self.__occupied
        except AttributeError:
            print("ERROR: Failed to get cell's occupied status.")


    # environment descriptions
    def set_env_descriptions(self, value) -> None:
        """Creates a list of possible descriptions for a cell's environment."""

        if value is not None and type(value) is dict:
            self.__env_descriptions = value
        else:
            self.__env_descriptions = gameplay_snippets.level1_descriptions

    def get_env_descriptions(self) -> dict:
        """Fetches the list of the cell environment descriptions."""
        try:
            return self.__env_descriptions
        except AttributeError:
            print('ERROR: Failed to get environment descriptions.')

    # ------ METHODS --------#

    def enter(self) -> None:
        """Marks the cell as occupied when the witch enters it."""
        debug_functions.debugMethod(self)
        self.set_occupied(True)

    def leave(self) -> None:
        """Marks the cell as not occupied when the witch leaves it."""
        debug_functions.debugMethod(self)
        self.set_occupied(False)

    def describeEnvironment(self) -> str:
        """Describes the environment of the current cell."""
        debug_functions.debugMethod(self)

        current_coordinates = f"{self.get_coordinates()[0]}x{self.get_coordinates()[1]}"

        # pick the right description from the list according to the coordinates of this cell
        if current_coordinates in self.get_env_descriptions():
            return self.get_env_descriptions()[current_coordinates]
        else:
            return 'There is no description for this cell.'
