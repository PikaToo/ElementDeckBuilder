import pygame
import random

pygame.font.init()
big_font = pygame.font.SysFont('arial', 70)
font = pygame.font.SysFont('arial', 40)
medium_font = pygame.font.SysFont('arial', 30)
small_font = pygame.font.SysFont('arial', 20)
tiny_font = pygame.font.SysFont('arial', 15)

gold_particle_list = []
override_store = False

def reset_gold_particle_list():
    gold_particle_list = []

element_list = (
        ("Air",             1,      " "),
        ("Earth",           1,      " "),
        ("Fire",            1,      " "),
        ("Water",           1,      " "),
        ("Dust",            2,      " "),
        ("Energy",          2,      " "),
        ("Clay",            2,      " "),
        ("Wind",            2,      " "),
        ("Lava",            2,      " "),
        ("Cold",            2,      " "),
        ("Steam",           2,      " "),
        ("Stone",           2,      " "),
        ("Carbon Dioxide",  2,      " "),
        ("Metal",           3,      " "),
        ("Ceramic",         3,      " "),
        ("Tornado",         3,      " "),
        ("Electricity",     3,      " "),
        ("Sand",            3,      " "),
        ("Ice",             3,      " "),
        ("Cloud",           3,      " "),
        ("Mountain",        3,      " "),
        ("Ocean",           3,      " "),
        ("Earthquake",      3,      " "),
        ("Egg",             3,      " "),
        ("Ash",             3,      " "),
        ("Glassware",       4,     " "),
        ("Life",            4,     " "),
        ("Hurricane",       4,     " "),
        ("Rain",            4,     " "),
        ("Volcano",         4,     " "),
        ("Wave",            4,     " "),
        ("Plants",          4,     " "),
        ("Bird",            4,     " "),
        ("Fish",            4,     " "),
        ("House",           4,     " "),
        ("Landslide",       4,     " "),
        ("Gold",            4,     " "),
        ("Sandstorm",       5,     " "),
        ("Cactus",          5,     " "),
        ("Alcohol",         5,     " "),
        ("Cola",            5,     " "),
        ("Angler",          5,     " "),
        ("Miner",           5,     " "),
        ("Blizzard",        5,     " "),
        ("Duststorm",       5,     " "),
        ("Snow",            5,     " "),
        ("Tsunami",         5,     " "),
        ("Robot",           5,     " "),
        ("Island",          5,     " "),
        ("Beach",           5,     " "),
        ("Seeds",           5,     " "),
        ("Wood",            5,     " "),
        ("Coal",            5,     " "),
        ("Oil",             5,     " "),
        ("Natural Gas",     5,     " "),
        ("Boat",            5,     " "),
        ("Human",           6,     " "),
        ("Music",           6,     " "),
        ("Thunder",         6,     " "),
        ("Avalanche",       6,     " "),
        ("Snowman",         6,     " "),
        ("AI",              6,     " "),
        ("Air",             6,     " "),
        ("Beast",           6,     " "),
        ("Pirate",          6,     " "),
        ("Love",            7,     " "),
        ("Android",         7,     " "),
        ("Phoenix",         7,     " "),
        ("Dragon",          7,     " "),
        ("Human",           7,     " "),
        ("Vocaloid",        7,     " "),
        ("Hero",            7,     " "),
    )

def gold_from(element):
    if element == "Empty":
        return 0
    for item in element_list:
        if item[0] == element:
            return item[1]

def description_of(element):
    description = []
    for line in element_list:
        if line[0] == element:
            i = 2
            while i < len(line):
                description.append(line[i])
                i += 1
            return description

def first_empty_slot_in(deck):
    x = 0
    y = 0
    for row in deck:
        for element_ in row:
            if element_ == "Empty":
                return (y, x)
            x += 1
        x = 0
        y += 1

def pick_for_shop(luck):
    # Gives a random selection of items such that their golds per turn are equal to or less than luck.
    shop_list = []
    i = 3
    while len(shop_list) < 4:
        element = ["Empty", luck]
        while element[1] > (luck-i):
            rand = random.randint(0, len(element_list) - 1)
            element = [element_list[rand][0], element_list[rand][1]]
        i -= 1
        i += element[1]
        shop_list.append(element[0])
    return shop_list

def ui(window, gold):
    pygame.draw.rect(window, (30, 30, 30), pygame.Rect(50, 50, 670, 500))
    pygame.draw.rect(window, (40, 40, 40), pygame.Rect(60, 60, 650, 100))
    pygame.draw.rect(window, (40, 40, 40), pygame.Rect(60, 170, 650, 370))
    window.blit(big_font.render("Elements on Board:", False, (255, 255, 255)), (70, 65))

    pygame.draw.rect(window, (30, 30, 30), pygame.Rect(735, 50, 415, 500))
    pygame.draw.rect(window, (40, 40, 40), pygame.Rect(745, 60, 395, 100))
    pygame.draw.rect(window, (40, 40, 40), pygame.Rect(745, 170, 395, 105))
    pygame.draw.rect(window, (40, 40, 40), pygame.Rect(745, 285, 395, 255))
    window.blit(big_font.render("Store:", False, (255, 255, 255)), (755, 65))

    window.blit(font.render("Gold: " + str(gold), False, (200, 200, 50)), (20, 550))

def previous_reactions(window, previous_reactions):
    window.blit(medium_font.render("Previous Turn's Reactions:", False, (180, 180, 180)), (752, 287))
    ry = 320
    for reaction in previous_reactions:
        reactants, products, gold_from_reaction = reaction

        left_side = reactants[0] + " + " + reactants[1] + " --> "
        right_side =  products[0] +  " + " + products[1] + " + " + str(gold_from_reaction) + "g"
        if products[1] == "Empty":
            right_side =  products[0] +  " + " + str(gold_from_reaction) + "g"
            if products[0] == "Empty":
                right_side = str(gold_from_reaction) + "g"
        elif products[0] == "Empty":
                right_side =  products[1] +  " + " + str(gold_from_reaction) + "g"
            
        text = left_side + right_side
        window.blit(tiny_font.render(text, False, (180, 180, 180)), (752, ry))
        ry += 15

def next_cycle(window, touching_mouse, turns, payment):
    if touching_mouse:          # gold
        pygame.draw.rect(window, (100, 100, 50), pygame.Rect(480, 555, 135, 40))
        pygame.draw.rect(window, (110, 110, 60), pygame.Rect(485, 560, 125, 30))
    else:                       # gray
        pygame.draw.rect(window, (50, 50, 50), pygame.Rect(480, 555, 135, 40))
        pygame.draw.rect(window, (60, 60, 60), pygame.Rect(485, 560, 125, 30))
    window.blit(medium_font.render("Next Cycle", False, (200, 200, 200)), (489, 556))
    window.blit(medium_font.render("Cycles 'til Payment: " + str(turns), False, (200, 200, 200)), (900, 556))
    window.blit(medium_font.render("Payment: " + str(payment), False, (200, 200, 200)), (700, 556))

def element_background(window, x, y, mouse_rect, element_selected):
    element_rect = pygame.Rect(x, y, 75, 75)
    element_rect_interior = pygame.Rect(x+5, y+5, 65, 65)

    x = int((x-75)/90)           # converting drawing coordinates to grid coordinates
    y = int((y-184)/89)

    if element_selected == [x, y]:                                      # orange for selected elements
        pygame.draw.rect(window, (150, 100, 40), element_rect)
        pygame.draw.rect(window, (70, 50, 30), element_rect_interior)
    elif (pygame.mouse.get_pressed()[0] and mouse_rect.colliderect(element_rect)):
        pygame.draw.rect(window, (40, 100, 40), element_rect)           # green if clicked
        pygame.draw.rect(window, (30, 50, 30), element_rect_interior)
    elif mouse_rect.colliderect(element_rect):                          # yellow if hovering
        pygame.draw.rect(window, (100, 100, 40), element_rect)
        pygame.draw.rect(window, (50, 50, 30), element_rect_interior)
    else:                                                               # grey if nothing.
        pygame.draw.rect(window, (20, 20, 20), element_rect)
        pygame.draw.rect(window, (30, 30, 30), element_rect_interior)

def shop_background(window, x, y, mouse_rect):
    element_rect = pygame.Rect(x, y, 75, 75)
    element_rect_interior = pygame.Rect(x+5, y+5, 65, 65)

    if mouse_rect.colliderect(element_rect):                          # yellow if hovering
        pygame.draw.rect(window, (100, 100, 40), element_rect)
        pygame.draw.rect(window, (50, 50, 30), element_rect_interior)
    else:                                                               # grey if nothing.
        pygame.draw.rect(window, (20, 20, 20), element_rect)
        pygame.draw.rect(window, (30, 30, 30), element_rect_interior)

def shop_curtains(window):
    curtains = pygame.Surface((415, 225))       # making a surface to get a transparent rect
    curtains.fill((10, 0, 0))                   # making surface dark red
    curtains.set_alpha(200)                     # getting transparency
    window.blit(curtains, (735, 50))

def add_gold(value, x, y):
    # adds values to the list to move (used in next function)
    if value != "0":
        gold_particle_list.append([value, x, y, -3, random.randint(-3, 3)])

def gold_animation(window):
    # moves all values in the list
    for particle in gold_particle_list:
        window.blit(font.render(particle[0], False, (250, 250, 50)), (particle[1], particle[2]))
        particle[1] += particle[4]      # x by the pre-set random velocity
        particle[2] += particle[3]      # y by gravity
        particle[3] += 0.3                # increase gravity
        if particle[2] > 600:
            gold_particle_list.remove(particle)

# <name> = [
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              ",
#     "              "
# ]

icon_dictionary = {
"Air": (
    "      YYY     ",
    "     YY YY    ",
    "    YY   YY   ",
    "   YY     YY  ",
    "   YY  YY  YY ",
    "   YY   YY  YY",
    "    YY   Y   Y",
    "     YY YY   Y",
    "      YYY    Y",
    "            YY",
    "           YY ",
    "          YY  ",
    "        YYY   ",
    "  YYYYYYY     "
),
"Earth": (
    "              ",
    "              ",
    "         GGGG ",
    "       GGGGGG ",
    "      GGGGG   ",
    "      GG      ",
    "      GG      ",
    " GGGGGGGGGGGG ",
    " GbbGbbbGGbbG ",
    " bbbbbbbbbbbb ",
    "  bbbbbbbbbb  ",
    "   bbbbbbbb   ",
    "    bbbbbb    ",
    "              "
),
"Fire": (
    "              ",
    "       YY     ",
    "      YYY     ",
    "     YYOY    ",
    "    YYOOY     ",
    "    OOOO  O   ",
    "   OOOO  OO   ",
    "  OOOR  OORR  ",
    "  OOOR  OORRR ",
    "  OORR OOORRR ",
    "  ORRRROORRRR ",
    "  RRRRRRRRRRR ",
    "   RRRRRRRRR  ",
    "    RRRRRRR   "
),
"Water": (
    "              ",
    "     B        ",
    "     BB       ",
    "      BB      ",
    "     BBBB     ",
    "    BBBBBB    ",
    "   BBBBBBBB   ",
    "   BBBBBBBB   ",
    "  BBBBBBBBBB  ",
    "  BBBBBBBBBB  ",
    "  BBBBBBBBBB  ",
    "   BBBBBBBB   ",
    "    BBBBBB    ",
    "              "
),
"Dust": (
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "    gbbb      ",
    "   gggbbb     ",
    "   gggbbb     ",
    "              "
),
"Energy": (
    "      gg      ",
    " gg  O  g  gg ",
    "g  g g  P g  g",
    " g  gg  gg  g ",
    "  g  g  g  g  ",
    " ggPggggggggg ",
    "g    g  g    g",
    "g    g  O    g",
    " gggggggggPgg ",
    "  g  g  g  g  ",
    " g  gg  gg  g ",
    "g  P g  O g  g",
    " gg  g  g  gg ",
    "      gg      "
),
"Cold": (
    "   ll     ll  ",
    "  ll  l l  ll ",
    " l l   l   l l",
    "    l  l  l   ",
    "     l l l    ",
    "  l   lll   l ",
    "   lllllllll  ",
    "  l   lll   l ",
    "     l l l    ",
    "    l  l  l   ",
    " l l   l   l l",
    "  ll  l l  ll ",
    "   ll     ll  ",
    "              "
),
"Lava": (
    "              ",
    "        YY    ",
    "       YO     ",
    "      OO      ",
    "     OOOO     ",
    "    OOOOOO    ",
    "   RRROOOOO   ",
    "   RRRRROOO   ",
    "  RRRRRRRROO  ",
    "  rrrRRRRRRR  ",
    "  rrrrrrRRRR  ",
    "   rrrrrrrr   ",
    "    rrrrrr    ",
    "              "
),
"Clay": (
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "       bb     ",
    "    bbbbbbb   ",
    "   bbbbbbbbb  "
),
"Steam": (
    "              ",
    "          ww ",
    "   www   wwww ",
    "  wwwwwwwwwww ",
    " wwwwwwwwwww  ",
    " wwwwwwwwww   ",
    "  wwwwwwwww   ",
    "    wwwwwwww  ",
    "    wwwwwwww ",
    "   wwwwwwwwwww",
    "    wwwww www",
    "       ww     ",
    "       ww     ",
    "       ww     "
),
"Stone": (
    "              ",
    "              ",
    "              ",
    "     gggggg   ",
    "    ggggggggg ",
    "   gggggggggg ",
    "  gggggggggg  ",
    "  gggggggggg  ",
    "  gggggggggg  ",
    "   gggggggg   ",
    "    gggggg    ",
    "              ",
    "              ",
    "              "
),
"Metal": (
    "              ",
    "              ",
    "  wwwwwwwwww  ",
    "  wgwwwwwwgw  ",
    "  wwwwwwwwww  ",
    "  wwwwwwwwww  ",
    "  wwwwwwwwww  ",
    "  wwwwwwwwww  ",
    "  wwwwwwwwww  ",
    "  wwwwwwwwww  ",
    "  wgwwwwwwgw  ",
    "  wwwwwwwwww  ",
    "              ",
    "              "
),
"Electricity": (
    "              ",
    "  gwwwwwwwwg  ",
    "  wwwwwYYwww  ",
    "  wwwwYYwwww  ",
    "  wwwYYwwwww  ",
    "  wwYYwwwwww  ",
    "  wYYYYYYYYw  ",
    "  wwwwwwYYww  ",
    "  wwwwwYYwww  ",
    "  wwwwYYwwww  ",
    "  wwwYYwwwww  ",
    "  wwYYwwwwww  ",
    "  gwwwwwwwwg  ",
    "              "
),
"Plants": (
    "      YY      ",
    "      YY      ",
    "    YYPPYY    ",
    "    YYPPYY    ",
    "      YY      ",
    "      YY      ",
    "      GG GGG  ",
    "      GGGG    ",
    "      GG      ",
    "      GG      ",
    "      GG      ",
    "      GG      ",
    "GGGGGGGGGGGGGG",
    "bbbbbbbbbbbbbb"
),
"Life": (
    " l          l ",
    " lYYYRYYPYYYl ",
    "  l        l  ",
    "  l        l  ",
    "   lYYYBYYl   ",
    "    l    l    ",
    "     llll     ",
    "     l  l     ",
    "    l    l    ",
    "   lYPYYYYl   ",
    "  l        l  ",
    "  l        l  ",
    " lYYBYYPYYYYl ",
    " l          l "
),
"Human": (
    "      bb      ",
    "     bbbb     ",
    "     bbbb     ",
    "      bb      ",
    "    bbbbbb    ",
    "   b bbbb b   ",
    "   b bbbb b   ",
    "   b bbbb b   ",
    "   b bbbb b   ",
    "     bbbb     ",
    "     b  b     ",
    "     b  b     ",
    "     b  b     ",
    "     b  b     "
),
"Love": (
    "              ",
    "   RR    RR   ",
    "  RRRR  RRRR  ",
    " RRRRRRRRRRRR ",
    "RRRRRRRRRRRRRR",
    "RRRRRRRRRRRRRR",
    " RRRRRRRRRRRR ",
    " RRRRRRRRRRRR ",
    "  RRRRRRRRRR  ",
    "   RRRRRRRR   ",
    "    RRRRRR    ",
    "     RRRR     ",
    "      RR      ",
    "              "
),
"Robot": (
    "     wwww     ",
    "     wwww     ",
    "     wwww     ",
    "      ww      ",
    "   wwwwwwww   ",
    "   w wwww w   ",
    "   w wwww w   ",
    "   w wwww w   ",
    "   w wwww w   ",
    "     wwww     ",
    "     w  w     ",
    "     w  w     ",
    "     w  w     ",
    "     w  w     "
),
"Ceramic": (
    "     bbbb     ",
    "      bb      ",
    "      bb      ",
    "      bb      ",
    "     bbbb     ",
    "    bbbbbb    ",
    "   bbbbbbbb   ",
    "  bbbbbbbbbb  ",
    " bbbbbbbbbbbb ",
    " bbbbbbbbbbbb ",
    " bbbbbbbbbbbb ",
    "  bbbbbbbbbb  ",
    "   bbbbbbbb   ",
    "    bbbbbb    "
),
"Wind": (
    "        YYYY  ",
    "       YY  YY ",
    "      YY    Y ",
    "       YY  YY ",
    "          YY  ",
    " YYYYYYYYYY   ",
    "              ",
    "        YYYY  ",
    "       YY  YY ",
    "      YY    YY",
    "     YY  YY  Y",
    "      YYYY  YY",
    "           YY ",
    "  YYYYYYYYYY  "
),
"Tornado": (
    "     YYYYYY   ",
    "    YY    YY  ",
    "   YY  YY  YY ",
    "  YY  YY  YY  ",
    "  YY   YYYY   ",
    "   YY       Y ",
    "    YYYY   YY ",
    "     YYYYYYY  ",
    "     YYYYYY   ",
    "      YYYY    ",
    "     YYYY     ",
    "    YYYY      ",
    "     YYY      ",
    "       YY     "
),
"Sand": (
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "      YYYY    ",
    "   YYYYYYYYY  ",
    " YYYYYYYYYYYY "
),
"Sandstorm": (
    "  YY YYYYYY   ",
    " YY YY    YY  ",
    " Y YY      YY ",
    " Y  YY  YY  YY",
    " YY  YYYY   YY",
    "  YY       YY ",
    "   YYYYY  YYY ",
    "    YYYYYYYY  ",
    "     YYYYYY   ",
    "   Y  YYYY    ",
    "     YYYY   Y ",
    "    YYYY      ",
    " Y   YYY   Y  ",
    "       YY     "
),
"Ice": (
    "              ",
    "              ",
    "     BBBBBBBB ",
    "    BlllllBlB ",
    "   BlllllBllB ",
    "  BllBBBBlllB ",
    " BBBBBllBlllB ",
    " BllllllBlllB ",
    " BllllllBlllB ",
    " BllllllBlllB ",
    " BllllllBllB  ",
    " BllllllBBB   ",
    " BlllBBBB     ",
    " BBBBB        "
),
"Blizzard": (
    "     llllll   ",
    "    ll    ll  ",
    "   ll      ll ",
    " l  ll  ll  ll",
    " ll  llll   ll",
    " lll       ll ",
    "  llllll  lll ",
    "   lllllllll  ",
    " l   llllll  l",
    "      llll    ",
    "   l  llll    ",
    "     llll     ",
    "     lll     ",
    "       ll  l  "
),
"Cloud": (
    "     WWWW     ",
    "  WWWWWWWWW   ",
    "WWWWWWWWWWWWW ",
    "   WWWWWWWWWW ",
    "  WWWWWWWWWW  ",
    "   WWWWWWWW   ",
    "              ",
    "       WWWWW  ",
    "      WWWWWWWW",
    "         WWWW ",
    "              ",
    "              ",
    "              ",
    "              "
),
"Rain": (
    "     gggg     ",
    "  ggggggggg   ",
    "gggggggggggg  ",
    " ggggggggggg  ",
    "  ggggg  B    ",
    "         B    ",
    "   B          ",
    "   B  gggggg  ",
    "     gggggggg ",
    " B      gggg  ",
    " B            ",
    "    B   B     ",
    "    B       B ",
    "              "
),
"Thunder": (
    "     gggg     ",
    "  ggggggggg   ",
    "gggggggggggg  ",
    " ggggggggggg  ",
    "  ggggg  B    ",
    "         B    ",
    "  YY          ",
    " YY    ggggg  ",
    "YY    ggggggg ",
    "YYYY    gggg  ",
    "  YY         ",
    " YY     B     ",
    "YY      B   B ",
    "            B "
),
"Snow": (
    "              ",
    "    WWWWWWW   ",
    "  WWWWWWWWWW  ",
    "   WWWWWWWWW  ",
    "    WWWWWW    ",
    "            w ",
    "  w           ",
    "       WWWW   ",
    "      WWWWWW  ",
    "         WW   ",
    "   w          ",
    "           w  ",
    "        w     ",
    "   w          "
),
"Snowman": (
    "              ",
    "     WWWW     ",
    "    WNWWNW    ",
    "    WWWWWW    ",
    "     WWWW     ",
    "    WWWWWW    ",
    "   WWWNNWWW   ",
    "   WWWWWWWW   ",
    "    WWNNWW    ",
    "   WWWWWWWW   ",
    "  WWWWNNWWWW  ",
    "  WWWWWWWWWW  ",
    "  WWWWWWWWWW  ",
    "   WWWWWWWW   "
),
"Avalanche": (
    "              ",
    "              ",
    "              ",
    "      WWWWWW  ",
    "    WWWWWWWWW ",
    "   WWWWWWWWWW ",
    "  WWWWWWWWWWWW",
    " WWWWWWWWWWWW ",
    " WWWWWWW  WWW ",
    " WWWWW     WWW",
    "  WWW       WW",
    "  WWW      WW ",
    " WWWWW        ",
    "  WWWWWW      "
),
"Volcano": (
    "              ",
    "  R     R   R ",
    "    R   R  R  ",
    "     RR   R   ",
    "      RR      ",
    "     bbbb     ",
    "    bbbbbb    ",
    "    bbbbbb    ",
    "   bbbbbbbb   ",
    "   bbbbbbbb   ",
    "  bbbbbbbbbb  ",
    "  bbbbbbbbbb  ",
    " bbbbbbbbbbbb ",
    " bbbbbbbbbbbb "
),
"Mountain": (
    "              ",
    "              ",
    "              ",
    "              ",
    "      bb      ",
    "     bbbb     ",
    "    bbbbbb    ",
    "    bbbbbb    ",
    "   bbbbbbbb   ",
    "   bbbbbbbb   ",
    "  bbbbbbbbbb  ",
    "  bbbbbbbbbb  ",
    " bbbbbbbbbbbb ",
    " bbbbbbbbbbbb "
),
"Ocean": (
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "  BBB    BBBB ",
    "BBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBB"
),
"Wave": (
    "              ",
    "              ",
    "    BBBBB     ",
    "   BBBBBBB    ",
    "  BBB   BBB   ",
    " BBB     BBB  ",
    "BBB       BBB ",
    "BB        BBB ",
    "BBB      BBB  ",
    "BBBB   BBB    ",
    "BBBBB         ",
    "BBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBB"
),
"Earthquake": (
    "bb  bbbbb     ",
    "bbb   bbbbb   ",
    "bbbbb  bbbbb  ",
    "  bbbbb  bbbb ",
    "   bbbbb  bbb ",
    "  bbbbb  b bb ",
    " bbbbb  bbbb  ",
    "bbb b  bbbbbb ",
    "bbbb  b b bbb ",
    " bbbb bb bbbb ",
    " bbbb b bbbbb ",
    " bbbb  bbbbb  ",
    " bbbb bbbbb   ",
    "  bbbb bbbbb  "
),
"Tsunami": (
    "              ",
    "BB       BBBB ",
    " BB     BB  BB",
    "       BB    B",
    "  BBBBBBBBB BB",
    " BBB    BBB   ",
    "BBB      BBB  ",
    "BB       BBB  ",
    "BBB     BBB BB",
    "BBBB  BBB  BB ",
    "BBBBB     BB  ",
    "BBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBB"
),
"Landslide": (
    "              ",
    "              ",
    "              ",
    "GG  bbb       ",
    "bGG bbbb      ",
    "bbG  bbb      ",
    "bbb  bbbb     ",
    "bbb  b b b    ",
    "bbb  bb   b   ",
    "bbb   b b     ",
    "bbb   b   b   ",
    "bbb   b b     ",
    "bbb b    b    ",
    "bbb   b   b   "
),
"Egg": (
    "              ",
    "              ",
    "      WW      ",
    "     WWWW     ",
    "    WWWWWW    ",
    "    WWWWWW    ",
    "   WWWWWWWW   ",
    "   WWWWWWWW   ",
    "   WWWWWWWW   ",
    "   WWWWWWWW   ",
    "   WWWWWWWW   ",
    "    WWWWWW    ",
    "     WWWW     ",
    "              "
),
"AI": (
    "              ",
    "              ",
    "              ",
    "              ",
    "   llllllll   ",
    "  llllllllll  ",
    "  llllllllll  ",
    "  llllllllll  ",
    "  llllllllll  ",
    "   llllllll   ",
    "  llll        ",
    "  ll          ",
    "              ",
    "              "
),
"Android": (
    "    G    G    ",
    "     G  G     ",
    "    GGGGGG    ",
    "   GGWGGWGG   ",
    "   GGGGGGGG   ",
    "    WWWWWW    ",
    " GWGGGGGGGGWG ",
    " G GGGGGGGG G ",
    " G GGGGGGGG G ",
    "   GGGGGGGG   ",
    "    GG  GG    ",
    "    GG  GG    ",
    "    GG  GG    ",
    "    GG  GG    "
),
"Bird": (
    "              ",
    "              ",
    "              ",
    "        wwww  ",
    "       wwNwwYY",
    "   wwwwwwwww  ",
    "  wwwwwwwww   ",
    "wwwwwwwwww    ",
    "   wwwwww     ",
    "    Y  Y      ",
    "    YY YY     ",
    "              ",
    "              ",
    "              "
),
"Beast": (
    "              ",
    "              ",
    "              ",
    "        gg  gg",
    "         gggg ",
    "        gNggNg",
    " ggggggggggggg",
    "ggggggggggggg ",
    "gggggggggggg  ",
    "  ggggggggg   ",
    "   w     w    ",
    "   ww    ww   ",
    "              ",
    "              "
),
"Fish": (
    "              ",
    "              ",
    "              ",
    " B     BBBB   ",
    " BB   BBBBBB  ",
    " BBB BBBBBWWB ",
    " BBBBBBBBBWNBB",
    " BBBBBBBBBBBBB",
    " BBB BBBBBBBB ",
    " BB   BBBBBB  ",
    " B     BBBB   ",
    "              ",
    "              ",
    "              "
),
"Phoenix": (
    "              ",
    "   OO    OOO  ",
    " R  OO  OO    ",
    " RR OORRRRR   ",
    "  RRORRRNRRYY ",
    "   RRRRRRRRR  ",
    "   RRRRRRRR   ",
    "RRRRRRRRRR    ",
    "   RRRRRR     ",
    "    Y  Y      ",
    "    YY YY     ",
    "              ",
    "              ",
    "              "
),
"Seeds": (
    "              ",
    "              ",
    "      RRR     ",
    "WW    RR      ",
    "WW        OO  ",
    "W        OOO  ",
    "   YY         ",
    "   YYY    b   ",
    "          bb  ",
    "    rr    bb  ",
    "    rrr       ",
    "         qq   ",
    "         qqq  ",
    "              "
),
"Beach": (
    "       YYYYYYY",
    "    YYYYYYYYBB",
    "   YYYYYYBBBBB",
    " YYYYYYYBBBBBB",
    "YYYYYBBBBBBBBB",
    "YYYYBBBBBBBBBB",
    "YYYBBBBBBBBBBB",
    "YYYBBBBBBBBBBB",
    "YYYYBBBBBBBBBB",
    "YYYYYYYBBBBBBB",
    " YYYYYYYBBBBBB",
    "  YYYYYYYBBBBB",
    "   YYYYYYYYBBB",
    "    YYYYYYYYYY"
),
"Hurricane": (
    "  BB BBBBB    ",
    " BB BB  BBB  B",
    " B BB     BB  ",
    " B  BB  B  BB ",
    " BB  BBBB  BB ",
    " BBB       BB ",
    "  BBBBB   BBB ",
    "    BBBB  BBB ",
    " B    BB BBB  ",
    "      BBBBB   ",
    "   B  BBBB    ",
    "     BBBB     ",
    "     BBB      ",
    "   BBBB    B  "
),
"Island": (
    "              ",
    "     GG   GG  ",
    "    G  G G  G ",
    "      GGGGG   ",
    "     G  b  G  ",
    " BBBBBBBbBBBBB",
    "BBYYYYYYbYYYYB",
    "BYYdddddbdYYYY",
    "BYYdddddddddYY",
    "BBYYddddddddYB",
    "BBYYYYYdddYYYB",
    " BBBBYYYYYYYBB",
    "  BBBBBBBBBBB ",
    "              "
),
"Wood": (
    "              ",
    "    bbbbbb    ",
    "   boooooob   ",
    "  boobbbboob  ",
    " boobooooboob ",
    " bboobbbboobb ",
    " boboooooobob ",
    " boobbbbbboob ",
    " boooooooooob ",
    " boooooooooob ",
    " boooooooooob ",
    "  boooooooob  ",
    "   boooooob   ",
    "    bbbbbb     "
),
"Duststorm": (
    "     wwbwww   ",
    "    ww    ww  ",
    "   ww      ww ",
    " w  ww  ww  bw",
    " wb  wwww  w w",
    " w w      www ",
    "  wwwwww  www ",
    "   ww wwww w  ",
    " w   www ww   ",
    "      wwww  w ",
    "   b  wwww    ",
    "     wwww     ",
    "     wwb     ",
    "    wwwww  w  "
),
"Cactus": (
    "      dd      ",
    "     dddd     ",
    "     dddd     ",
    "     dddd  dd ",
    "     dddd  dd ",
    "  ddddddddddd ",
    " ddddddddddd  ",
    " dd  dddd     ",
    " dd  dddd     ",
    " dd  dddd     ",
    "     dddd     ",
    "     dddd     ",
    "  YYYYYYYYYY  ",
    "YYYYYYYYYYYYYY"
),
"Glassware": (
    "              ",
    "    wwwwww    ",
    "   w      w   ",
    "   ww    ww   ",
    "   wwwwwwww   ",
    "   wwwwwwww   ",
    "    wwwwww    ",
    "    wwwwww    ",
    "     wwww     ",
    "      ww      ",
    "      ww      ",
    "      ww      ",
    "    wwwwww    ",
    "   wwwwwwww   "
),
"Alcohol": (
    "              ",
    "              ",
    "      bb      ",
    "      dd      ",
    "      dd      ",
    "     dddd     ",
    "    dddddd    ",
    "    dddddd    ",
    "    wwwwww    ",
    "    wwwwww    ",
    "    dddddd    ",
    "    dddddd    ",
    "    dddddd    ",
    "    dddddd    "
),
"Ash": (
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "              ",
    "       N      ",
    "      NNN     ",
    "    NNNNNN    ",
    "  NNNNNNNNN   ",
    " NNNNNNNNNNN  ",
    "              "
),
"Angler": (
    "              ",
    "     wwww     ",
    "    wwwwww    ",
    "     qqqq     ",
    "      qq      ",
    "    WWWWWW    ",
    "   WWWWWW W   ",
    "   W WWWW  q  ",
    "   W WWWW BBB ",
    "   q NNNN  B  ",
    "     NNNN BBB ",
    "     N  N BBB ",
    "     N  N  B  ",
    "     q  q     "
),
"Miner": (
    "     YYYY     ",
    "    YYYYYY    ",
    "     bbbb     ",
    "      bb      ",
    "    OOOOOO    ",
    "   O OOOO O   ",
    "   O OOOO O   ",
    "   O OOOO O   ",
    "   b OOOO b   ",
    "w b  OOOO     ",
    "wb   O  O     ",
    " ww  O  O     ",
    "     b  b     ",
    "     b  b     "
),
"Gold": (
    "              ",
    "              ",
    "        AAA   ",
    "       AAAAA  ",
    "      AAAAAAA ",
    "     AAAAAAAA ",
    "    AAAAAAAA  ",
    "   AAAAAAAA   ",
    "  AAAAAAAA    ",
    "  AAAAAAA     ",
    "   AAAAA      ",
    "    AAA       ",
    "              ",
    "              "
),
"Pirate": (
    "     NNNN     ",
    "    NNWWNN    ",
    "   NNNNNNNN   ",
    "     QQQQ     ",
    "      QQ      ",
    "    NNWWNN    ",
    "  YN NWWN NY  ",
    "  YY NWWN YY  ",
    " w   BBBB   w ",
    "w    NNNN    w",
    "     NNNN     ",
    "     N  N     ",
    "     N  N     ",
    "     N  N     "
),
"Boat": (
    "      W       ",
    "      WRR     ",
    "      WRRR    ",
    "      WRRRR   ",
    "      WRR     ",
    "      WR      ",
    "      W       ",
    "bb    W     bb",
    "bbbb  W   bbbb",
    " bbbbbbbbbbbb ",
    "  bbbbbbbbbb  ",
    "   bbbbbbbb   ",
    "    bbbbbb    ",
),
"Coal": (
    "              ",
    "   nnnn       ",
    "  nnnnnn      ",
    " nnnnnnn  nnn ",
    "nnnnnnn  nnnnn",
    " nnnnn  nnnnnn",
    "            nn",
    "    nnnnnnn   ",
    "   nnnnnnnnn  ",
    "  nnnnnnnnnn  ",
    "  nnnnnnnnn   ",
    "    nnnnn     ",
    "              ",
    "              "
),
"Oil": (
        "       N      ",
    "       NN     ",
    "       NNN    ",
    "      NNNN    ",
    "     NNNNN    ",
    "    NNNNNN    ",
    "   NNNNNNNN   ",
    "   NNNNNNNN   ",
    "  NNNNNNNNNN  ",
    "  NNNNNNNNNN  ",
    "  NNNNNNNNNN  ",
    "   NNNNNNNN   ",
    "    NNNNNN    ",
    "              "
),
"Natural Gas": (
    "              ",
    "              ",
    "      OOO     ",
    "   OOOOOOOO   ",
    "      OOOOOO  ",
    "     OOOOO    ",
    " OOOOOOOO     ",
    "     OOOOOOO  ",
    "  OOOOOOOO    ",
    "    OOOOOOO   ",
    "   OOOOO      ",
    "  OOOOOOOOO   ",
    "              ",
    "              "
),
"House": (
    "         ww   ",
    "         w    ",
    "              ",
    "        RR    ",
    "        RR    ",
    "   RRRRRRRR   ",
    "  RRRRRRRRRR  ",
    "  RRRRRRRRRR  ",
    "   WWWWWWWW   ",
    "   WllWWllW   ",
    "   WllWWllW   ",
    "   WWWWWWWW   ",
    "   WWWbbWWW   ",
    "   WWWbbWWW   "
),
"Music": (
    "              ",
    "           BB ",
    "           B  ",
    "  RR       BB ",
    "  R   YY  BB  ",
    "  R   YY  BB  ",
    " RR           ",
    " RR  GGGG     ",
    "     G  G     ",
    "     G  G     ",
    "    GG GG     ",
    "    GG GG     ",
    "              ",
    "              "
),
"Vocaloid": (
    "    Tp  pT    ",
    "   TTpTTpTT   ",
    "  TTTTWWTTTT  ",
    "  TT WWWW TT  ",
    "  T   WW   T  ",
    " T  WwTTwW  T ",
    " T W wTTw W T ",
    "   N wwTw N   ",
    "   N wwww N   ",
    "   W NwwN W   ",
    "     NNNN     ",
    "     W  W     ",
    "     N  N     ",
    "     N  N     "
),
"Dragon": (
    "   NN   BBBBBB",
    "  NN  BBBBB   ",
    " NN  BBBB     ",
    " BBBBBBBBBBB  ",
    "BBBBBBBBBBBBB ",
    "BBBB       BBB",
    "      BBB   BB",
    "     BB  B  BB",
    "B   BBB    BBB",
    "BB BBB    BBB ",
    "BBBBB    BBBBB",
    "  BBB   BBB BB",
    "   BBBBBBB   B",
    "    BBBBB     "
),
"Hero": (
    "       GG     ",
    "     GGGGG    ",
    "    GGGG      ",
    "    hhhh      ",
    "    hhhh      ",
    "     hh       ",
    "   GGGGGG     ",
    "  G GGGG G    ",
    "  G GGGG GB   ",
    "  h GGGG hBWWW",
    "    GGGG  B   ",
    "    b  b      ",
    "    b  b      ",
    "    b  b      "
),
"Carbon Dioxide": (
    "              ",
    "      NNNN    ",
    "    NNNNNNN   ",
    " NNNNNNNNNNN  ",
    "   NNNNNNNN   ",
    "     NNNNN    ",
    " NNNNNNNNN    ",
    "   NNNNNNNNN  ",
    " NNNNNNNNNN   ",
    "   NNNNNNN    ",
    " NNNNNNN      ",
    "  NNNNNNNN    ",
    "      NNNNNN  ",
    "              "
),
"Cola": (
    "      RR      ",
    "      NN      ",
    "      NN      ",
    "     NNNN     ",
    "    NNNNNN    ",
    "    NNNNNN    ",
    "    RRRRRR    ",
    "    RWRWWR    ",
    "    RRWRWR    ",
    "    RRRRRR    ",
    "    NNNNNN    ",
    "    NNNNNN    ",
    "    NNNNNN    ",
    "    NNNNNN    "
),
}


def element_interior(window, x, y, element, mouse_rect):
    interior_rect = pygame.Rect(x, y, 75, 75)
    x += 8
    y += 8
    color_list = (
        ("Y", (200, 200, 50)),      # Y | yellow
        ("G", (50, 250, 50)),       # G | green
        ("g", (80, 80, 80)),        # g | gray
        ("l", (100, 100, 200)),     # l | light blue
        ("B", (50, 50, 250)),       # B | blue
        ("b", (150, 100, 30)),      # b | brown
        ("R", (250, 50, 50)),       # R | red
        ("r", (150, 30, 30)),       # r | dark red
        ("O", (250, 120, 50)),      # O | orange
        ("o", (250, 170, 100)),     # o | weaker orange
        ("W", (255, 255, 255)),     # W | white
        ("w", (110, 110, 110)),     # w | light gray
        ("P", (180, 50, 250)),      # P | purple
        ("N", (0, 0, 0)),           # N | black
        ("p", (180, 50, 250)),      # p | pink
        ("q", (250, 180, 200)),     # q | pale peach
        ("d", (30, 100, 30)),       # d | dark green
        ("Q", (200, 180, 100)),     # Q | yellowish-white
        ("h", (200, 160, 90)),      # h | brownish-white
        ("A", (255, 220, 0)),       # A | gold 
        ("n", (10, 10, 10)),        # n | light black  
        ("T", (100, 200, 255)),     # T | turquoise

    )
    icon = []                           # blank for if element is blank or not defined.
    if element != "Empty":
        if element in icon_dictionary:          # to stop crashes when an invalid icon is found
            icon = icon_dictionary[element] # getting element art

    # looping through the whole image. using different x/y since its used again later.
    x_ = x
    y_ = y
    for row in icon:
        for value in row:
            # picking color and drawing
            for color in color_list:
                if value == color[0]:
                    pygame.draw.rect(window, color[1], pygame.Rect(x_, y_, 4, 4))
            
            x_ += 4
        x_ = x
        y_ += 4

    if element != "Empty" and interior_rect.colliderect(mouse_rect):
        pygame.draw.rect(window, (40, 40, 40), pygame.Rect(745, 285, 395, 255))
        name_tag = pygame.Surface((385, 50))    # making a surface to get a transparent rect
        name_tag.fill((0, 0, 0))                # making surface black
        name_tag.set_alpha(100)                 # getting transparency
        window.blit(name_tag, (750, 290))
        window.blit(font.render(element, False, (255, 255, 255)), (755, 290))
        window.blit(font.render(str(gold_from(element)) + "g", False, (250, 250, 100)), (1080, 290))
        y = 340
        for line in description_of(element):
            window.blit(small_font.render(line, False, (180, 180, 180)), (755, y))
            y += 18
