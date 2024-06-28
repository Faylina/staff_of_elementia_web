#---------------------------------------#
#------------ GRID CLASS ---------------#
#---------------------------------------#

"""The class for the creation of the grid of the forest."""

#---------- IMPORTS -----------#
from debugging    import debug_functions
from classes.Cell import Cell


#---------- CLASS -----------#
class Grid:
    """
        This class represents the grid of the forest.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, grid=None):
        """
        Creates a Grid object with a list of all cells in the grid.

        :param __grid           :dict   = None      a collection of all Cells in the grid of this world
        """
        debug_functions.debugClass(self)

        self.set_grid(grid)


    # ------ GETTER & SETTER --------#

    def set_grid(self, value) -> None:
        """Creates the grid that the game starts off with."""
        if value is not None and type(value) is dict:
            self.__grid = value
        else:
            self.__grid = {}

    def get_grid(self) -> dict:
        """Fetches the grid of the forest."""
        try:
            return self.__grid
        except AttributeError:
            print('ERROR: Failed to get the grid.')


    # ------ METHODS --------#
    def displayGrid(self) -> str:
        """Lists all cells in the grid."""
        debug_functions.debugMethod(self)

        current_grid = '\nYour current grid:'
        for cell in self.get_grid().values():
            current_grid += f"\n\t{cell.get_coordinates()}: {cell.describeEnvironment()}"
        return current_grid

    def addCell(self, cell: Cell) -> str:
        """Adds a cell to the grid."""
        debug_functions.debugMethod(self)

        try:
            # check if the object is actually a cell
            if isinstance(cell, Cell):

                new_cell = cell.get_coordinates()

                # check if the grid already contains the cell
                if len(self.get_grid()) > 0 and new_cell in self.get_grid():
                    return f"The cell with the coordinates {new_cell} is already in the grid."
                else:
                    self.get_grid()[new_cell] = cell
                    return f"The cell with the coordinates {new_cell} has been added to your grid."
            else:
                print('This is not a cell.')
        except AttributeError:
            print('\nERROR Attribute : Cell could not be added.')
