#---------------------------------------#
#--------- STAFF OF ELEMENTIA ----------#
#-------------- GAMEPLAY ---------------#
#---------------------------------------#

"""This is the main gameplay."""

#---------- IMPORTS -----------#

from debugging          import debug_functions, config
from texts              import gameplay_snippets
from classes.Game       import Game
from classes.Player     import Player
from classes.Forest     import Forest
from classes.Witch      import Witch
import requests 


def play_game(player_input):

    #---------- VARIABLES ----------#

    new_texts   = []
    n           = 0
    input       = player_input

    #---------- FUNCTIONS -----------#

    def increment(n):
        n = n + 1
        return n

    #---------- INTRO ---------------#

    #new_texts.append(gameplay_snippets.title)
    new_texts.append(gameplay_snippets.intro)
    new_texts.append('Enter your response (y = I want to help! / n = No, thanks...):')

    if( len(input) > n):
        confirmation    = input[n]      
        n               = increment(n) 

        confirmation    = confirmation.strip().lower()
        debug_functions.debugVariable('confirmation', confirmation)

        new_texts.append('Your answer: ' + confirmation) 

        if confirmation != 'y':
            new_texts.append('Farewell, traveler. Come back when you are ready to tackle this challenge.')
            new_texts_str = '$'.join(new_texts)
            requests.put(url=config.URL, json={'texts': new_texts_str})   
    
        else:
 
            #---------- CREATING A PLAYER ---------#

            new_texts.append('Then state your name, brave traveler!')
            new_texts_str = '$'.join(new_texts)
            requests.put(url=config.URL, json={'texts': new_texts_str})

            if( len(input) > n ):

                player_name = input[n]      
                n           = increment(n)  

                player_name = player_name.strip()
                debug_functions.debugVariable('player_name', player_name)

                # name = None
                player = Player(player_name)
                debug_functions.debugVariable('player.get_name()', player.get_name())

                # TODO: check if the player has played before

                # case: player has not played before
                greeting = player.greetPlayer()

                new_texts.append('Your answer: ' + player_name)  

                new_texts.append(greeting) 

                new_texts.append('Are you ready to start a new adventure? (y/n)')
                new_texts_str = '$'.join(new_texts)
                requests.put(url=config.URL, json={'texts': new_texts_str})   

                if( len(input) > n ):

                    new_game_confirmation = input[n]      
                    n                     = increment(n)  

                    new_game_confirmation = new_game_confirmation.strip().lower()
                    debug_functions.debugVariable('new_game_confirmation', new_game_confirmation)

                    new_texts.append('Your answer: ' + new_game_confirmation) 

                    if new_game_confirmation != 'y':

                        new_texts.append(f"Farewell, {player_name}. Come back when you're ready to tackle this challenge.")
                        new_texts_str = '$'.join(new_texts)
                        requests.put(url=config.URL, json={'texts': new_texts_str})

                    else:

                        #---------- CREATING THE FOREST ---------#

                        debug_functions.debugProcess('Creating the forest...')

                        # create the forest grid for level 1
                        grid = Forest.createGrid(1)
                        debug_functions.debugVariable('grid.get_grid()', grid.get_grid())

                        # create the forest
                        # grid_layout = None, position = None, grid = None)
                        forest = Forest('3x3', [2, 2], grid)
                        debug_functions.debugVariable('forest.get_grid()', forest.get_grid())


                        # ---------- CREATING THE WITCH AND HER PET ---------#

                        debug_functions.debugProcess('Creating the witch and her pet...')

                        # player customization of the witch and her pet
                        new_texts.append("Let's transform you into a witch!")  

                        new_texts.append("What would you like to be called as a witch?")
                        new_texts_str = '$'.join(new_texts)
                        requests.put(url=config.URL, json={'texts': new_texts_str})   

                        if( len(input) > n ):
                        
                            witch_name = input[n]      
                            n          = increment(n)
                            debug_functions.debugVariable('witch_name', witch_name)

                            new_texts.append('Your answer: ' + witch_name)

                            new_texts.append('Would you like to adopt a pet? (y/n)')
                            new_texts_str = '$'.join(new_texts)
                            requests.put(url=config.URL, json={'texts': new_texts_str})

                            if( len(input) > n ):

                                pet_lover = input[n]      
                                n         = increment(n)
                                pet_lover = pet_lover.strip().lower()
                                debug_functions.debugVariable('pet_lover', pet_lover)

                                new_texts.append('Your answer: ' + pet_lover)

                                if pet_lover == 'y':
                                    pet = None
                                    while pet == None:
                                        pet_list = Witch.choosePet(new_texts, input, n)
                    
                                        new_texts   = pet_list[0]
                                        input       = pet_list[1]
                                        n           = pet_list[2]

                                        if (len(pet_list) == 4):
                                            pet = pet_list[3]
                                        else:
                                            pet = None

                                else:
                                    pet = None

                                # creating a witch
                                '''
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
                                '''

                                witch = Witch(forest, pet, witch_name)
                                debug_functions.debugVariable('witch.get_art()', witch.get_art())

                                new_texts.append(f'Congratulations! You were reborn as a witch named {witch.get_name()}!') 
                                # new_texts.append(witch.get_art())

                                if witch.get_familiar() is not None:
                                    new_texts.append(witch.adoptPet())


                                # ---------- START THE GAME ---------#

                                # level=1, end_of_level=False, game_over=True
                                game = Game()
                                game.startNewGame()

                                new_texts.append('Would you like to enter the forest now? (y/n)')
                                new_texts_str = '$'.join(new_texts)
                                requests.put(url=config.URL, json={'texts': new_texts_str})

                                if( len(input) > n ):

                                    forest_confirmation = input[n]      
                                    n                   = increment(n)
                                    forest_confirmation = forest_confirmation.strip().lower()

                                    new_texts.append('Your answer: ' + forest_confirmation)  

                                    if forest_confirmation != 'y':

                                        new_texts.append(f"Goodbye, {player_name}. Come back when you're ready to tackle this challenge.")
                                        new_texts_str = '$'.join(new_texts)
                                        requests.put(url=config.URL, json={'texts': new_texts_str})
                        
                                    else:

                                        # ---------- ENTERING THE FOREST ---------#

                                        # let witch enter the start point
                                        new_texts.append(witch.get_forest().enterCell())  

                                        # ---------- START INTERACTION LOOP ---------#

                                        while not game.get_game_over():

                                            new_texts.append('Enter any letter to see your current options.')
                                            new_texts_str = '$'.join(new_texts)
                                            requests.put(url=config.URL, json={'texts': new_texts_str})

                                            if( len(input) > n ):

                                                option = input[n]      
                                                n      = increment(n)

                                                # ---------- PRESENT OPTIONS ---------#

                                                options_pet                 = gameplay_snippets.input_list_with_pet
                                                options_no_pet              = gameplay_snippets.input_list_no_pet
                                                options_for_pet_interaction = gameplay_snippets.input_pet_interaction_list
                                                actions                     = gameplay_snippets.output_list_with_pet
                                                pet_interactions            = gameplay_snippets.output_pet_interaction_list

                                                # print prompt depending on whether the witch has a pet
                                                if witch.get_familiar() is None:

                                                    new_texts.append('This is what you could do now:')
                                                  
                                                    for string in options_no_pet:
                                                        new_texts.append(string)  
                                                    
                                                    new_texts.append('Choose wisely: ')
                                                    new_texts_str = '$'.join(new_texts)
                                                    requests.put(url=config.URL, json={'texts': new_texts_str})   

                                                    if( len(input) > n ):

                                                        action = input[n]      
                                                        n      = increment(n)
                                                        action = action.strip().lower()

                                                        new_texts.append('Your answer: ' + action) 

                                                    else: 
                                                        break
                                                else:
                                                    new_texts.append('This is what you could do now:') 

                                                    for string in options_pet:
                                                        new_texts.append(string)  

                                                    new_texts.append('Choose wisely: ')
                                                    new_texts_str = '$'.join(new_texts)
                                                    requests.put(url=config.URL, json={'texts': new_texts_str})

                                                    if( len(input) > n ):   
                                                        action = input[n]      
                                                        n      = increment(n)
                                                        action = action.strip().lower()

                                                        new_texts.append('Your answer: ' + action) 
                                                    
                                                    else:
                                                        break

                                                # ---------- EXECUTE ACTION ---------#

                                                try:
                                                    # preparation for constructing the chosen method
                                                    args = None
                                                    method_reference = lambda method: getattr(witch, method)

                                                    # get the chosen method and its arguments from the actions list
                                                    method = actions[action]
                                                    if type(method) == tuple:
                                                        method_name, args = method
                                                    else:
                                                        method_name = method

                                                    # ---------- QUIT GAME ---------#
                                                    if method_name == 'quit':
                                                        game.quitGame()

                                                        new_texts.append(f"Goodbye, {player_name}. Come back when you're ready to continue.")
                                                        new_texts_str = '$'.join(new_texts)
                                                        requests.put(url=config.URL, json={'texts': new_texts_str})

                                                    # ---------- PRESENT PET OPTIONS ---------#

                                                    elif method_name == 'interactWithPet':

                                                        new_texts.append(f'How would you like to interact with {witch.get_familiar().get_name()}?') 

                                                        for string in options_for_pet_interaction:
                                                            new_texts.append(string)
                                                        
                                                        new_texts.append('Choose interaction: ')
                                                        new_texts_str = '$'.join(new_texts)
                                                        requests.put(url=config.URL, json={'texts': new_texts_str})

                                                        if( len(input) > n ):

                                                            interaction = input[n]      
                                                            n           = increment(n)

                                                            interaction = interaction.strip().lower()
                                                            new_texts.append('Your answer: ' + interaction)

                                                            # ---------- EXECUTE PET INTERACTION ---------#

                                                            # get the chosen method from the interactions list
                                                            method = pet_interactions[interaction]

                                                            # ---------- QUIT GAME ---------#
                                                            if interaction == 'quit':
                                                                game.quitGame()

                                                                new_texts.append(f"Goodbye, {player_name}. Come back when you're ready to continue.")
                                                                new_texts_str = '$'.join(new_texts)
                                                                requests.put(url=config.URL, json={'texts': new_texts_str})

                                                            # ---------- PET INTERACTIONS ---------#
                                                            else:
                                                                # create a reference of the pet interaction method
                                                                method = method_reference(method)

                                                                # call the method
                                                                new_texts.append(method())  

                                                        else:
                                                            break

                                                    # ---------- EXECUTE OTHER ACTIONS ---------#
                                                    else:
                                                        # create a reference of the method if it's not a pet interaction
                                                        method = method_reference(method_name)

                                                        # call the method
                                                        if args is None:
                                                            new_texts.append(method()) 
  
                                                        else:
                                                            new_texts.append(method(args))  
                                                            
                                                except KeyError:
                                                    new_texts.append('This is not a valid action.')

                                            else:
                                                break

