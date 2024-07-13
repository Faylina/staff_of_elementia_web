#---------------------------------------#
#------------ PET CLASS ----------------#
#---------------------------------------#

"""The abstract parent class for the adoption of a dog or cat"""

#---------- IMPORTS -----------#
from abc            import ABC, abstractmethod
from debugging      import debug_functions


#---------- CLASS -----------#
class Pet(ABC):
    """
        This abstract parent class represents the characteristics of a pet.
    """

    # ------ CONSTRUCTOR --------#
    @abstractmethod
    def __init__(self, name=None, age=None, color=None, sex=None):
        """
        Creates a Pet object with information about its traits.

        :param _name    : str    = None      name of the pet
        :param _age     : int    = None      age of the pet
        :param _color   : str    = None      color of the pet's fur
        :param _sex     : str    = None      the pet's sex
        :param _hungry  : bool   = True      indicates whether the pet is hungry
        :param _pronoun : str    = None      pronoun to use for the pet
        """
        debug_functions.debugClass(self)

        if name != '' and name is not None:
            self.set_name(name)
        if age != '' and age is not None:
            self.set_age(age)
        if color != '' and color is not None:
            self.set_color(color)
        if sex != '' and sex is not None:
            self.set_sex(sex)
            self.set_pronoun()
        self.set_hungry(True)


    # ------ GETTER & SETTER --------#

    # name
    def set_name(self, value: str) -> None:
        """Defines the name of the pet and formats it."""
        try:
            value = value.strip().title()
            self.__name = value
        except AttributeError:
            print('This is not a valid name.')

    def get_name(self) -> None or str:
        """Fetches the formatted name of the pet."""
        try:
            return self.__name
        except AttributeError:
            print('ERROR: Failed to get pet name.')

    # age
    def set_age(self, value: int or str) -> None:
        """Defines the age of the pet."""
        try:
            value = int(value)
        except ValueError:
            print("The pet's age is not an integer.")
        else:
            if value < 0:
                print('This is not a valid age.')
            else:
                self._age = value

    def get_age(self) -> None or int:
        """Fetches the age of the pet."""
        try:
            return self._age
        except AttributeError:
            print("ERROR: Failed to get pet's age.")

    # color
    def set_color(self, value: str) -> None:
        """Defines the color of the pet and formats it."""
        value = value.strip().lower()
        self._color = value

    def get_color(self) -> None or str:
        """Fetches the formatted color of the pet."""
        try:
            return self._color
        except AttributeError:
            print('ERROR: Failed to get pet color.')

    # sex
    def set_sex(self, value: str) -> None:
        """Defines the sex of the pet and validates it."""
        if value != 'female' and value != 'male':
            print('This is not a valid sex.')
        else:
            self._sex = value

    def get_sex(self) -> None or str:
        """Fetches the sex of the pet."""
        try:
            return self._sex
        except AttributeError:
            print("ERROR: Failed to get pet's sex.")

    # hungry
    def set_hungry(self, value: bool) -> None:
        """Defines whether the pet is hungry."""
        self._hungry = value

    def get_hungry(self) -> None or bool:
        """Indicates whether the pet is hungry."""
        try:
            return self._hungry
        except AttributeError:
            print("ERROR: Failed to get pet's hunger status.")

    # pronoun
    def set_pronoun(self) -> None:
        """Defines the pronoun of the pet."""
        if self.get_sex() == 'female':
            self._pronoun = 'her'
        elif self.get_sex() == 'male':
            self._pronoun = 'his'

    def get_pronoun(self) -> None or str:
        """Fetches the pronoun of the pet."""
        try:
            return self._pronoun
        except AttributeError:
            print("ERROR: Failed to get pet's pronoun.")


    # ------ METHODS --------#

    def adoptPet(self) -> str:
        """Congratulates the player for adopting their new pet."""
        debug_functions.debugMethod(self)
        adoption_certificate = "You've welcomed a new family member into your life! "
        adoption_certificate += "This little friend, is now yours forever, "
        adoption_certificate += "sharing the adventure and growing with you every step of the way. Congrats! "
        adoption_certificate += (f"{self.get_name()} is {self.get_sex()} and is currently {self.get_age()} years old. "
                                 f"{self.get_pronoun().title()} fur is shiny {self.get_color()}. "
                                 f"Enjoy your time together!")
        return adoption_certificate


    def call(self) -> str:
        """Calls the pet."""
        debug_functions.debugMethod(self)
        return f"{self.get_name()} runs to you happily."


    def pet(self) -> str:
        """Pets the pet."""
        debug_functions.debugMethod(self)
        return f"{self.get_name()} rolls on {self.get_pronoun()} back, visibly enjoying your affection."


    def feed(self) -> str:
        """Feeds the pet."""
        debug_functions.debugMethod(self)
        self.set_hungry(False)
        return f"{self.get_name()} eats happily."


    def play(self) -> str:
        """Plays with the pet."""
        debug_functions.debugMethod(self)
        self.set_hungry(True)
        return f"{self.get_name()} plays with you, jumping around in excitement."


    def checkIfHungry(self) -> str:
        """Checks if the pet is hungry."""
        debug_functions.debugMethod(self)
        if self.get_hungry() == True:
            return f"{self.get_name()} is hungry!"
        else:
            return f"{self.get_name()} is sated!"

