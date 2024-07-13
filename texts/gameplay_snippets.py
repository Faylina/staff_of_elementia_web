#---------------------------------------#
#---------- GAMEPLAY SNIPPETS ----------#
#---------------------------------------#

"""Contains the texts necessary for running the main gameplay."""

#---------- TEXT SNIPPETS -----------#

# Introduction

title  = "   _____ _         __  __          __   ______ _                           _   _ "
title += "  / ____| |       / _|/ _|        / _| |  ____| |                         | | (_) "
title += " | (___ | |_ __ _| |_| |_    ___ | |_  | |__  | | ___ _ __ ___   ___ _ __ | |_ _  _"
title += "  \___ \| __/ _` |  _|  _|  / _ \|  _| |  __| | |/ _ \ '_ ` _ \ / _ \ '_ \| __| |/ _` |"
title += "  ____) | || (_| | | | |   | (_) | |   | |____| |  __/ | | | | |  __/ | | | |_| | (_| |"
title += " |_____/ \__\__,_|_| |_|    \___/|_|   |______|_|\___|_| |_| |_|\___|_| |_|\__|_|\__,_|"

intro = ("Welcome, traveler, "  
         "to a world teetering on the edge of chaos. "  
         "In this magical forest, a brave witch embarks on a journey to find the Staff of Elementia, "  
         "a powerful artifact capable of restoring balance to nature. "  
         "As you guide her, you'll encounter dangerous foes, solve puzzles, "  
         "and gather valuable ingredients for potions and spells. "  
         "Will you help the witch restore harmony to the realm, or will you succumb to darkness?")


# player options listed for the player to prompt input
input_list_with_pet = ['check inventory   = Check your inventory',
                       'read spellbook    = Read your spellbook',
                       'interact with pet = Interact with your pet',
                       'move north        = Walk north',
                       'move south        = Walk south',
                       'move east         = Walk east',
                       'move west         = Walk west',
                       'quit              = quit'
                       ]

# player options without pet listed for the player to prompt input
input_list_no_pet = ['check inventory   = Check your inventory',
                     'read spellbook    = Read your spellbook',
                     'move north        = Walk north',
                     'move south        = Walk south',
                     'move east         = Walk east',
                     'move west         = Walk west',
                     'quit              = quit'
                     ]

# map of corresponding methods to the player's input
output_list_with_pet = {'check inventory'   : 'checkInventory',
                        'read spellbook'    : 'readSpellbook',
                        'interact with pet' : 'interactWithPet',
                        'move north'        : ('walk', 'north'),
                        'move south'        : ('walk', 'south'),
                        'move east'         : ('walk', 'east'),
                        'move west'         : ('walk', 'west'),
                        'quit'              : 'quit'
                        }

# player options listed for the player to prompt input for pet interaction
input_pet_interaction_list = [  'call pet       = Call your pet',
                                'look at pet    = Look at your pet',
                                'pet pet        = Pet your pet',
                                'play with pet  = Play with your pet',
                                'feed pet       = Feed your pet',
                                'check hunger   = Check if your pet is hungry',
                                'quit           = quit'
                             ]

# map of corresponding methods to the player's input for pet interaction
output_pet_interaction_list = { 'call pet'      : 'callPet',
                                'look at pet'   : 'lookAtPet',
                                'pet pet'       : 'petPet',
                                'play with pet' : 'playWithPet',
                                'feed pet'      : 'feedPet',
                                'check hunger'  : 'checkPetsHunger',
                                'quit'          : 'quit'
                               }

# cell descriptions for the first level
level1_descriptions = {'1x1': 'You emerge into a sunlit glade, its grassy expanse shimmering with dew. '
                              'In the center of the glade stands an ancient oak tree, '
                              'its branches stretching towards the heavens like the arms of a wise old man. '
                              'Beneath the oak tree, a family of rabbits huddles together, '
                              'their soft fur glowing in the morning light. '
                              'The glade is alive with the songs of birds and the buzzing of insects, '
                              'and you feel a sense of peace and tranquility wash over you. ',
                       '1x2': "You encounter a dense thicket of brambles. "
                              "The brambles twist and writhe, "
                              "forming a maze-like barrier that blocks your path. "
                              "The air is thick with the scent of ripe blackberries, "
                              "tempting you to push through the tangled mess. "
                              "However, the brambles are guarded by a territorial badger, "
                              "its sharp claws and powerful jaws ready to defend its territory. "
                              "You must carefully navigate the brambles, avoiding the badger's wrath, "
                              "to discover what lies beyond.",
                       '1x3': "You find a picturesque waterfall, "
                              "its roar echoing through the tranquil forest. "
                              "The waterfall is a magnificent sight, "
                              "cascading down the rocky slope in a series of steps, "
                              "each one creating a misty veil that hangs in the air. "
                              "At the base of the falls, the water forms a small pool, "
                              "crystal clear and reflecting the verdant surroundings. "
                              "The sound of the water crashing against the rocks fills the air, "
                              "harmonizing with the gentle rustle of the nearby trees. "
                              "The waterfall seems to embody the very essence of nature, "
                              "a testament to the beauty and power of the natural world.",
                       '2x1': 'You discover a towering hillside covered in a blanket of wildflowers. '
                              'The flowers dance in the wind, '
                              'their vibrant petals painting the hillside with a rainbow of colors. '
                              'Atop the hill, a wise old owl perches atop a weathered stone monument, '
                              'its piercing gaze surveying the surrounding forest. '
                              'The owl speaks in a haunting melody, '
                              'sharing ancient wisdom and cryptic prophecies '
                              'with any who dare to seek it out.',
                       '2x2': 'You see a clearing in the enchanted forest. '
                              'The sunlight filters through the dense canopy, '
                              'illuminating the moss-covered stones and the vibrant leaves of the trees. '
                              'In the center of the clearing, there is a majestic oak tree, '
                              'its trunk thick and gnarled, its branches reaching towards the sky. '
                              'As you look closer, you see that the oak tree '
                              'is home to a family of squirrels, '
                              'their fur fluffy and their eyes bright with curiosity.',
                       '2x3': 'You come across a babbling brook that meanders its way through the forest. '
                              'The water sparkles in the dappled light filtering through the trees, '
                              'reflecting the colors of the surrounding foliage. '
                              'The air is fresh and clean, carrying with it the scent of wildflowers '
                              "growing along the brook's edges.",
                       '3x1': 'You discover a hidden valley nestled within the forest. '
                              'The valley is shrouded in mystery and surrounded by an ethereal fog. '
                              'The air is charged with magic, '
                              'and the whispers of ancient spirits fill the space. '
                              'At the heart of the valley lies a mystical lake, '
                              'its surface reflecting the stars in the night sky. '
                              'The water glimmers with iridescent hues, '
                              'inviting you to immerse yourself in its enchanting waters.',
                       '3x2': 'Here lies an enigmatic forest of towering trees '
                              'whose branches intertwine overhead, creating a labyrinth of shadows. '
                              'The trees whisper secrets and riddles, '
                              'challenging you to solve them in exchange for passage. '
                              'Amidst the tangled roots, a serpent slithers, '
                              'its scales shimmering with iridescent hues. '
                              'If you are clever enough to answer the riddles, '
                              'the serpent will lead you to a hidden portal, '
                              'transporting you to a realm beyond you wildest dreams.',
                       '3x3': "There is a towering cliff face that looks out over a vast, uncharted plain. "
                              "The cliff face is home to a colony of peregrine falcons, "
                              "their feathers a brilliant white contrasting with the cool blue of the sky. "
                              "The falcons are protective of their territory, "
                              "and their wingspan casts a shadow over your path. "
                              "But those with a keen eye may notice something peculiar "
                              "in the falcons' flight patterns."
                       }

