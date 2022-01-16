synergy_list = [
    #((Element 1, Element 2), (Replacement 1, Replacement 2), Money from Replacement)
    # Note: Element 1/2 can either be one element or possible elements available for the reaction.
    #           If the reaction is not a replacement reaction, meaning the elements stay the same
    #           but there is gold earnt from it (an adjacency bonus reaction), 
    #           (Replacement 1, Replacement 2) should be ("No Change")
    #   Element 1 --> Replacement 1, Element 2 --> Replacement 2.
    (("Earth", "Air"), ("Dust", "Empty"), 3), 
    (("Fire", "Air"), ("Energy", "Empty"), 3), 
    (("Light", ("Light", "Air", "Fire")), ("Energy", "Empty"), 15), 
    (("Fire", "Cold"), ("Air", "Empty"), 3), 
    (("Earth", "Fire"), ("Lava", "Empty"), 3), 
    (("Fire", "Fire"), ("Light", "Empty"), 3), 
    (("Earth", "Water"), ("Clay", "Empty"), 3), 
    (("Water", ("Fire", "Energy")), ("Steam", "Empty"), 3), 
    ((("Steam", "Energy"), "Cold"), ("Water", "Empty"), 3), 
    (("Ice", ("Fire", "Energy")), ("Water", "Empty"), 5), 
    (("Lava", ("Water", "Cold", "Ice", "Snow")), ("Stone", "Empty"), 3), 
    (("Stone", "Fire"), ("Metal", "Empty"), 3),
    (("Dust", "Dust"), ("Sand", "Empty"), 3), 
    (("Wind", ("Dust", "Ash", "Tumbleweed")), ("Wind", "Empty"), 5), 
    (("Wind", ("Ceramic", "Glassware")), ("Wind", "Empty"), 25), 
    (("Stone", ("Ceramic", "Glassware")), ("Stone", "Empty"), 25), 
    (("Metal", "Energy"), ("Electricity", "Empty"), 3), 
    (("Metal", "Electricity"), ("No Change"), 5), 
    (("Electricity", "Gold"), ("No Change"), 5), 
    (("Gold", "Gold"), ("No Change"), 2), 
    (("Clay", "Fire"), ("Ceramic", "Empty"), 3), 
    (("Sand", "Fire"), ("Glassware", "Empty"), 3), 
    (("Glassware", ("Ceramic", "Alcohol", "Water")), ("No Change"), 5), 
    (("Ceramic", "Ceramic"), ("No Change"), 3), 
    (("Glassware", "Glassware"), ("No Change"), 3), 
    (("Steam", "Steam"), ("Cloud", "Empty"), 3), 
    (("Cloud", ("Steam", "Cloud", "Water")), ("Rain", "Empty"), 3), 
    ((("Rain", "Cloud"), ("Electricity", "Energy")), ("Thunder", "Empty"), 3), 
    (("Thunder", "Rain"), ("No Change"), 3), 
    (("Thunder", "Thunder"), ("Thunder", "Empty"), 250),
    (("Rain", "Rain"), ("Rain", "Empty"), 200),  
    ((("Rain", "Thunder", "Cloud"), "Wind"), ("Empty", "Empty"), 25),  
    
    # pyromaniac    
    (("Fire", ("Wood", "Boat", "House")), ("Fire", "Coal"), 30), 
    (("Fire", ("Plants", "Dust", "Cactus", "Tumbleweed")), ("Fire", "Ash"), 50),

    (("Coal", "Water"), ("Oil", "Empty"), 3), 
    (("Coal", "Air"), ("Natural Gas", "Empty"), 3), 

    (("Fire", "Coal"), ("Fire", "Carbon Dioxide"), 150), 
    (("Fire", "Oil"), ("Fire", "Carbon Dioxide"), 175), 
    (("Fire", "Natural Gas"), ("Fire", "Carbon Dioxide"), 200), 

    (("Fire", "Alcohol"), ("Fire", "Fire"), 75), 

    (("Plants", ("Ash", "Carbon Dioxide")), ("Plants", "Empty"), 15), 
    (("Cactus", ("Ash", "Carbon Dioxide")), ("Cactus", "Empty"), 15),
    (("Ocean", "Carbon Dioxide"), ("Ocean", "Empty"), 15), 

    # cold things
    (("Water", "Air"), ("Cold", "Empty"), 3), 
    (("Water", "Cold"), ("Ice", "Empty"), 3), 
    (("Rain", ("Cold", "Ice")), ("Snow", "Empty"), 3), 
    (("Cloud", ("Cold", "Ice")), ("Snow", "Empty"), 3), 
    (("Snow", ("Energy", "Landslide")), ("Avalanche", "Empty"), 3), 
    (("Snow", "Human"), ("Snowman", "Human"), 3), 
    (("Avalanche", "Blizzard"), ("Snow", "Snow"), 15), 
    (("Earth", ("Ice", "Snow", "Cold")), ("Permafrost", "Empty"), 3), 
    (("Ice", ("Ice", "Snow")), ("Glacier", "Empty"), 3), 

    (("Snow", "Snow"), ("No Change"), 5), 
    (("Glacier", "Ocean"), ("No Change"), 5), 
    (("Snow", ("Glacier", "Permafrost", "Snowman", "Avalanche")), ("No Change"), 5), 
    ((("Glacier", "Permafrost"), ("Ice", "Cold")), ("No Change"), 8), 
    (("Glacier", "Glacier"), ("No Change"), 5),  
    (("Permafrost", "Permafrost"), ("No Change"), 5), 
    (("Penguin", ("Permafrost", "Snow", "Glacier", "Ocean", "Cold", "Ice")), ("No Change"), 8), 

    # cold synergy with fire & carbon dioxide
    (("Snow", ("Fire", "Energy")), ("Empty", "Empty"), 50), 
    (("Avalanche", ("Fire", "Energy")), ("Empty", "Empty"), 75), 
    (("Snowman", ("Fire", "Energy")), ("Empty", "Empty"), 125),     
    (("Glacier", ("Fire", "Energy")), ("Water", "Carbon Dioxide"), 75), 
    (("Permafrost", ("Fire", "Energy")), ("Earth", "Carbon Dioxide"), 75),

    (("Volcano", ("Snow", "Snowman", "Avalanche", "Glacier")), ("Mountain", "Water"), 50),
    (("Volcano", "Permafrost"), ("Mountain", "Earth"), 50), 
    (("Lava", ("Snow", "Snowman", "Avalanche", "Glacier")), ("Stone", "Water"), 50), 
    (("Lava", "Permafrost"), ("Stone", "Earth"), 50), 

    (("Glacier", "Carbon Dioxide"), ("Glacier", "Empty"), 25), 
    (("Permafrost", "Carbon Dioxide"), ("Permafrost", "Empty"), 25), 
    (("Snow", "Carbon Dioxide"), ("Snow", "Empty"), 25), 
    (("Ice", "Carbon Dioxide"), ("Ice", "Empty"), 25), 
    (("Snowman", "Carbon Dioxide"), ("Snowman", "Empty"), 25), 
    (("Avalanche", "Carbon Dioxide"), ("Avalanche", "Empty"), 25), 

    # living (or close enough) things:
    (("Clay", "Energy"), ("Life", "Empty"), 3), 

    (("Metal", "Life"), ("Robot", "Empty"), 3),         # robotic
    (("Electricity", "Life"), ("AI", "Empty"), 3), 
    (("Robot", "AI"), ("Android", "Empty"), 3), 
    (("Robot", "Electricity"), ("Robot", "Electricity"), 5), 
    (("AI", "Electricity"), ("AI", "Electricity"), 5), 
    ((("AI", "Robot"), "Music"), ("Vocaloid", "Empty"), 3), 

    (("Stone", "Life"), ("Egg", "Empty"), 3),             # animals
    (("Egg", ("Fire", "Air", "Wind", "Energy")), ("Bird", "Empty"), 3), 
    (("Egg", ("Love", "Life")), ("Bird", "Empty"), 40), 
    (("Bird", "Stone"), ("Bird", "Egg"), 3), 
    ((("Bird", "Egg"), ("Snow", "Ice", "Cold")), ("Penguin", "Empty"), 3), 
    (("Bird", ("Air", "Wind")), ("No Change"), 5), 
    ((("Egg", "Bird"), "Water"), ("Fish", "Empty"), 3),
    ((("Bird", "Egg"), "Ocean"), ("Fish", "Ocean"), 3), 
    (("Beast", "Ocean"), ("Turtle", "Ocean"), 3), 
    (("Beast", "Water"), ("Turtle", "Empty"), 3), 
    (("Fish", ("Earth", "Stone")), ("Turtle", "Empty"), 3), 
    (("Ocean", ("Egg", "Bird")), ("Fish", "Empty"), 3), 
    ((("Bird", "Egg"), ("Earth", "Mountain")), ("Beast", "Empty"), 3),
    ((("Egg", "Bird"), "Lava"), ("Phoenix", "Empty"), 3),  
    (("Bird", "Fire"), ("Phoenix", "Empty"), 3), 
    (("Beast", ("Bird", "Penguin")), ("Dragon", "Empty"), 3), 
    (("Light", "Life"), ("Will o' Wisp", "Empty"), 3), 

    (("Earth", "Life"), ("Plants", "Empty"), 3),            # plants
    (("Plants", ("Light", "Water")), ("Plants", "Empty"), 50), 
    (("Plants", "Seeds"), ("Plants", "Plants"), 3), 
    (("Sand", ("Plants", "Seeds")), ("Cactus", "Empty"), 3),
    (("Cactus", "Light"), ("Cactus", "Empty"), 75), 
    (("Earth", "Plants"), ("Wood", "Empty"), 3), 
    (("Seeds", ("Water", "Earth", "Rain", "Light")), ("Wood", "Empty"), 50), 
    (("Plants", "Wind"), ("Tumbleweed", "Empty"), 3), 

    (("Beast", "Plants"), ("Beast", "Seeds"), 10),          # plant eating
    (("Bird", "Plants"), ("Bird", "Seeds"), 10), 
    (("Fish", "Plants"), ("Fish", "Seeds"), 10), 
    (("Fish", "Plants"), ("Fish", "Seeds"), 30), 
    (("Turtle", "Plants"), ("Turtle", "Seeds"), 30), 
    (("Bird", "Seeds"), ("Bird", "Empty"), 50), 
    (("Phoenix", "Seeds"), ("Phoenix", "Empty"), 50), 

    (("Clay", "Life"), ("Human", "Empty"), 3),              # humans
    (("Human", "Human"), ("Love", "Empty"), 3), 
    (("Wood", ("Air", "Wind")), ("Music", "Empty"), 3), 
    (("Wood", "Clay"), ("House", "Empty"), 3), 
    (("House", "House"), ("No Change"), 3), 
    (("House", ("Human", "Angler", "Miner")), ("No Change"), 15), 
    (("Human", ("Phoenix", "Dragon")), ("Hero", "Empty"), 300), 
    (("Hero", ("Phoenix", "Dragon")), ("Hero", "Empty"), 300), 
    (("Human", "Plants"), ("Human", "Alcohol"), 3), 
    (("Water", "Carbon Dioxide"), ("Cola", "Empty"), 3), 
    (("Human", "Fish"), ("Angler", "Fish"), 3), 
    (("Angler", "Fish"), ("Angler", "Empty"), 75), 
    (("Human", "Mountain"), ("Miner", "Mountain"), 3), 
    (("Miner", "Volcano"), ("Miner", "Lava"), 3), 
    (("Miner", "Mountain"), ("Miner", "Stone"), 3), 
    (("Miner", "Stone"), ("Miner", "Metal"), 3), 
    (("Miner", "Metal"), ("Miner", "Gold"), 3), 
    (("Miner", "Gold"), ("Miner", "Coal"), 3), 
    (("Human", "Gold"), ("Pirate", "Empty"), 3), 
    (("Pirate", "Gold"), ("Pirate", "Empty"), 5), 
    (("Hero", "Pirate"), ("Hero", "Human"), 30), 
    (("Human", ("Light", "Bird")), ("Angel", "Empty"), 3), 

    # drinking drinks and smashing pots
    (("Human", ("Alcohol", "Cola")), ("Human", "Empty"), 75), 
    (("Miner", ("Alcohol", "Cola")), ("Miner", "Empty"), 75), 
    (("Angler", ("Alcohol", "Cola")), ("Angler", "Empty"), 75), 
    (("Pirate", ("Alcohol", "Cola")), ("Pirate", "Empty"), 75), 
    (("Hero", ("Alcohol", "Cola")), ("Hero", "Empty"), 75), 
    (("Angel", "Cola"), ("Angel", "Empty"), 150), 
    (("Pirate", ("Ceramic", "Glassware")), ("Pirate", "Empty"), 25), 
    (("Hero", ("Ceramic", "Glassware")), ("Hero", "Empty"), 25), 
    
    (("Robot", "Robot"), ("No Change"), 3),                # synergies amongst selves
    ((("Robot", "AI"), "Android"), ("No Change"), 5), 
    (("Android", "Android"), ("No Change"), 3),
    (("Human", "Beast"), ("No Change"), 5), 
    (("Bird", "Bird"), ("No Change"), 3), 
    (("Bird", ("Fish", "Turtle")), ("Bird", "Empty"), 50), 
    (("Penguin", "Fish"), ("Penguin", "Empty"), 75), 
    (("Turtle", "Fish"), ("Turtle", "Empty"), 50), 
    (("Beast", ("Fish", "Turtle")), ("Beast", "Empty"), 20), 
    (("Fish", ("Water", "Fish")), ("No Change"), 5),
    (("Beast", "Beast"), ("No Change"), 3), 
    (("Penguin", "Penguin"), ("No Change"), 3), 
    (("Turtle", "Turtle"), ("No Change"), 3), 
    (("Phoenix", ("Ash", "Fire", "Lava")), ("No Change"), 10), 
    (("Dragon", ("Phoenix", "Gold")), ("No Change"), 10),     
    (("Plants", "Rain"), ("No Change"), 5),
    (("Plants", "Plants"), ("No Change"), 3), 
    (("Cactus", "Sand"), ("No Change"), 10), 
    (("Cactus", "Beach"), ("No Change"), 5), 
    
    (("Tumbleweed", ("Earth", "Sand", "Stone", "Clay", "Plants", "Seeds", "Dust")), 
            ("Tumbleweed", "Tumbleweed"), 10),  

    ((("Human", "Beast", "Bird", "Phoenix", "Dragon", "Android", "Plants", "Cactus", "Angler", "Miner", "Pirate", 
        "Vocaloid", "Hero", "Will o' Wisp", "Penguin", "Turtle", "Angel"), "Love"), ("No Change"), 8), 

    ((("Human", "Beast", "Phoenix", "Dragon", "Android", "Plants", "Cactus", "Angler", "Miner", 
        "Hero", "Penguin", "Turtle"), "Music"), ("No Change"), 7),
    ((("Bird", "Pirate", "Vocaloid", "Angel"), "Music"), ("No Change"), 10), 

    ((("Human", "Beast", "Phoenix", "Dragon", "Android", "Plants", "Cactus", "Angler", "Miner", 
    "Hero", "Penguin", "Turtle"), "Vocaloid"), ("No Change"), 5),
    ((("Pirate", "Bird", "Vocaloid", "Angel"), "Vocaloid"), ("No Change"), 10), 

    ((("Beast", "Bird", "Angler", "Miner", "Pirate", "Penguin", "Turtle"), "Light"), ("No Change"), 2),
    ((("Hero", "Will o' Wisp", "Angel"), "Light"), ("No Change"), 7), 

    ((("Human", "Angler", "Miner", "Pirate", "Hero"), "Will o' Wisp"), ("Empty", "Empty"), 150), 
    (("Angel", "Will o' Wisp"), ("Angel", "Empty"), 100),  

    ((("Android", "Robot", "AI", "Vocaloid"), ("Water", "Ocean", "Wave", "Tsunami")), ("Metal", "Empty"), 150), 

    ((("Human", "Android", "Angler", "Miner", "Pirate", "Hero"), "Snowman"), ("No Change"), 5),

    (("House", ("Earthquake", "Tornado", "Blizzard", "Hurricane", "Duststorm", "Sandstorm", "Earthquake", 
        "Landslide", "Avalanche")), ("Empty", "Empty"), 100), 
    
    (("Pirate", ("Boat", "Ocean", "Beach", "Pirate")), ("No Change"), 7),
    (("Miner", ("Bird", "Human", "Angler", "Miner")), ("No Change"), 7), 
    (("Angler", ("Human", "Ocean", "Beach", "Boat", "Angler", "Turtle")), ("No Change"), 7), 
    (("Hero", ("Human", "Angler", "Miner")), ("No Change"), 7), 
    (("Angel", ("Human", "Angler", "Miner", "Bird", "Angel")), ("No Change"), 5),
    (("Angel", "Hero"), ("No Change"), 15),
    (("Angel", ("Phoenix", "Dragon")), ("Empty", "Empty"), 1000), 


    # phenomena / other disasters
    (("Air", "Air"), ("Wind", "Empty"), 3),                       # swirly lads
    (("Wind", "Wind"), ("Tornado", "Empty"), 3), 
    (("Tornado", "Dust"), ("Duststorm", "Empty"), 3), 
    (("Duststorm", "Dust"), ("No Change"), 5), 
    (("Tornado", ("Ice", "Snow", "Cold")), ("Blizzard", "Empty"), 3),
    (("Blizzard", "Snow"), ("No Change"), 5), 
    (("Tornado", "Sand"), ("Sandstorm", "Empty"), 3), 
    (("Sandstorm", "Sand"), ("No Change"), 5), 
    (("Tornado", ("Water", "Steam")), ("Hurricane", "Empty"), 3), 
    (("Ocean", ("Steam", "Fire", "Wind", "Rain", "Tornado")), ("Hurricane", "Empty"), 3), 
    (("Hurricane", ("Ocean", "Steam")), ("No Change"), 10), 
    (("Hurricane", "Cold"), ("Water", "Empty"), 70), 
    ((("Tornado", "Hurricane", "Sandstorm", "Duststorm", "Blizzard"), "Wind"), ("Empty", "Empty"), 25), 
    ((("Tornado", "Hurricane", "Sandstorm", "Duststorm", "Blizzard"), 
    ("Tornado", "Hurricane", "Sandstorm", "Duststorm", "Blizzard")), ("Empty", "Empty"), 50), 
    (("Tornado", ("Ceramic", "Glassware")), ("Tornado", "Empty"), 50),
    (("Hurricane", ("Ceramic", "Glassware")), ("Hurricane", "Empty"), 50),
    (("Sandstorm", ("Ceramic", "Glassware")), ("Sandstorm", "Empty"), 50),
    (("Duststorm", ("Ceramic", "Glassware")), ("Duststorm", "Empty"), 50),
    (("Blizzard", ("Ceramic", "Glassware")), ("Blizzard", "Empty"), 50),

    # rocky lads
    ((("Earth", "Earthquake", "Stone", "Clay"), ("Earth", "Earthquake", "Stone", "Clay")), ("Mountain", "Empty"), 3),
    (("Clay", "Clay"), ("Mountain", "Empty"), 3), 
    (("Mountain", "Mountain"), ("No Change"), 3), 
    (("Mountain", ("Stone", "Dust")), ("Mountain", "Empty"), 5),
    (("Mountain", "Lava"), ("Volcano", "Empty"), 3), 
    (("Volcano", "Lava"), ("No Change"), 5), 
    (("Volcano", ("Ice", "Water", "Cold")), ("Mountain", "Empty"), 15), 
    (("Mountain", "Volcano"), ("No Change"), 5), 
    (("Earth", "Energy"), ("Earthquake", "Empty"), 3), 
    (("Mountain", ("Tornado", "Energy", "Earthquake")), ("Landslide", "Empty"), 3), 
    (("Landslide", ("Stone", "Earth")), ("Earth", "Earth"), 50), 
    (("Mountain", "Landslide"), ("No Change"), 5), 
    (("Landslide", "Landslide"), ("Mountain", "Mountain"), 50), 
    (("Earthquake", ("Ceramic", "Glassware")), ("Earthquake", "Empty"), 25),
    (("Landslide", ("Ceramic", "Glassware")), ("Landslide", "Empty"), 25),  

    (("Ocean", "Earthquake"), ("Tsunami", "Empty"), 3),           # tsunami, also an ocean thing
    (("Wave", ("Wave", "Energy", "Wind")), ("Tsunami", "Empty"), 3), 

    # ocean things
    (("Water", "Water"), ("Ocean", "Empty"), 3),                  # ocean/wave/sand
    (("Ocean", ("Wind", "Ocean", "Energy")), ("Wave", "Empty"), 3), 
    (("Stone", ("Wave", "Cold", "Wind")), ("Sand", "Empty"), 8), 
    (("Ocean", "Stone"), ("Ocean", "Sand"), 8), 
    (("Ocean", "Fire"), ("Ocean", "Steam"), 3), 
    (("Ocean", ("Volcano", "Lava", "Mountain")), ("Island", "Empty"), 3), 
    (("Ocean", ("Wood", "Metal")), ("Ocean", "Boat"), 3),
    (("Ocean", "Sand"), ("Beach", "Empty"), 3),
    
    (("Beach", ("Tsunami", "Hurricane")), ("Sand", "Ocean"), 100),
    (("Tsunami", ("Tsunami", "Hurricane")), ("Ocean", "Ocean"), 50), 

    (("Beach", ("Sand", "Wave")), ("Beach", "Empty"), 75), 
    (("Island", "Sand"), ("Island", "Empty"), 75), 
    ((("Tsunami", "Hurricane"), "Boat"), ("Ocean", "Empty"), 200), 

    (("Ocean", ("Wave", "Beach", "Fish", "Boat", "Tsunami")), ("No Change"), 10),
    (("Island", ("Ocean", "Plants", "Fish")), ("No Change"), 10), 
    (("Sand", "Sand"), ("No Change"), 5), 
    (("Island", "Island"), ("No Change"), 5), 
    (("Boat", "Boat"), ("No Change"), 5), 
    (("Turtle", ("Beach", "Ocean", "Island")), ("No Change"), 5),
]

def x_in_y(element, group):         # The regular "in" function can't diffrentiate properly between
    if type(group) is str:          # things like "Earth" and "Earthquake", hence I had to make my own.
        if element == group:
            return True
    elif type(group) is tuple:
        for thing in group:
            if element == thing:
                return True
    return False

def check_for_synergy(elements):            # takes in tuple of elements to check    
    for synergy in synergy_list:
        if x_in_y(elements[0], synergy[0][0]) and x_in_y(elements[1], synergy[0][1]): # if present
            if synergy[1] == "No Change":   # if the reaction is an adjacency bonus
                return (True, (elements, elements, synergy[2]))   
            else:                           # if the reaction is a transformation reaction
                return (True, (elements, synergy[1], synergy[2])) 

    return (False, None)        # returns that no synergy is present if none was found.

# TODO:
# future plans:
# potentially add food combinations
#   humans eat food
#   food buffs other food
#   beast + human --> cow + human
#   cow + water/plants --> cow + milk
#   milk + ice/snow --> ice cream
#   milk + fire --> cheese
#   egg + cheese --> omelette

# possible symbol: void
# human + void --> mage
# mage + fire/water/earth/air/energy/clay/wind/lava/cold/steam/stone/metal/electricity/sand/ice/light/snow/void
#             --> mage
# empty + void --> void + void

# more mythical creatures
#   could try to use light

# balancing of current strats:
#   Living being strats
#   Burning strats
#   Ocean strats
#   Sandstorm strats
#   Snow strats
#   Gold strats
