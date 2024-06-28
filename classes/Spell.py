#---------------------------------------#
#---------- SPELL CLASS ----------------#
#---------------------------------------#

"""The class for the creation of all spells"""

#---------- IMPORTS -----------#
from debugging import debug_functions


#---------- CLASS -----------#
class Spell:
    """
        This class represents the characteristics of all spells.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, name=None, description=None, element=None, effect=None, effectiveness=None, cost=None):
        """
        Creates a Spell object with information about its name, description, element,
        effect, effectiveness and cost.

        :param __name           :str    = None      name of the spell
        :param __description    :int    = None      what does the spell do?
        :param __element        :str    = None      the element of the spell
        :param __effect         :str    = None      effect of the spell
        :param __effectiveness  :int    = None      effectiveness of the spell for damage and healing
        :param __cost           :int    = None      cost of the spell
        """
        debug_functions.debugClass(self)

        if name != '' and name is not None:
            self.set_name(name)
        if description != '' and description is not None:
            self.set_description(description)
        if element != '' and element is not None:
            self.set_element(element)
        if effect != '' and effect is not None:
            self.set_effect(effect)
        if effectiveness != '' and effectiveness is not None:
            self.set_effectiveness(effectiveness)
        if cost != '' and cost is not None:
            self.set_cost(cost)


    # ------ GETTER & SETTER --------#

    # name
    def set_name(self, value: str) -> None:
        """Defines the name of the spell and formats it."""
        try:
            value = value.strip().title()
            self.__name = value
        except AttributeError:
            print('This is not a valid spell name.')

    def get_name(self) -> None or str:
        """Fetches the formatted name of the spell."""
        try:
            return self.__name
        except AttributeError:
            print('ERROR: Failed to get the spell name.')

    # description
    def set_description(self, value: str) -> None:
        """Defines the description of the spell."""
        value = value.strip()
        self.__description = value

    def get_description(self) -> None or str:
        """Fetches the description of the spell."""
        try:
            return self.__description
        except AttributeError:
            print('ERROR: Failed to get the spell description.')

    # element
    def set_element(self, value: str) -> None:
        """Defines the element of the spell."""
        value = value.strip().title()
        if value != 'Earth' and value != 'Water' and value != 'Air' and value != 'Fire':
            print('This is not a valid element of a spell.')
        else:
            self.__element = value

    def get_element(self) -> None or str:
        """Fetches the element of the spell."""
        try:
            return self.__element
        except AttributeError:
            print('ERROR: Failed to get element of the spell.')

    # effect
    def set_effect(self, value: str) -> None:
        """Defines the effect of the spell."""
        value = value.strip().lower()
        if value != 'offensive' and value != 'defensive' and value != 'healing':
            print('This is not a valid effect of a spell.')
        else:
            self.__effect = value

    def get_effect(self) -> None or str:
        """Fetches the effect of the spell."""
        try:
            return self.__effect
        except AttributeError:
            print('ERROR: Failed to get effect of the spell.')

    # effectiveness
    def set_effectiveness(self, value: int or str) -> None:
        """Defines the effectiveness of the spell."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the spell effectiveness must be an integer.')
        else:
            if value < 1:
                print('This is not a valid spell effectiveness.')
            else:
                self.__effectiveness = value

    def get_effectiveness(self) -> None or int:
        """Fetches the effectiveness of the spell."""
        try:
            return self.__effectiveness
        except AttributeError:
            print('ERROR: Failed to get effectiveness of the spell.')

    # cost
    def set_cost(self, value: int or str) -> None:
        """Defines the cost of the spell."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the spell cost must be an integer.')
        else:
            if value < 1:
                print('This is not a valid spell cost.')
            else:
                self.__cost = value

    def get_cost(self) -> None or int:
        """Fetches the cost of the spell."""
        try:
            return self.__cost
        except AttributeError:
            print('ERROR: Failed to get cost of the spell.')


    # ------ METHODS --------#

    def checkEffect(self) -> str:
        """Returns a description of the spell's effect."""
        debug_functions.debugMethod(self)
        if self.get_effect() == "offensive":
            return (f"{self.get_name()} uses the element of {self.get_element()} "
                    f"to deal {self.get_effectiveness()} points of damage to the opponent.")
        elif self.get_effect() == "defensive":
            return (f"{self.get_name()} restores {self.get_effectiveness()} health points "
                    f"and defends with the power of {self.get_element()}.")
        elif self.get_effect() == "healing":
            return f"{self.get_name()} restores {self.get_effectiveness()} health points."


