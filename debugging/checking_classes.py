#---------------------------------------#
#---------- TESTING CLASSES ------------#
#---------------------------------------#

#---------- IMPORTS --------------------#

from classes.Ingredient import Ingredient
from classes.Pouch      import Pouch
# from classes.Pet      import Pet
from classes.Dog        import Dog
from classes.Cat        import Cat
from classes.Spell      import Spell
from classes.Spellbook  import Spellbook
from classes.Witch      import Witch
from classes.Potion     import Potion
from classes.Cell       import Cell
from classes.Grid       import Grid
from classes.Forest     import Forest
from classes.Player     import Player



#---------- TESTING INGREDIENT ---------#

print('\n>>> Testing empty Ingredient object:')

ingredient1 = Ingredient()

print('\nEmpty Ingredient object:',
      '\nName:',           ingredient1.get_name(),
      '\nRarity:',         ingredient1.get_rarity(),
      '\nEffectiveness:',  ingredient1.get_effectiveness(),
      '\nEffect:',         ingredient1.get_effect(),
      '\nAmount:',         ingredient1.get_amount())


print('\n>>> Testing filled Ingredient object:')

# name=None, rarity=None, effectiveness=None, effect=None, amount=None
ingredient2 = Ingredient('dried herbs', 'Common', 3, 'health', 2)

print('\nFilled Ingredient object:',
      '\nName:',           ingredient2.get_name(),
      '\nRarity:',         ingredient2.get_rarity(),
      '\nEffectiveness:',  ingredient2.get_effectiveness(),
      '\nEffect:',         ingredient2.get_effect(),
      '\nAmount:',         ingredient2.get_amount())


print('\n>>> Testing faulty Ingredient object:')

# name=None, rarity=None, effectiveness=None, effect=None, amount=None
ingredient3 = Ingredient('dried herbs', 'Commo', '12', 'stamina')

print('\nFaulty Ingredient object:',
      '\nName:',           ingredient3.get_name(),
      '\nRarity:',         ingredient3.get_rarity(),
      '\nEffectiveness:',  ingredient3.get_effectiveness(),
      '\nEffect:',         ingredient3.get_effect(),
      '\nAmount:',         ingredient3.get_amount())

print('\n>>> Testing Ingredient method checkEffect():')
print('\nFilled Ingredient object:', ingredient2.checkEffect())
print('\nFaulty Ingredient object:', ingredient3.checkEffect())



#---------- TESTING POUCH ---------#

print('\n>>> Testing empty Pouch object:')
# inventory=None
pouch1 = Pouch()
print('\nEmpty Pouch object:',
      '\nInventory:', pouch1.get_inventory())


print('\n>>> Testing faulty Pouch object:')
# inventory=None
pouch2 = Pouch({'herbs'})
print('\nFaulty Pouch object:',
      '\nInventory:', pouch2.get_inventory())

print('\n>>> Testing Pouch method displayInventory():')
print(pouch1.displayInventory())

print('\n>>> Testing Pouch method addIngredient():')
# name=None, rarity=None, effectiveness=None, effect=None, amount=1
herbs1 = Ingredient('herbs', 'common', 2, 'magic')
herbs2 = Ingredient('herbs', 'common', 2, 'magic')
herbs3 = Ingredient('herbs', 'common', 2, 'magic')
pouch1.addItem(herbs1)
pouch1.addItem(herbs2)
pouch1.addItem(herbs3)
print('Testing valid object: Add herbs', pouch1.displayInventory())

herb = 'herb'
pouch1.addItem(herb)
print('Testing invalid object: Add herb', pouch1.displayInventory())


print('\n>>> Testing Pouch method removeIngredient():')
print(pouch1.removeItem(herbs1))
print(pouch1.removeItem(herbs2, 2))
print('Testing removing ingredient:', pouch1.displayInventory())


#---------- TESTING DOG ---------#

print('\n>>> Testing empty Dog object:')

dog1 = Dog()

print('\nEmpty Dog object:',
      '\nName:',    dog1.get_name(),
      '\nAge:',     dog1.get_age(),
      '\nColor:',   dog1.get_color(),
      '\nHungry:',  dog1.get_hungry(),
      '\nPronoun:', dog1.get_pronoun())


print('\n>>> Testing filled Dog object:')

# name=None, age=None, color=None, sex=None
dog2 = Dog('Puppy', 5, 'brown', 'male')

print('\nFilled Dog object:',
      '\nName:',    dog2.get_name(),
      '\nAge:',     dog2.get_age(),
      '\nColor:',   dog2.get_color(),
      '\nSex:',     dog2.get_sex(),
      '\nHungry:',  dog2.get_hungry(),
      '\nPronoun:', dog2.get_pronoun())


print('\n>>> Testing faulty Dog object:')

# name=None, age=None, color=None, sex=None
dog3 = Dog('dried herbs', -1, '12', 'something')

print('\nFaulty Dog object:',
      '\nName:',    dog3.get_name(),
      '\nAge:',     dog3.get_age(),
      '\nColor:',   dog3.get_color(),
      '\nSex:',     dog3.get_sex(),
      '\nHungry:',  dog3.get_hungry(),
      '\nPronoun:', dog3.get_pronoun())

print('\n>>> Testing Dog methods:')
print(dog2.adoptPet())
print(dog2.call())
print(dog2.pet())
print(dog2.checkIfHungry())
print(dog2.feed())
print(dog2.checkIfHungry())
print(dog2.play())
print(dog2.checkIfHungry())
print(dog2.look())


#---------- TESTING CAT ---------#

print('\n>>> Testing empty Cat object:')

cat1 = Cat()

print('\nEmpty Cat object:',
      '\nName:',    cat1.get_name(),
      '\nAge:',     cat1.get_age(),
      '\nColor:',   cat1.get_color(),
      '\nHungry:',  cat1.get_hungry(),
      '\nPronoun:', cat1.get_pronoun())


print('\n>>> Testing filled Cat object:')

# name=None, age=None, color=None, sex=None
cat2 = Cat('Kitty', 3, 'brown', 'female')

print('\nFilled Cat object:',
      '\nName:',    cat2.get_name(),
      '\nAge:',     cat2.get_age(),
      '\nColor:',   cat2.get_color(),
      '\nSex:',     cat2.get_sex(),
      '\nHungry:',  cat2.get_hungry(),
      '\nPronoun:', cat2.get_pronoun())


print('\n>>> Testing faulty Cat object:')

# name=None, age=None, color=None, sex=None
cat3 = Cat('dried herbs', -1, '12', 'something')

print('\nFaulty Cat object:',
      '\nName:',    cat3.get_name(),
      '\nAge:',     cat3.get_age(),
      '\nColor:',   cat3.get_color(),
      '\nSex:',     cat3.get_sex(),
      '\nHungry:',  cat3.get_hungry(),
      '\nPronoun:', cat3.get_pronoun())

print('\n>>> Testing Cat methods:')
print(cat2.adoptPet())
print(cat2.call())
print(cat2.pet())
print(cat2.checkIfHungry())
print(cat2.feed())
print(cat2.checkIfHungry())
print(cat2.play())
print(cat2.checkIfHungry())
print(cat2.look())



#---------- TESTING SPELL ---------#

print('\n>>> Testing empty Spell object:')

spell1 = Spell()

print('\nEmpty Spell object:',
      '\nName:',              spell1.get_name(),
      '\nDescription:',       spell1.get_description(),
      '\nElement:',           spell1.get_element(),
      '\nEffect:',            spell1.get_effect(),
      '\nEffectiveness:',     spell1.get_effectiveness(),
      '\nCost:',              spell1.get_cost())


print('\n>>> Testing filled Spell object:')

# name=None, description=None, effect=None, effectiveness=None, cost=None
spell2 = Spell('Windgust',
               'creates a powerful gust of wind that knocks back enemies',
               'Air',
               'offensive',
               10,
               5)

print('\nFilled Spell object:',
      '\nName:',              spell2.get_name(),
      '\nDescription:',       spell2.get_description(),
      '\nElement:',           spell2.get_element(),
      '\nEffect:',            spell2.get_effect(),
      '\nEffectiveness:',     spell2.get_effectiveness(),
      '\nCost:',              spell2.get_cost())


print('\n>>> Testing faulty Spell object:')

# name=None, description=None, effect=None, effectiveness=None, cost=None
spell3 = Spell('windgust', 'does something', 'water', 'healing', 'something', 'much')

print('\nFaulty Spell object:',
      '\nName:',              spell3.get_name(),
      '\nDescription:',       spell3.get_description(),
      '\nElement:',           spell3.get_element(),
      '\nEffect:',            spell3.get_effect(),
      '\nEffectiveness:',     spell3.get_effectiveness(),
      '\nCost:',              spell3.get_cost())

print('\n>>> Testing Spell methods:')
print(spell2.checkEffect())



#---------- TESTING SPELLBOOK ---------#

print('\n>>> Testing empty Spellbook object:')
# arsenal=[]
spellbook1 = Spellbook()
print('\nEmpty Spellbook object:',
      '\nArsenal:', spellbook1.get_arsenal())

print('\n>>> Testing faulty Spellbook object:')
# arsenal=[]
spellbook2 = Spellbook(['spell'])
print('\nFaulty Spellbook object:',
      '\nArsenal:', spellbook2.get_arsenal())

print('\n>>> Testing Spellbook method addSpell():')
print(spellbook1.addSpell(spell2))

print('\n>>> Testing Spellbook method displayArsenal():')
print('Filled Spellbook', spellbook1.displayArsenal())

herb = 'herb'
spellbook1.addSpell(herb)
print('Testing invalid object: Add herb', spellbook1.displayArsenal())



#---------- TESTING WITCH ---------#

print('\n>>> Testing empty Witch object:')

witch1 = Witch()

print('\nEmpty Witch object:',
      '\nForest:',            witch1.get_forest(),
      '\nFamiliar:',          witch1.get_familiar(),
      '\nName:',              witch1.get_name(),
      '\nMax HP:',            witch1.get_max_HP(),
      '\nCurrent HP:',        witch1.get_current_HP(),
      '\nMax MP:',            witch1.get_max_MP(),
      '\nCurrent MP:',        witch1.get_current_MP(),
      '\nGold:',              witch1.get_gold(),
      '\nPouch:',             witch1.get_pouch(),
      '\nSpellbook:',         witch1.get_spellbook(),
      '\nAction list:',       witch1.get_action_list(),
      '\nWitch Art:',         witch1.get_art())


print('\n>>> Testing filled Witch object:')

'''
forest         = Forest()
familiar       = None,
name           = 'Asciri',
max_HP         = 20,
current_HP     = 20,
max_MP         = 0,
current_MP     = 0,
gold           = 30,
pouch          = Pouch(),
spellbook      = Spellbook(),
action_list    = []
'''
forest = Forest()
witch2 = Witch(forest,
               dog2,
               'Witchy',
               30,
               15,
               15,
               10,
               250,
               pouch1,
               spellbook1,
               [])

print('\nFilled Witch object:',
      '\nForest:',            witch2.get_forest(),
      '\nFamiliar:',          witch2.get_familiar(),
      '\nName:',              witch2.get_name(),
      '\nMax HP:',            witch2.get_max_HP(),
      '\nCurrent HP:',        witch2.get_current_HP(),
      '\nMax MP:',            witch2.get_max_MP(),
      '\nCurrent MP:',        witch2.get_current_MP(),
      '\nGold:',              witch2.get_gold(),
      '\nPouch:',             witch2.get_pouch(),
      '\nSpellbook:',         witch2.get_spellbook(),
      '\nAction list:',       witch2.get_action_list(),
      '\nWitch Art:',         witch2.get_art())


print('\n>>> Testing faulty Witch object:')

'''
forest         = Forest()
familiar       = None,
name           = 'Asciri',
max_HP         = 20,
current_HP     = 20,
max_MP         = 0,
current_MP     = 0,
gold           = 30,
pouch          = Pouch(),
spellbook      = Spellbook(),
action_list    = []
'''
witch3 = Witch( forest,
                pouch2,
               12,
               15,
               -4,
               -9,
               '12',
               -54,
               dog2,
               cat2,
               ['herbs'])

print('\nFaulty Witch object:',
      '\nForest:',            witch3.get_forest(),
      '\nFamiliar:',          witch3.get_familiar(),
      '\nName:',              witch3.get_name(),
      '\nMax HP:',            witch3.get_max_HP(),
      '\nCurrent HP:',        witch3.get_current_HP(),
      '\nMax MP:',            witch3.get_max_MP(),
      '\nCurrent MP:',        witch3.get_current_MP(),
      '\nGold:',              witch3.get_gold(),
      '\nPouch:',             witch3.get_pouch(),
      '\nSpellbook:',         witch3.get_spellbook(),
      '\nAction list:',       witch3.get_action_list(),
      '\nWitch Art:',         witch3.get_art())

print('\n>>> Testing Witch methods:')
print("\nWitch's inventory:",  witch1.checkInventory())
print("\nWitch's arsenal:",    witch1.readSpellbook())
print("\nWitch's actions:",    witch1.listActions())
print("\nAdd ingredient:",     witch1.addItemToPouch(ingredient2))
print("\nWitch's inventory:",  witch1.checkInventory())
print("\nAdd ingredient:",     witch1.removeItemFromPouch(ingredient2,1))
print("\nWitch's inventory:",  witch1.checkInventory())
print("\nLearn spell:",        witch1.learnSpell(spell2))
print("\nWitch's arsenal:",    witch1.readSpellbook())
print("\nAdopt pet:",          witch2.adoptPet())
print("\nCall pet:",           witch2.callPet())
print("\nLook at pet:",        witch2.lookAtPet())
print("\nPet pet:",            witch2.petPet())
print("\nPlay with pet:",      witch2.playWithPet())
print("\nCheck pet's hunger:", witch2.checkPetsHunger())
print("\nFeed pet:",           witch2.feedPet())
print("\nCheck pet's hunger:", witch2.checkPetsHunger())




#---------- TESTING POTION ---------#

print('\n>>> Testing empty Potion object:')

potion1 = Potion()

print('\nEmpty Potion object:',
      '\nName:',           potion1.get_name(),
      '\nDescription:',    potion1.get_description(),
      '\nEffect:',         potion1.get_effect(),
      '\nEffectiveness:',  potion1.get_effectiveness(),
      '\nElement:',        potion1.get_element(),
      '\nAmount:',         potion1.get_amount())


print('\n>>> Testing filled Potion object:')

# name=None, description=None, effect=None, effectiveness=None, element=None, amount=1
potion2 = Potion('healing potion',
                 'Heals a certain amount of HP.',
                 'healing',
                 20,
                 'air',
                 2)

print('\nFilled Potion object:',
      '\nName:',           potion2.get_name(),
      '\nDescription:',    potion2.get_description(),
      '\nEffect:',         potion2.get_effect(),
      '\nEffectiveness:',  potion2.get_effectiveness(),
      '\nElement:',        potion2.get_element(),
      '\nAmount:',         potion2.get_amount())


print('\n>>> Testing faulty Potion object:')

# name=None, description=None, effect=None, effectiveness=None, element=None, amount=1
potion3 = Potion(12, 5, '12', 'stamina', 15)

print('\nFaulty Potion object:',
      '\nName:',           potion1.get_name(),
      '\nDescription:',    potion1.get_description(),
      '\nEffect:',         potion1.get_effect(),
      '\nEffectiveness:',  potion1.get_effectiveness(),
      '\nElement:',        potion1.get_element(),
      '\nAmount:',         potion1.get_amount())

print('\n>>> Testing Potion method checkEffect():')
print('\nFilled Potion object:', potion2.checkEffect())
print('\nFaulty Potion object:', potion3.checkEffect())



#---------- TESTING BREW POTION ---------#

print('\n>>> Testing brewing Potions:')

small_mixed_herbs = Ingredient( 'small pouch of mixed herbs',
                                            'common',
                                            100,
                                            'health',
                                            3)
vial_of_moonlight = Ingredient( 'vial of concentrated moonlight essence',
                                            'common',
                                            2,
                                            'magic',
                                            3)
handful_of_soil = Ingredient('handful of enchanted soil from the heart of the forest',
                                         'common',
                                         2,
                                         'base',
                                         3)
lumina_fungus = Ingredient('lumina fungus',
                                         'legendary',
                                         1,
                                         'spell',
                                         3)

witch2.addItemToPouch(small_mixed_herbs)
witch2.addItemToPouch(vial_of_moonlight)
witch2.addItemToPouch(handful_of_soil)
witch2.addItemToPouch(lumina_fungus)
print(witch2.checkInventory())
potion1 = witch2.brewPotion(small_mixed_herbs, handful_of_soil)
potion2 = witch2.brewPotion(vial_of_moonlight, handful_of_soil)
potion3 = witch2.brewPotion(small_mixed_herbs, handful_of_soil)
potion4 = witch2.brewPotion(lumina_fungus, handful_of_soil)
potion5 = witch2.brewPotion(lumina_fungus, handful_of_soil)
print(witch2.checkInventory())

print('\n>>> Testing healing Potion:')
print('\nMax HP: ', witch2.get_max_HP())
print('\nCurrent HP: ', witch2.get_current_HP())
witch2.drinkPotion(potion1)
print(witch2.checkInventory())
print('\nMax HP: ', witch2.get_max_HP())
print('\nCurrent HP: ', witch2.get_current_HP())

print('\n>>> Testing restoring Potion:')
print('\nMax MP: ', witch2.get_max_MP())
print('\nCurrent MP: ', witch2.get_current_MP())
witch2.drinkPotion(potion2)
print(witch2.checkInventory())
print('\nMax MP: ', witch2.get_max_MP())
print('\nCurrent MP: ', witch2.get_current_MP())

print('\n>>> Testing learning Potion:')
print(witch2.checkInventory())
print(witch2.readSpellbook())
spell1 = witch2.drinkPotion(potion4)
print(witch2.readSpellbook())
print(witch2.checkInventory())
spell2 = witch2.drinkPotion(potion5)
print(witch2.readSpellbook())
print(witch2.checkInventory())


#---------- TESTING CELL ---------#

print('\n>>> Testing empty Cell object:')

cell1 = Cell()

print('\nEmpty Cell object:',
      '\nCoordinates:',             cell1.get_coordinates(),
      '\nLevel:',                   cell1.get_level(),
      '\nContent:',                 cell1.get_content(),
      '\nOccupied:',                cell1.get_occupied(),
      '\nEnvironment Description:', cell1.get_env_descriptions())


print('\n>>> Testing filled Cell object:')

# coordinates=None, level=None, content=None, occupied=False, env_descriptions=None
cell2 = Cell((1,1), 1, 'scenery', True)

print('\nFilled Cell object:',
      '\nCoordinates:',             cell2.get_coordinates(),
      '\nLevel:',                   cell2.get_level(),
      '\nContent:',                 cell2.get_content(),
      '\nOccupied:',                cell2.get_occupied(),
      '\nEnvironment Description:', cell2.get_env_descriptions())


print('\n>>> Testing faulty Cell object:')

# name=None, rarity=None, effectiveness=None, effect=None, amount=None
cell3 = Cell('dried herbs', 'Commo', '12')

print('\nFaulty Cell object:',
      '\nCoordinates:',             cell3.get_coordinates(),
      '\nLevel:',                   cell3.get_level(),
      '\nContent:',                 cell3.get_content(),
      '\nOccupied:',                cell3.get_occupied(),
      '\nEnvironment Description:', cell3.get_env_descriptions())

print('\n>>> Testing Cell methods:')
cell2.enter()
print('\nCell enter():', cell2.get_occupied())
cell2.leave()
print('\nCell leave():', cell2.get_occupied())
print('\nCell describeEnvironment():', cell2.describeEnvironment())


#---------- TESTING GRID ---------#

print('\n>>> Testing empty Grid object:')
# grid=None
grid1 = Grid()
print('\nEmpty Grid object:',
      '\nGrid:', grid1.get_grid())


print('\n>>> Testing faulty Grid object:')
# grid=None
grid2 = Grid({'herbs'})
print('\nFaulty Grid object:',
      '\nGrid:', grid2.get_grid())

print('\n>>> Testing Grid method addCell():')
grid1.addCell(cell2)
cell4 = Cell((2,1), 1, 'scenery', False)
grid1.addCell(cell4)

print('\n>>> Testing Grid method displayGrid():')
print(grid1.displayGrid())

herb = 'herb'
grid1.addCell(herb)
print('Testing invalid Cell object: Add herb', grid1.displayGrid())



#---------- TESTING FOREST ---------#

print('\n>>> Testing empty Forest object:')

forest1 = Forest()

print('\nEmpty Forest object:',
      '\nGrid Layout:', forest1.get_grid_layout(),
      '\nPosition:',    forest1.get_position(),
      '\nGrid:',        forest1.get_grid())


print('\n>>> Testing filled Forest object:')

# grid_layout=None, position=None, grid=None
forest2 = Forest('3x3', [1,1], grid1)

print('\nFilled Forest object:',
      '\nGrid Layout:', forest2.get_grid_layout(),
      '\nPosition:',    forest2.get_position(),
      '\nGrid:',        forest2.get_grid())


print('\n>>> Testing faulty Forest object:')

# grid_layout=None, position=None, grid=None
forest3 = Forest(9, {1,2}, grid2)

print('\nFaulty Forest object:',
      '\nGrid Layout:', forest3.get_grid_layout(),
      '\nPosition:',    forest3.get_position(),
      '\nGrid:',        forest3.get_grid())

print('\n>>> Testing Witch method walk():')

witch4 = Witch(forest2,
               dog2,
               'Witchy',
               30,
               15,
               15,
               10,
               250,
               pouch1,
               spellbook1,
               [])

print(witch4.walk('east'))


#---------- TESTING PLAYER ---------#

print('\n>>> Testing empty Player object:')

player1 = Player()

print('\nEmpty Player object:',
      '\nName:', player1.get_name())


print('\n>>> Testing filled Player object:')

# name=None
player2 = Player('Sabrina')

print('\nFilled Player object:',
      '\nName:', player2.get_name())


print('\n>>> Testing faulty Player object:')

# name=None
player3 = Player(9)

print('\nFaulty Player object:',
      '\nName:', player3.get_name())

print('\n>>> Testing Player method greet():')
print(player2.greetPlayer())

