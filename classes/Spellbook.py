#---------------------------------------#
#---------- SPELLBOOK CLASS ------------#
#---------------------------------------#

"""The class for the creation of a spellbook for the witch"""

#---------- IMPORTS -----------#

from classes.Spell  import Spell
from debugging      import debug_functions


#---------- CLASS -----------#
class Spellbook:
    """
        This class represents the characteristics of a spellbook.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self, arsenal=None):
        """
        Creates a Spellbook object with information about its contents.

        :param __arsenal    : dict = None      list of spells in the spellbook
        """
        debug_functions.debugClass(self)

        self.set_arsenal(arsenal)


    #------ GETTER & SETTER --------#

    def set_arsenal(self, value: dict or None) -> None:
        """Creates the list of spells that the witch starts off with."""
        if value is not None and type(value) == dict:
            self.__arsenal = value
        else:
            self.__arsenal = {}

    def get_arsenal(self) -> dict:
        """Fetches the arsenal of the spellbook."""
        try:
            return self.__arsenal
        except AttributeError:
            print('ERROR: Failed to get arsenal.')


    # ------ METHODS --------#

    def displayArsenal(self) -> str:
        """Lists all spells in the spellbook."""
        debug_functions.debugMethod(self)
        current_arsenal = '\nYour current arsenal:'
        for spell in self.get_arsenal().values():
            current_arsenal += f"\n\t{spell.get_name()} (Element: {spell.get_element()})"
        return current_arsenal


    def addSpell(self, spell: Spell) -> str:
        """Adds a spell to the spellbook."""
        debug_functions.debugMethod(self)
        try:
            # check if the object is actually a spell
            if isinstance(spell, Spell):

                new_spell = spell.get_name()

                # check if the spellbook already contains the spell
                if len(self.get_arsenal()) > 0 and new_spell not in self.get_arsenal():

                    # add spell if the spell is not yet in the spellbook
                    self.get_arsenal()[new_spell] = spell
                    return f"{new_spell} has been added to your arsenal."
                else:
                    # add spell is the arsenal is empty
                    self.get_arsenal()[new_spell] = spell
                    return f"{new_spell} has been added to your arsenal."
            else:
                print('This is not a spell.')
        except AttributeError:
            print('\nERROR: Spell could not be added.')