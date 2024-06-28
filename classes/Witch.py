#---------------------------------------#
#------------ WITCH CLASS --------------#
#---------------------------------------#

"""The class for the creation of a witch"""

#---------- IMPORTS -----------#

from debugging          import debug_functions
from classes.Pouch      import Pouch
from classes.Spellbook  import Spellbook
from classes.Cat        import Cat
from classes.Dog        import Dog
from classes.Ingredient import Ingredient
from classes.Spell      import Spell
from classes.Potion     import Potion
from classes.Forest     import Forest


#---------- CLASS -----------#
class Witch:
    """
        This class represents the characteristics of a witch.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self,
                 forest         = Forest(),
                 familiar       = None,
                 name           = 'Asciri',
                 max_HP         = 20,
                 current_HP     = 20,
                 max_MP         = 0,
                 current_MP     = 0,
                 gold           = 30,
                 pouch          = Pouch(),
                 spellbook      = Spellbook(),
                 action_list    = None
                 ):
        """
        Creates a Witch object with information about her traits and possessions.

        :param __forest      : Forest               = Forest()     the forest that the witch is currently in
        :param __familiar    : Cat or Dog or str    = None         pet of the witch
        :param __name        : str                  = 'Asciri'     name of the witch
        :param __max_HP      : int                  = 20           maximum health points of the witch
        :param __current_HP  : int                  = 20           current health point of the witch
        :param __max_MP      : int                  = 0            maximum mana points of the witch
        :param __current_MP  : int                  = 0            current mana point of the witch
        :param __gold        : int                  = 30           gold in possession of the witch
        :param __pouch       : Pouch                = Pouch()      inventory of the witch
        :param __spellbook   : Spellbook            = Spellbook()  spellbook of the witch
        :param __action_list : list                 = None         list of currently available actions
        :param __witch_art   : str                  = string       image of the witch
        """
        debug_functions.debugClass(self)

        if forest != '' and forest is not None:
            self.set_forest(forest)

        self.set_familiar(familiar)

        if name != '' and name is not None:
            self.set_name(name)
        if max_HP != '' and max_HP is not None:
            self.set_max_HP(max_HP)
        if current_HP != '' and current_HP is not None:
            self.set_current_HP(current_HP)
        if max_MP != '' and max_MP is not None:
            self.set_max_MP(max_MP)
        if current_MP != '' and current_MP is not None:
            self.set_current_MP(current_MP)
        if gold != '' and gold is not None:
            self.set_gold(gold)
        if pouch != '' and pouch is not None:
            self.set_pouch(pouch)
        if spellbook != '' and spellbook is not None:
            self.set_spellbook(spellbook)

        self.set_action_list(action_list)
        self.set_art()

    # ------ GETTER & SETTER --------#

    # forest
    def set_forest(self, value: Forest) -> None:
        """Defines the forest that the witch is in."""
        if isinstance(value, Forest):
            self.__forest = value
        else:
            print('This is not a forest.')

    def get_forest(self) -> Forest:
        """Fetches the forest that the witch is in."""
        try:
            return self.__forest
        except AttributeError:
            print('ERROR: Failed to get the forest.')

    # familiar
    def set_familiar(self, value: Cat or Dog or None) -> None:
        """Allows the witch to adopt a dog or cat if she chooses to."""

        if type(value) == Cat or type(value) == Dog or value is None:
            self.__familiar = value
        else:
            print('This is not a valid familiar.')

    def get_familiar(self) -> None or Cat or Dog:
        """Fetches the pet of the witch."""
        try:
            return self.__familiar
        except AttributeError:
            print('ERROR: Failed to get pet.')


    # name
    def set_name(self, value: str) -> None:
        """Defines the name of the witch and formats it."""
        try:
            value = value.strip().title()
            self.__name = value
        except AttributeError:
            print('This is not a valid name.')

    def get_name(self) -> None or str:
        """Fetches the formatted name of the witch."""
        try:
            return self.__name
        except AttributeError:
            print("ERROR: Failed to get the witch's name.")


    # max_HP
    def set_max_HP(self, value: int or str) -> None:
        """Defines the maximum amount of HP the witch can have at her disposal."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the maximum HP must be an integer.')
        else:
            if value < 20:
                print('This is not a valid max HP amount.')
            else:
                self.__max_HP = value

    def get_max_HP(self) -> None or int:
        """Fetches the maximum HP of the witch."""
        try:
            return self.__max_HP
        except AttributeError:
            print('ERROR: Failed to get max HP.')


    # current_HP
    def set_current_HP(self, value: int or str) -> None:
        """Defines the current amount of HP of the witch."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the current HP must be an integer.')
        else:
            if value < 0:
                print('This is not a valid current HP amount.')
            else:
                self.__current_HP = value

    def get_current_HP(self) -> None or int:
        """Fetches the current HP of the witch."""
        try:
            return self.__current_HP
        except AttributeError:
            print('ERROR: Failed to get current HP.')


    # max_MP
    def set_max_MP(self, value: int or str) -> None:
        """Defines the maximum amount of MP the witch can have at her disposal."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the maximum MP must be an integer.')
        else:
            if value < 0:
                print('This is not a valid max MP amount.')
            else:
                self.__max_MP = value

    def get_max_MP(self) -> None or int:
        """Fetches the maximum MP of the witch."""
        try:
            return self.__max_MP
        except AttributeError:
            print('ERROR: Failed to get max MP.')


    # current_MP
    def set_current_MP(self, value: int or str) -> None:
        """Defines the current amount of MP of the witch."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the current MP must be an integer.')
        else:
            if value < 0:
                print('This is not a valid current MP amount.')
            else:
                self.__current_MP = value

    def get_current_MP(self) -> None or int:
        """Fetches the current MP of the witch."""
        try:
            return self.__current_MP
        except AttributeError:
            print('ERROR: Failed to get current MP.')


    # gold
    def set_gold(self, value: int or str) -> None:
        """Defines the current amount of gold of the witch."""
        try:
            value = int(value)
        except ValueError:
            print('The format of gold must be an integer.')
        else:
            if value < 0:
                print('This is not a valid gold amount.')
            else:
                self.__gold = value

    def get_gold(self) -> None or int:
        """Fetches the current amount of gold of the witch."""
        try:
            return self.__gold
        except AttributeError:
            print('ERROR: Failed to get gold.')


    # pouch
    def set_pouch(self, value: Pouch) -> None:

        if isinstance(value, Pouch):
            self.__pouch = value
        else:
            print('This is not a pouch.')

    def get_pouch(self) -> Pouch:
        """Fetches the pouch of the witch."""
        try:
            return self.__pouch
        except AttributeError:
            print('ERROR: Failed to get the pouch.')


    # spellbook
    def set_spellbook(self, value: Spellbook) -> None:
        """Creates the spellbook of the witch."""
        if isinstance(value, Spellbook):
            self.__spellbook = value
        else:
            print('This is not a spellbook.')

    def get_spellbook(self) -> Spellbook:
        """Fetches the spellbook of the witch."""
        try:
            return self.__spellbook
        except AttributeError:
            print('ERROR: Failed to get the spellbook.')


    # action_list (- to be deleted?)
    def set_action_list(self, value: list) -> None:
        """Creates the list of action that the witch can perform."""

        if value is not None and type(value) == list:
            self.__action_list = value
        # the witch starts the game with some basic actions that are added to her action list
        else:

            initial_action_list = ['List actions you can perform',
                                   'Check your inventory',
                                   'Read your spellbook',
                                   'Brew a potion',
                                   'Drink a potion'
                                   'Cast a spell',
                                   'Walk through the forest',
                                   'Search for ingredient',
                                   'Flee from opponent',
                                   'Add ingredient to your pouch',
                                   'Remove ingredient from your pouch',
                                   'Add spell to your spellbook',
                                   'Call your pet',
                                   'Look at your pet',
                                   'Pet your pet',
                                   'Play with your pet',
                                   'Feed your pet',
                                   'Check if your pet is hungry'
                                   ]

            self.__action_list = initial_action_list

    def get_action_list(self) -> list:
        """Fetches the list of actions that the witch is able to perform."""
        try:
            return self.__action_list
        except AttributeError:
            print('ERROR: Failed to get action list.')


    # witch_art
    def set_art(self) -> None:
        """Creates the image of a witch."""
        witch_art =  '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢠⣿'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡆'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣼⣿⡇'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢣⣿⣿⡇'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡼⠏⣼⣿⣿⣿'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⢹⣿⢻⣿⣿⣿⣦⣄'
        witch_art += '\n⠀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⣸⠟⠛⠿⠶⢾⣿⣿⣿⣿⡿⠗'
        witch_art += '\n⠘⢿⣿⣿⣿⣦⡀⠀⠀⠀⢀⣿⠐⡀⠀⠰⠘⣿⣿⣿⣿⡄'
        witch_art += '\n⠀⠀⠈⠉⠛⠻⠿⣶⣶⠄⢸⣿⣧⣄⣀⠀⢀⣿⣿⣿⣿⡇'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⢞⣿⣿⣿⣧⣾⣶⣿⣿⣿⠿⠟'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⣿⣿⣿⡿⠀'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣼⢄⡀'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠧⠈⠁'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⠉'
        self.__witch_art = witch_art

    def get_art(self) -> str:
        """Fetches the image of a witch."""
        return self.__witch_art


    # ------ METHODS --------#

    def checkInventory(self) -> str:
        """Lists all ingredients in the pouch with their respective amounts."""
        debug_functions.debugMethod(self)
        return self.get_pouch().displayInventory()


    def readSpellbook(self) -> str:
        """Lists all spells in the spellbook."""
        debug_functions.debugMethod(self)
        return self.get_spellbook().displayArsenal()


    def listActions(self) -> str:
        """Lists all actions that the witch can perform."""
        debug_functions.debugMethod(self)

        current_action = '\nYou can do this:'
        for item in self.get_action_list():
            current_action += f"\n\t{item}"

        return current_action


    def addItemToPouch(self, item: Ingredient or Potion) -> str:
        """Adds an item to the pouch."""
        debug_functions.debugMethod(self)
        return self.get_pouch().addItem(item)


    def removeItemFromPouch(self, ingredient: Ingredient, amount: int = 1) -> str:
        """Removes an item from the pouch."""
        debug_functions.debugMethod(self)
        return self.get_pouch().removeItem(ingredient, amount)


    def learnSpell(self, spell: Spell) -> str:
        """Adds a spell to the spellbook."""
        debug_functions.debugMethod(self)
        return self.get_spellbook().addSpell(spell)


    @staticmethod
    def choosePet() -> Dog or Cat or None:
        """Allows the player to create and customize the witch's pet."""
        pet_choice = input('\nWhat kind of pet would you like to adopt? (cat/dog)\n')
        pet_choice = pet_choice.strip().lower()
        debug_functions.debugVariable('pet_choice', pet_choice)

        pet_sex = input('\nWhat would you like the sex of your pet to be? (male/female)\n')
        debug_functions.debugVariable('pet_sex', pet_sex)

        pet_name = input('\nWhat would you like to name your pet?\n')
        debug_functions.debugVariable('pet_name', pet_name)

        pet_age = input('\nHow old would you prefer your pet to be?\n')
        debug_functions.debugVariable('pet_age', pet_age)

        pet_color = input('\nWhat color would you prefer your pet to be?\n')
        debug_functions.debugVariable('pet_color', pet_color)

        # creating a pet
        if pet_choice == 'cat':
            # name = None, age = None, color = None, sex = None
            pet = Cat(pet_name, pet_age, pet_color, pet_sex)
            debug_functions.debugVariable('pet.look()', pet.look())

        elif pet_choice == 'dog':
            # name = None, age = None, color = None, sex = None
            pet = Dog(pet_name, pet_age, pet_color, pet_sex)
            debug_functions.debugVariable('pet.look()', pet.look())

        else:
            print('There are no pets of this kind for adoption.')
            pet = None

        if pet is not None:
            if (    pet.get_name()  is None or
                    pet.get_age()   is None or
                    pet.get_color() is None or
                    pet.get_sex()   is None):

                pet = None

        return pet


    def adoptPet(self) -> str:
        """Congratulates the player for adopting their new pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().adoptPet()


    def callPet(self) -> str:
        """Calls your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().call()


    def lookAtPet(self) -> str:
        """Look at your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().look()


    def petPet(self) -> str:
        """Pet your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().pet()


    def playWithPet(self) -> str:
        """Play with your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().play()


    def feedPet(self) -> str:
        """Feed your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().feed()


    def checkPetsHunger(self) -> str:
        """Checks if your pet is hungry."""
        debug_functions.debugMethod(self)
        return self.get_familiar().checkIfHungry()


    def brewPotion(self, ingredient1: Ingredient, ingredient2: Ingredient) -> Potion:
        """Brews a potion depending on the provided ingredients and puts it in the pouch."""
        debug_functions.debugMethod(self)

        # healing ingredients
        healing_ingredient1 = 'Small Pouch Of Mixed Herbs'

        # restoring ingredients
        restoring_ingredient1 = 'Vial Of Concentrated Moonlight Essence'

        # ingredients for learning spells
        spell_ingredient1 = 'Lumina Fungus'

        # base ingredients
        base_ingredient = 'Handful Of Enchanted Soil From The Heart Of The Forest'

        if (
                (ingredient1.get_name() == healing_ingredient1
                 and ingredient2.get_name() == base_ingredient)
                or
                (ingredient1.get_name() == base_ingredient
                 and ingredient2.get_name() == healing_ingredient1)
        ):
            # name = None, description = None, effect = None, effectiveness = None, element = None, amount = 1
            new_potion = Potion('Greenwood Healer',
                                'A thick, dark green liquid with small flecks of dirt suspended in it. '
                                'This potion is said to contain the life force of the enchanted forest itself, '
                                'granting the consumer a surge of energy and vitality.',
                                'healing',
                                ingredient1.get_effectiveness() + ingredient2.get_effectiveness(),
                                'earth'
                                )

            self.addItemToPouch(new_potion)
            self.removeItemFromPouch(ingredient1)
            self.removeItemFromPouch(ingredient2)
            return new_potion

        elif (
                (ingredient1.get_name() == restoring_ingredient1
                 and ingredient2.get_name() == base_ingredient)
                or
                (ingredient1.get_name() == base_ingredient
                 and ingredient2.get_name() == restoring_ingredient1)
        ):
            # name = None, description = None, effect = None, effectiveness = None, element = None, amount = 1
            new_potion = Potion('Lunar Restoration',
                                'This potion glows softly with a pale blue light, '
                                'and carries a faint scent of citrus. '
                                'When consumed, it immediately restores a portion of your mana.',
                                'restoring',
                                ingredient1.get_effectiveness() + ingredient2.get_effectiveness(),
                                'air'
                                )

            self.addItemToPouch(new_potion)
            self.removeItemFromPouch(ingredient1)
            self.removeItemFromPouch(ingredient2)
            return new_potion

        elif (
                (ingredient1.get_name() == spell_ingredient1
                 and ingredient2.get_name() == base_ingredient)
                or
                (ingredient1.get_name() == base_ingredient
                 and ingredient2.get_name() == spell_ingredient1)
        ):
            # name = None, description = None, effect = None, effectiveness = None, element = None, amount = 1
            new_potion = Potion('Elemental Infusion',
                              'This potion '
                              'is said to imbue the drinker with the power of a thousand suns. '
                              'Its golden, shimmering liquid appears to dance with the promise of magical knowledge. '
                              'Consuming it grants the drinker the ability to learn a devastating spell '
                              'to defeat their enemies.',
                              'learning',
                              1,
                              'air'
                              )

            self.addItemToPouch(new_potion)
            self.removeItemFromPouch(ingredient1)
            self.removeItemFromPouch(ingredient2)
            return new_potion



    def drinkPotion(self, potion: Potion) -> None or str:
        """Drink a potion."""
        debug_functions.debugMethod(self)

        if isinstance(potion, Potion):
            if potion.get_effect() == 'healing':

                current_HP_amount = self.get_current_HP()
                potion_effect = potion.get_effectiveness()
                max_HP = self.get_max_HP()

                # if adding the HP would exceed the max HP, set current HP to max HP
                if (current_HP_amount + potion_effect) >= max_HP:
                    self.set_current_HP(max_HP)

                # otherwise increase the current HP by the additional amount
                else:
                    self.set_current_HP(current_HP_amount + potion_effect)

            elif potion.get_effect() == 'restoring':

                current_MP_amount = self.get_current_MP()
                potion_effect = potion.get_effectiveness()
                max_MP = self.get_max_MP()

                # if adding the MP would exceed the max MP, set current MP to max MP
                if (current_MP_amount + potion_effect) >= max_MP:
                    self.set_current_MP(max_MP)

                # otherwise increase the current MP by the additional amount
                else:
                    self.set_current_MP(current_MP_amount + potion_effect)

            elif potion.get_effect() == 'learning':
                # create a new Spell
                # name = None, description = None, element = None, effect = None, effectiveness = None, cost = None
                new_spell = Spell('Wind Gust',
                                  'Wind Gust creates a powerful gust of wind that knocks back enemies '
                                  'and disorients them.',
                                  'air',
                                  'offensive',
                                  20,
                                  5
                                  )

                self.learnSpell(new_spell)
                self.get_pouch().removeItem(potion)
                return new_spell

            self.get_pouch().removeItem(potion)
        else:
            return 'This is not a potion.'


    def castSpell(self, spell: Spell) -> str:
        """Casts a spell."""
        debug_functions.debugMethod(self)

        if spell.get_effect() == 'offensive':
            # TODO: add spell effect
            pass

        elif spell.get_effect() == 'defensive':
            # TODO: add spell effect
            pass

        elif spell.get_effect() == 'healing':
            # spell cost
            current_MP_amount = self.get_current_MP()
            spell_cost = spell.get_cost()

            # if there is not enough mana to cast the spell
            if (current_MP_amount - spell_cost) < 0:
                return "You don't have enough mana to cast this spell."

            # if there is enough mana, use spell
            else:
                self.set_current_MP(current_MP_amount - spell_cost)

                # healing effect
                current_HP_amount = self.get_current_HP()
                spell_effect = spell.get_effectiveness()
                max_HP = self.get_max_HP()

                # if adding the HP would exceed the max HP, set current HP to max HP
                if (current_HP_amount + spell_effect) >= max_HP:
                    self.set_current_HP(max_HP)

                # otherwise increase the current HP by the additional amount
                else:
                    self.set_current_HP(current_HP_amount + spell_effect)

                return (f'You have healed {spell_effect} HP. Currently you have {self.get_current_HP()} HP '
                        f'of {self.get_max_HP()} HP.')


    def walk(self, direction: str) -> str:
        """Move around in the forest."""
        debug_functions.debugMethod(self)

        current_position = self.get_forest().get_position()
        old_x = current_position[0]
        old_y = current_position[1]

        border_x = int(self.get_forest().get_grid_layout()['x'])
        border_y = int(self.get_forest().get_grid_layout()['y'])

        # walk east
        if direction == 'east':
            # check x border
            if (old_x + 1) > border_x:
                return 'This is the end of the forest. The path is blocked.'
            else:
                # leave previous cell
                self.get_forest().leaveCell()
                # update position
                self.get_forest().set_position([old_x + 1, old_y])
                # enter new cell
                return self.get_forest().enterCell()

        # walk west
        elif direction == 'west':
            # check x border
            if (old_x - 1) == 0:
                return 'This is the end of the forest. The path is blocked.'
            else:
                # leave previous cell
                self.get_forest().leaveCell()
                # update position
                self.get_forest().set_position([old_x - 1, old_y])
                # enter new cell
                return self.get_forest().enterCell()

        # walk north
        elif direction == 'north':
            # check y border
            if (old_y + 1) > border_y:
                return 'This is the end of the forest. The path is blocked.'
            else:
                # leave previous cell
                self.get_forest().leaveCell()
                # update position
                self.get_forest().set_position([old_x, old_y + 1])
                # enter new cell
                return self.get_forest().enterCell()

        # walk south
        elif direction == 'south':
            # check y border
            if (old_y - 1) == 0:
                return 'This is the end of the forest. The path is blocked.'
            else:
                # leave previous cell
                self.get_forest().leaveCell()
                # update position
                self.get_forest().set_position([old_x, old_y - 1])
                # enter new cell
                return self.get_forest().enterCell()


    def search(self):
        """Search for an ingredient in the forest."""
        debug_functions.debugMethod(self)
        # TODO: finish search method


    def flee(self):
        """Flee from an enemy."""
        debug_functions.debugMethod(self)
        # TODO: finish flee method
