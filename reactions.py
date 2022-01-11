synergy_list = [
    #((Element 1, Element 2), (Replacement 1, Replacement 2), Money from Replacement)
    # Note: Element 1/2 can either be one element or possible elements available for the reaction.
    #           If the reaction is not a replacement reaction, meaning the elements stay the same
    #           but there is gold earnt from it (an adjacency bonus reaction), 
    #           (Replacement 1, Replacement 2) should be ("No Change")
    #   Element 1 --> Replacement 1, Element 2 --> Replacement 2.
    (("Earth", "Air"), ("Dust", "Empty"), 3), 
    (("Fire", "Air"), ("Energy", "Empty"), 3), 
    (("Earth", "Fire"), ("Lava", "Empty"), 3), 
    (("Earth", "Water"), ("Clay", "Empty"), 3), 
    (("Water", ("Fire", "Energy")), ("Steam", "Empty"), 3), 
    (("Steam", "Cold"), ("Water", "Empty"), 3), 
    (("Ice", ("Fire", "Energy")), ("Water", "Empty"), 5), 
    (("Lava", ("Water", "Cold", "Ice", "Snow")), ("Stone", "Empty"), 3), 
    (("Stone", "Fire"), ("Metal", "Empty"), 3),
    (("Dust", "Dust"), ("Sand", "Empty"), 3), 
    (("Wind", ("Dust", "Ash")), ("Wind", "Empty"), 5), 
    (("Wind", ("Ceramic", "Glassware")), ("Wind", "Empty"), 25), 
    (("Stone", ("Ceramic", "Glassware")), ("Stone", "Empty"), 15), 
    (("Metal", "Energy"), ("Electricity", "Empty"), 3), 
    (("Metal", "Electricity"), ("No Change"), 5), 
    (("Electricity", "Gold"), ("No Change"), 5), 
    (("Gold", "Gold"), ("No Change"), 2), 
    (("Clay", "Fire"), ("Ceramic", "Empty"), 3), 
    (("Sand", "Fire"), ("Glassware", "Empty"), 3), 
    (("Glassware", ("Ceramic", "Alcohol")), ("No Change"), 5), 
    (("Ceramic", "Ceramic"), ("No Change"), 3), 
    (("Glassware", "Glassware"), ("No Change"), 3), 
    (("Steam", "Steam"), ("Cloud", "Empty"), 3), 
    (("Cloud", ("Steam", "Cloud")), ("Rain", "Empty"), 3), 
    (("Rain", "Electricity"), ("Thunder", "Empty"), 3), 
    (("Thunder", "Rain"), ("No Change"), 3), 
    (("Thunder", "Thunder"), ("Thunder", "Empty"), 30),
    (("Rain", "Rain"), ("Rain", "Empty"), 30),  
    
    # pyromaniac    
    (("Fire", ("Wood", "Boat")), ("Fire", "Coal"), 30), 
    (("Fire", ("Plants", "Dust", "Cactus")), ("Fire", "Ash"), 50),

    (("Coal", "Water"), ("Oil", "Empty"), 3), 
    (("Coal", "Air"), ("Natural Gas", "Empty"), 3), 

    (("Fire", "Coal"), ("Fire", "Carbon Dioxide"), 150), 
    (("Fire", "Oil"), ("Fire", "Carbon Dioxide"), 175), 
    (("Fire", "Natural Gas"), ("Fire", "Carbon Dioxide"), 200), 

    (("Fire", "Alcohol"), ("Fire", "Fire"), 30), 

    (("Plants", ("Ash", "Carbon Dioxide")), ("Plants", "Empty"), 15), 
    (("Cactus", ("Ash", "Carbon Dioxide")), ("Plants", "Empty"), 15),
    (("Ocean", "Carbon Dioxide"), ("Ocean", "Empty"), 15), 
        # also see: phoenix things (eats ash, gains from fire)

    # cold things
    (("Water", "Air"), ("Cold", "Empty"), 3), 
    (("Water", "Cold"), ("Ice", "Empty"), 3), 
    (("Rain", ("Cold", "Ice")), ("Snow", "Empty"), 3), 
    (("Cloud", ("Cold", "Ice")), ("Snow", "Empty"), 3), 
    (("Snow", "Snow"), ("Avalanche", "Empty"), 3), 
    (("Snow", "Human"), ("Snowman", "Human"), 3), 
    (("Snow", ("Avalanche", "Snowman")), ("No Change"), 5), 
    (("Snow", "Fire"), ("Empty", "Fire"), 5), 
    (("Avalanche", "Fire"), ("Empty", "Fire"), 25), 
    (("Snowman", "Fire"), ("Empty", "Fire"), 50), 
    (("Avalanche", "Snowstorm"), ("Snow", "Snow"), 15), 

    # living (or close enough) things:
    (("Clay", "Energy"), ("Life", "Empty"), 3), 

    (("Metal", "Life"), ("Robot", "Empty"), 3),         # robotic
    (("Electricity", "Life"), ("AI", "Empty"), 3), 
    (("Robot", "AI"), ("Android", "Empty"), 3), 
    (("Robot", "Electricity"), ("Robot", "Electricity"), 5), 
    (("AI", "Electricity"), ("AI", "Electricity"), 5), 
    ((("AI", "Robot"), "Music"), ("Vocaloid", "Empty"), 3), 

    (("Stone", "Life"), ("Egg", "Empty"), 3),             # animals
    (("Egg", ("Fire", "Air", "Energy")), ("Bird", "Empty"), 3), 
    (("Egg", ("Love", "Life")), ("Bird", "Empty"), 40), 
    (("Bird", "Stone"), ("Bird", "Egg"), 3), 
    (("Bird", ("Air", "Wind")), ("No Change"), 5), 
    ((("Egg", "Bird"), "Water"), ("Fish", "Empty"), 3), 
    (("Ocean", ("Egg", "Bird")), ("Fish", "Empty"), 3), 
    ((("Bird", "Egg"), ("Earth", "Mountain")), ("Beast", "Empty"), 3), 
    (("Bird", "Fire"), ("Phoenix", "Empty"), 3), 
    (("Phoenix", ("Ash", "Fire")), ("Phoenix", "Empty"), 25), 
    (("Beast", "Bird"), ("Dragon", "Empty"), 3), 
    (("Dragon", ("Phoenix", "Gold")), ("No Change"), 25), 

    (("Earth", "Life"), ("Plants", "Empty"), 3),          # plants
    (("Plants", "Water"), ("Plants", "Water"), 5), 
    (("Plants", "Rain"), ("No Change"), 5), 
    (("Beast", "Plants"), ("Beast", "Seeds"), 10), 
    (("Bird", "Plants"), ("Bird", "Seeds"), 10), 
    (("Fish", "Plants"), ("Fish", "Seeds"), 10), 
    (("Bird", "Seeds"), ("Bird", "Empty"), 30), 
    (("Phoenix", "Seeds"), ("Phoenix", "Empty"), 30), 
    (("Fish", "Plants"), ("Fish", "Seeds"), 30), 
    (("Plants", "Plants"), ("No Change"), 3), 
    (("Sand", ("Plants", "Seeds")), ("Cactus", "Empty"), 3),
    (("Cactus", "Sand"), ("No Change"), 3), 
    (("Earth", "Plants"), ("Wood", "Empty"), 3), 
    (("Seeds", "Water"), ("Wood", "Empty"), 30), 
    (("Earth", "Seeds"), ("Wood", "Empty"), 30), 

    (("Clay", "Life"), ("Human", "Empty"), 3),            # humans
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
    (("Angler", "Fish"), ("Angler", "Empty"), 50), 
    (("Miner", "Volcano"), ("Miner", "Lava"), 3), 
    (("Miner", "Mountain"), ("Miner", "Stone"), 3), 
    (("Miner", "Stone"), ("Miner", "Metal"), 3), 
    (("Miner", "Metal"), ("Miner", "Gold"), 3), 
    (("Miner", "Gold"), ("Miner", "Coal"), 3), 
    (("Human", "Gold"), ("Pirate", "Empty"), 3), 
    (("Pirate", "Gold"), ("Pirate", "Empty"), 5), 
    (("Human", ("Alcohol", "Cola")), ("Human", "Empty"), 15), 
    (("Miner", ("Alcohol", "Cola")), ("Miner", "Empty"), 15), 
    (("Angler", ("Alcohol", "Cola")), ("Miner", "Empty"), 15), 
    (("Pirate", ("Alcohol", "Cola")), ("Pirate", "Empty"), 15), 
    (("Hero", ("Alcohol", "Cola")), ("Hero", "Empty"), 15), 
    (("Hero", "Pirate"), ("Hero", "Human"), 30), 
    (("Pirate", ("Ceramic", "Glassware")), ("Pirate", "Empty"), 25), 
    (("Hero", ("Ceramic", "Glassware")), ("Hero", "Empty"), 25), 
    
    (("Robot", "Robot"), ("No Change"), 3),                # synergies amongst selves
    ((("Robot", "AI"), "Android"), ("No Change"), 5), 
    (("Android", "Android"), ("No Change"), 3),
    (("Human", "Beast"), ("No Change"), 5), 
    (("Bird", "Bird"), ("No Change"), 3), 
    (("Bird", "Fish"), ("Bird", "Empty"), 20), 
    (("Beast", "Fish"), ("Beast", "Empty"), 20), 
    (("Fish", ("Water", "Fish")), ("No Change"), 3),
    (("Beast", "Beast"), ("No Change"), 3), 
    ((("Human", "Beast", "Bird", "Phoenix", "Dragon", "Android", "Plants", "Cactus", "Angler", "Miner", "Pirate", 
        "Vocaloid", "Hero"), "Love"), ("No Change"), 10), 
    ((("Human", "Beast", "Phoenix", "Dragon", "Android", "Plants", "Cactus", "Angler", "Miner", 
        "Hero"), "Music"), ("No Change"), 5), 
    ((("Bird", "Pirate", "Vocaloid", "Hero"), "Music"), ("No Change"), 10), 
    ((("Human", "Android", "Angler", "Miner", "Pirate", "Hero"), "Snowman"), ("No Change"), 5), 
    
    (("Pirate", ("Boat", "Ocean", "Beach")), ("No Change"), 5), 
    (("Miner", ("Bird", "Human", "Angler")), ("No Change"), 5), 
    (("Angler", ("Human", "Ocean", "Beach", "Boat")), ("No Change"), 5), 
    ((("Human", "Beast", "Bird", "Phoenix", "Dragon", "Android", "Plants", "Cactus", "Angler", "Miner", 
        "Hero"), "Vocaloid"), ("No Change"), 5), 

    (("Vocaloid", "Pirate"), ("No Change"), 15), 
    (("Vocaloid", "Vocaloid"), ("No Change"), 5), 
    (("Angler", "Angler"), ("No Change"), 3), 
    (("Pirate", "Pirate"), ("No Change"), 3), 

    # phenomena / other disasters
    (("Air", "Air"), ("Wind", "Empty"), 3),                       # swirly lads
    (("Wind", "Wind"), ("Tornado", "Empty"), 3), 
    (("Tornado", "Dust"), ("Duststorm", "Empty"), 3), 
    (("Duststorm", "Dust"), ("No Change"), 5), 
    (("Blizzard", "Snow"), ("No Change"), 5), 
    (("Tornado", ("Ice", "Snow", "Cold")), ("Blizzard", "Empty"), 3),
    (("Tornado", "Sand"), ("Sandstorm", "Empty"), 3), 
    (("Sandstorm", "Sand"), ("Sandstorm", "Sand"), 5), 
    (("Tornado", ("Water", "Steam")), ("Hurricane", "Empty"), 3), 
    (("Tornado", ("Ceramic", "Glassware")), ("Tornado", "Empty"), 25),
    (("Ocean", "Tornado"), ("Hurricane", "Empty"), 3), 
    (("Ocean", ("Steam", "Fire", "Wind", "Rain")), ("Hurricane", "Empty"), 3), 
    (("Ocean", "Hurricane"), ("No Change"), 5), 
    (("Hurricane", "Hurricane"), ("Hurricane", "Empty"), 25), 
    (("Tornado", "Tornado"), ("Tornado", "Empty"), 25), 
    (("Duststorm", "Duststorm"), ("Duststorm", "Empty"), 25), 
    (("Blizzard", "Blizzard"), ("Blizzard", "Empty"), 25), 
    (("Sandstorm", "Sandstorm"), ("Sandstorm", "Empty"), 25), 
    (("Hurricane", "Cold"), ("Water", "Empty"), 25), 
    (("Tornado", "Wind"), ("No Change"), 5), 
    ((("Tornado", "Hurricane", "Sandstorm", "Duststorm", "Blizzard"), "Wind"), ("Empty", "Empty"), 25), 

    (("Earth", ("Earth", "Earthquake", "Stone", "Clay")), ("Mountain", "Empty"), 3),          # rocky lads
    (("Stone", "Stone"), ("Mountain", "Empty"), 3), 
    (("Mountain", "Mountain"), ("No Change"), 3), 
    (("Mountain", ("Stone", "Dust")), ("Mountain", "Empty"), 5),
    (("Mountain", "Lava"), ("Volcano", "Empty"), 3), 
    (("Volcano", "Lava"), ("No Change"), 5), 
    (("Volcano", ("Ice", "Water", "Cold")), ("Mountain", "Empty"), 15), 
    (("Mountain", "Volcano"), ("No Change"), 5), 
    (("Earth", "Energy"), ("Earthquake", "Empty"), 3), 
    (("Mountain", ("Tornado", "Energy", "Earthquake")), ("Landslide", "Empty"), 3), 
    (("Landslide", ("Stone", "Dust")), ("Landslide", "Empty"), 5), 
    (("Mountain", "Landslide"), ("No Change"), 5), 

    (("Ocean", "Earthquake"), ("Tsunami", "Empty"), 3),           # tsunami, also an ocean thing
    (("Wave", "Wave"), ("Tsunami", "Empty"), 3), 
    ((("Ocean", "Beach"), "Tsunami"), ("No Change"), 5), 
    (("Tsunami", "Tsunami"), ("Tsunami", "Empty"), 25), 

    # ocean things
    (("Water", "Water"), ("Ocean", "Empty"), 3),                  # ocean/wave/sand
    (("Ocean", ("Wind", "Ocean", "Energy")), ("Wave", "Empty"), 3), 
    (("Stone", ("Wave", "Cold", "Wind")), ("Sand", "Empty"), 8), 
    (("Ocean", "Stone"), ("Ocean", "Sand"), 8), 
    (("Ocean", "Fire"), ("Ocean", "Steam"), 3), 

    
    (("Ocean", "Sand"), ("Beach", "Empty"), 3),                    # fish/beach/island 
    (("Beach", "Wave"), ("No Change"), 8), 
    (("Beach", "Sand"), ("Beach", "Empty"), 10), 
    (("Ocean", ("Wave", "Beach", "Fish", "Boat")), ("No Change"), 5),
    (("Ocean", ("Volcano", "Lava", "Mountain")), ("Island", "Empty"), 3), 
    (("Sand", "Sand"), ("No Change"), 3), 
    (("Island", ("Ocean", "Plants", "Fish")), ("No Change"), 5), 
    (("Island", "Island"), ("No Change"), 3), 
    (("Island", "Sand"), ("Island", "Empty"), 10), 
    (("Ocean", ("Wood", "Metal")), ("Ocean", "Boat"), 3),
    (("Boat", "Boat"), ("No Change"), 3), 
    ((("Tsunami", "Hurricane"), "Boat"), ("Ocean", "Empty"), 25), 


]

def check_for_synergy(elements):            # takes in tuple of elements to check    

    for synergy in synergy_list:
        if elements[0] in synergy[0][0] and elements[1] in synergy[0][1]:   # if the elements match
            if synergy[1] == "No Change":   # if the reaction is an adjacency bonus
                return (True, (elements, elements, synergy[2]))   
            else:                           # if the reaction is a transformation reaction
                return (True, (elements, synergy[1], synergy[2])) 

    return (False, None)        # returns that no synergy is present if none was found.
