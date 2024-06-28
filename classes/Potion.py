#---------------------------------------#
#---------- POTION CLASS ---------------#
#---------------------------------------#

"""The class for the creation of all potions."""

#---------- IMPORTS -----------#
from debugging import debug_functions


#---------- CLASS -----------#
class Potion:
    """
        This class represents the characteristics of all potions.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, name=None, description=None, effect=None, effectiveness=None, element=None, amount=1):
        """
        Creates a Potion object with information about its name, description, effect, effectiveness,
        element and amount.

        :param __name           :str    = None      name of the potion
        :param __description    :int    = None      what does the potion do?
        :param __effect         :str    = None      effect of the potion
        :param __effectiveness  :int    = None      effectiveness of the potion for healing and restoration
        :param __element        :str    = None      the element of the potion
        :param __amount         :int    = 1         amount of the same potion
        """
        debug_functions.debugClass(self)

        if name != '' and name is not None:
            self.set_name(name)
        if description != '' and description is not None:
            self.set_description(description)
        if effect != '' and effect is not None:
            self.set_effect(effect)
        if effectiveness != '' and effectiveness is not None:
            self.set_effectiveness(effectiveness)
        if element != '' and element is not None:
            self.set_element(element)
        if amount != '' and amount is not None:
            self.set_amount(amount)


    # ------ GETTER & SETTER --------#

    # name
    def set_name(self, value: str) -> None:
        """Defines the name of the potion and formats it."""
        try:
            value = value.strip().title()
            self.__name = value
        except AttributeError:
            print('This is not a valid potion name.')

    def get_name(self) -> None or str:
        """Fetches the formatted name of the potion."""
        try:
            return self.__name
        except AttributeError:
            print('ERROR: Failed to get the potion name.')


    # description
    def set_description(self, value: str) -> None:
        """Defines the description of the potion."""
        try:
            value = value.strip()
            self.__description = value
        except AttributeError:
            print('This is not a valid potion description.')

    def get_description(self) -> None or str:
        """Fetches the description of the potion."""
        try:
            return self.__description
        except AttributeError:
            print('ERROR: Failed to get the potion description.')


    # effect
    def set_effect(self, value: str) -> None:
        """Defines the effect of the potion."""
        value = value.strip().lower()
        if value != 'healing' and value != 'restoring' and value != 'learning':
            print('This is not a valid effect of a potion.')
        else:
            self.__effect = value

    def get_effect(self) -> None or str:
        """Fetches the effect of the potion."""
        try:
            return self.__effect
        except AttributeError:
            print('ERROR: Failed to get effect of the potion.')


    # effectiveness
    def set_effectiveness(self, value: int or str) -> None:
        """Defines the effectiveness of the potion."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the potion effectiveness must be an integer.')
        else:
            if value < 1:
                print('This is not a valid potion effectiveness.')
            else:
                self.__effectiveness = value

    def get_effectiveness(self) -> None or int:
        """Fetches the effectiveness of the potion."""
        try:
            return self.__effectiveness
        except AttributeError:
            print('ERROR: Failed to get effectiveness of the potion.')


    # element
    def set_element(self, value: str) -> None:
        """Defines the element of the potion."""
        try:
            value = value.strip().title()
            if value != 'Earth' and value != 'Water' and value != 'Air' and value != 'Fire':
                print('This is not a valid element of a potion.')
            else:
                self.__element = value
        except AttributeError:
            print('This is not a valid potion name.')


    def get_element(self) -> None or str:
        """Fetches the element of the potion."""
        try:
            return self.__element
        except AttributeError:
            print('ERROR: Failed to get element of the potion.')


    # amount
    def set_amount(self, value: int or str) -> None:
        """Defines the amount of the potion."""
        try:
            value = int(value)
        except TypeError:
            print('The format of the potion amount must be an integer.')
        else:
            if value < 0:
                print('This is not a valid potion amount.')
            else:
                self.__amount = value

    def get_amount(self) -> None or int:
        """Fetches the amount of the potion."""
        try:
            return self.__amount
        except AttributeError:
            print('ERROR: Failed to get the amount of the potion.')


    # ------ METHODS --------#
    def checkEffect(self) -> str:
        """Returns a description of the potion's effect."""
        debug_functions.debugMethod(self)

        if self.get_effect() == "healing":
            return f"{self.get_name()} restores {self.get_effectiveness()} health points."
        elif self.get_effect() == "restoring":
            return f"{self.get_name()} restores {self.get_effectiveness()} magic points "
        elif self.get_effect() == "learning":
            return f"{self.get_name()} teaches a {self.get_element()} spell."
