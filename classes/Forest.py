#---------------------------------------#
#------------ FOREST CLASS -------------#
#---------------------------------------#

"""The class for the creation of the forest."""

#---------- IMPORTS -----------#
from debugging    import debug_functions
from classes.Grid import Grid
from classes.Cell import Cell


#---------- CLASS -----------#
class Forest:
    """
        This class represents the forest of the witch.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, grid_layout=None, position=None, grid=None):
        """
        Creates a Forest object with information about its layout, the witch's current position and a grid
        containing all cells of the forest.

        :param __grid_layout    :str    = None      grid layout of the world (e.g. 3x3)
        :param __position       :list   = None      the current coordinates if the witch (e.g. [2,2])
        :param __grid           :Grid   = None      a collection of all Cells in the grid of this world
        """
        debug_functions.debugClass(self)

        if grid_layout != '' and grid_layout is not None:
            self.set_grid_layout(grid_layout)
        if position != '' and position is not None:
            self.set_position(position)
        if grid != '' and grid is not None:
            self.set_grid(grid)

    # ------ GETTER & SETTER --------#

    # grid_layout
    def set_grid_layout(self, value: str) -> None:
        """Defines the size and layout of the forest."""
        if type(value) is str:
            value = value.strip()

            x = value[0]
            y = value[2]
            size = {'x': x, 'y': y}

            self.__grid_layout = size
        else:
            print('This is not a valid grid layout of the forest.')

    def get_grid_layout(self) -> None or str:
        """Fetches the size and layout of the forest."""
        try:
            return self.__grid_layout
        except AttributeError:
            print('ERROR: Failed to get the grid layout of the forest.')


    # position
    def set_position(self, value: list) -> None:
        """Defines the current coordinates of the witch in the forest."""
        if type(value) is list:
            if type(value[0]) == int and type(value[1]) == int:
                self.__position = value
            else:
                print('Those are not valid coordinates of the forest.')
        else:
            print('Those are not valid coordinates of the forest.')

    def get_position(self) -> None or list:
        """Fetches the current coordinates of the witch in the forest."""
        try:
            return self.__position
        except AttributeError:
            print("ERROR: Failed to get the witch's current coordinates in the forest.")


    # grid
    def set_grid(self, value: Grid) -> None:
        """Defines the grid of the current forest."""
        if isinstance(value, Grid):
            self.__grid = value
        else:
            print('This is not a grid.')

    def get_grid(self) -> Grid:
        """Fetches the grid of the current forest."""
        try:
            return self.__grid
        except AttributeError:
            print('ERROR: Failed to get the grid of the forest.')


    # ------ METHODS --------#

    def enterCell(self) -> str or None:
        """Marks the cell as occupied when the witch enters it."""
        debug_functions.debugMethod(self)

        current_cell = tuple(self.get_position())
        grid_dict = self.get_grid().get_grid()

        if current_cell in grid_dict:
            grid_dict[current_cell].enter()
            return grid_dict[current_cell].describeEnvironment()
        else:
            print('Wrong position.')


    def leaveCell(self) -> None:
        """Marks the cell as not occupied when the witch leaves it."""
        debug_functions.debugMethod(self)

        current_cell = tuple(self.get_position())
        grid_dict = self.get_grid().get_grid()

        if current_cell in grid_dict:
            grid_dict[current_cell].leave()
        else:
            print('Wrong position.')


    @staticmethod
    def createGrid(level: int) -> Grid:
        """Creates a new grid depending on the level."""
        debug_functions.debugProcess('Forest.createGrid()')

        if level == 1:

            # Creating cells
            cells = []
            for i in range(1, 4):
                for j in range(1, 4):
                    # coordinates = None, level = None, content = None, occupied = False, env_descriptions = None
                    cell = Cell((i, j), 1, 'scenery')
                    cells.append(cell)
            # debug
            for cell in cells:
                debug_functions.debugVariable(f'cell{cell.get_coordinates()}.get_coordinates()',
                                              cell.get_coordinates())
            # Creating Grid
            # grid=None
            grid = Grid()
            for cell in cells:
                grid.addCell(cell)

            debug_functions.debugVariable('grid.get_grid()', grid.get_grid())

            return grid

