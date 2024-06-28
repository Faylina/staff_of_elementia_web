#---------------------------------------#
#------------ POUCH CLASS --------------#
#---------------------------------------#

"""The class for the creation of a pouch for the witch"""

#---------- IMPORTS -----------#

from classes.Ingredient import Ingredient
from classes.Potion     import Potion
from debugging          import debug_functions


#---------- CLASS -----------#
class Pouch:
    """
        This class represents the characteristics of a pouch.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self, inventory=None):
        """
        Creates a Pouch object with information about its contents.

        :param __inventory  :dict = None      list of ingredients in the pouch
        """
        debug_functions.debugClass(self)

        self.set_inventory(inventory)


    #------ GETTER & SETTER --------#

    def set_inventory(self, value) -> None:
        """Creates the pouch that the witch starts off with."""
        if value is not None and type(value) == dict:
            self.__inventory = value
        else:
            self.__inventory = {}

    def get_inventory(self) -> dict:
        """Fetches the inventory of the pouch."""
        try:
            return self.__inventory
        except AttributeError:
            print('ERROR: Failed to get inventory.')


    # ------ METHODS --------#

    def displayInventory(self) -> str:
        """Lists all ingredients in the pouch with their respective amounts."""
        debug_functions.debugMethod(self)

        current_inventory = '\nYour current inventory:'
        for item in self.get_inventory().values():
            current_inventory += f"\n\t{item.get_amount()}x {item.get_name()}"
        return current_inventory


    def addItem(self, item: Ingredient or Potion) -> str:
        """Adds an item to the pouch."""
        debug_functions.debugMethod(self)

        try:
            # check if the object is actually an ingredient or potion
            if isinstance(item, Ingredient) or isinstance(item, Potion):

                new_item = item.get_name()

                # check if the pouch already contains the item
                if len(self.get_inventory()) > 0 and new_item in self.get_inventory():
                    inventory_item = self.get_inventory()[item.get_name()]

                    # increase the amount
                    current_amount = inventory_item.get_amount()
                    inventory_item.set_amount(current_amount + item.get_amount())
                    return f"You have one more of {new_item} now."

                else:
                    self.get_inventory()[new_item] = item
                    return f"{new_item} has been added to your inventory."
            else:
                print('This is not an ingredient nor a potion.')
        except AttributeError:
            print('\nERROR Attribute : Item could not be added.')


    def removeItem(self, item: Ingredient or Potion, amount: int = 1) -> str:
        """Removes an item from the pouch."""
        debug_functions.debugMethod(self)

        # check if the amount that is supposed to be removed is valid
        try:
            amount = int(amount)
        except TypeError:
            print('The format of the amount to be deleted must be an integer.')
        else:
            if amount < 1:
                print('This is not a valid amount.')
            else:

                # removing the item
                try:
                    # check if the object is actually an ingredient
                    if isinstance(item, Ingredient) or isinstance(item, Potion):

                        item_to_remove = item.get_name()

                        # check if the pouch already contains the item
                        if len(self.get_inventory()) > 0 and item_to_remove in self.get_inventory():
                            inventory_item = self.get_inventory()[item_to_remove]

                            # decrease the amount
                            current_amount = inventory_item.get_amount()
                            inventory_item.set_amount(current_amount - amount)

                            # remove the item if the amount has become 0
                            if inventory_item.get_amount() == 0:
                                del self.get_inventory()[item_to_remove]
                                return f"{item_to_remove} has been removed from your inventory."
                            else:
                                return f"You have one {item_to_remove} less now."
                        else:
                            print('You do not own this item.')
                    else:
                        print('This is not an ingredient nor a potion.')
                except AttributeError:
                    print('\nERROR: Item could not be removed.')

