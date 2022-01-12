import pygame
import sys
from pygame.locals import *
import draw
from draw import gold_from, pick_for_shop, first_empty_slot_in
from reactions import check_for_synergy

# TODO
# more combinations
#   balancing of current ones:
#       e.g.
#       Living being strats
#       Robot strats
#       Fire strats
#       Ocean strats
#       Sandstorm strats
#       Snow strats
#       Gold strats
#       Focus especially more so on instant money from merges.
#   after balancing, change score brackets.
#
# possible new starting symbols: void, light
# potentially add food combinations
#   humans eat food
#   food buffs other food
#   beast + human --> cow + human
#   cow + water/plants --> milk
#   milk + ice/snow --> ice cream
#   milk + fire --> cheese
#   egg + cheese --> omelette

# DEBUG // FPS checking
# tick = pygame.time.Clock()
#         tick.tick()
#         print(int(tick.get_fps()))

# Game set up
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
window_width = 1200
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Elemental Deck Builder')
icon = pygame.Surface((20, 20))
pygame.display.set_icon(icon)

# initializing font for later use
pygame.font.init()
big_font = pygame.font.SysFont('arial', 70)
font = pygame.font.SysFont('arial', 40)
medium_font = pygame.font.SysFont('arial', 30)
small_font = pygame.font.SysFont('arial', 20)
tiny_font = pygame.font.SysFont('arial', 12)

def menu():

    # main menu screen

    rect = pygame.Rect(800, 400, 185, 50)
    back_rect = pygame.Rect(795, 395, 195, 60)

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
        mouse_x, mouse_y = pygame.mouse.get_pos()               # getting mouse pos for collision checks later
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)

        window.fill((0, 0, 0))
        back_color = (30, 30, 30)             # setting background color for both buttons

        if mouse_rect.colliderect(rect):                        # if button collides, changes back color
            back_color = (200, 200, 50)
            if pygame.mouse.get_pressed()[0]:                   # ends screen if new is clicked
                break

        # drawing the back of the buttons
        pygame.draw.rect(window, back_color, back_rect)
        pygame.draw.rect(window, (50, 50, 50), rect)

        # drawing the text on buttons
        window.blit(font.render(" New Game", True, (255, 255, 255)), rect)

        # game title
        massive_font = pygame.font.SysFont('arial', 150)
        window.blit(massive_font.render("Elements for Money", True, (200, 200, 255)), pygame.Rect(50, 50, 195, 60))
        # element banner
        x = 150
        while x < 800:
            draw.element_interior(window, x, 200, "Air", (0, 0, 0, 0))
            draw.element_interior(window, x+59, 200, "Earth", (0, 0, 0, 0))
            draw.element_interior(window, x+110, 200, "Fire", (0, 0, 0, 0))
            draw.element_interior(window, x+160, 202, "Water", (0, 0, 0, 0))
            x += 205

        pygame.display.flip()


    # how to play screen

    rect = pygame.Rect(830, 470, 95, 50)
    back_rect = pygame.Rect(825, 465, 105, 60)

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
        mouse_x, mouse_y = pygame.mouse.get_pos()               # getting mouse pos for collision checks later
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)

        window.fill((0, 0, 0))
        back_color = (30, 30, 30)             # setting background color for both buttons

        if mouse_rect.colliderect(rect):                        # if button collides, changes back color
            back_color = (200, 200, 50)
            if pygame.mouse.get_pressed()[0]:                   # ends screen if new is clicked
                break

        # drawing the back of the buttons
        pygame.draw.rect(window, back_color, back_rect)
        pygame.draw.rect(window, (50, 50, 50), rect)

        # drawing the text on buttons
        window.blit(font.render(" Start", True, (255, 255, 255)), rect)

        # drawing the instructions
        text = "Place elements next to each other to set up a reaction."
        window.blit(font.render(text, True, (255, 255, 255)), pygame.Rect(50, 50, 50, 50))
        text = "You may pick a new element from the shop each cycle."
        window.blit(font.render(text, True, (255, 255, 255)), pygame.Rect(50, 150, 50, 50))
        text = "Advance to the next cycle to do all reactions and gain gold."
        window.blit(font.render(text, True, (255, 255, 255)), pygame.Rect(50, 250, 50, 50))
        text = "Get enough gold to pay off each payment."
        window.blit(font.render(text, True, (255, 255, 255)), pygame.Rect(50, 350, 50, 50))

        pygame.display.flip()
    
    # starts the game after menus are done
    main()


def lose_screen(gold, payment):
    rect = pygame.Rect(420, 410, 320, 50)
    back_rect = pygame.Rect(415, 405, 330, 60)

    # getting game info
    payment_lost_at = int((payment/100)-1)
    total_gold_earnt = 50*(payment_lost_at**2 + payment_lost_at) + gold     # quadratic equation

    # getting rank
    rank = "SSS"                    # assumes highest rank until proven otherwise
    rank_color = (255, 255, 0)
    score_list = (
        (0, 250, "F", (255, 0, 0)),
        (251, 1000, "D", (200, 50, 50)),
        (1001, 3000, "C", (200, 100, 0)),
        (3001, 10000, "B", (100, 100, 0)),
        (10001, 50000, "A", (0, 240, 0)),
        (50001, 100000, "S", (240, 180, 0)),
        (100001, 200000, "SS", (240, 220, 0)),
    )
    for score in score_list:
        if score[0] <= total_gold_earnt <= score[1]:
            rank = score[2]
            rank_color = score[3]

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
        mouse_x, mouse_y = pygame.mouse.get_pos()                   # getting mouse pos for collision checks later
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)

        window.fill((0, 0, 0))
        back_color = (30, 30, 30)             # setting background color for both buttons

        if mouse_rect.colliderect(rect):                        # if button collides, changes back color
            back_color = (200, 200, 50)
            if pygame.mouse.get_pressed()[0]:                       # ends screen if new is clicked
                break

        # drawing the back of the buttons and the text
        pygame.draw.rect(window, back_color, back_rect)
        pygame.draw.rect(window, (50, 50, 50), rect)
        window.blit(font.render(" Return to Main Menu", True, (255, 255, 255)), rect)

        # blitting text
        window.blit(big_font.render("You missed payment.", True, (200, 200, 255)), pygame.Rect(50, 50, 195, 60))
        window.blit(font.render(f"You lost at payment {payment_lost_at}.", True, 
                                (200, 200, 255)), pygame.Rect(70, 150, 195, 60))
        window.blit(font.render(f"You missed payment by {(abs(gold))}g.", True, 
                                (200, 200, 255)), pygame.Rect(70, 200, 195, 60))
        window.blit(font.render(f"You earnt a total of {abs(total_gold_earnt)}g.", True, 
                                (200, 200, 255)), pygame.Rect(70, 250, 195, 60))
        window.blit(font.render(f"{rank} Rank", True, rank_color), pygame.Rect(70, 300, 195, 60))

        pygame.display.flip()

    # resetting variables when "exit to main menu" is pressed
    draw.gold_particle_list = []

    menu()


def main():
    # basic definitions
    pick = []
    deck = [
    ["Air", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],
    ["Empty", "Empty", "Earth", "Empty", "Empty", "Empty","Empty"],
    ["Empty", "Empty", "Empty", "Empty", "Fire", "Empty", "Empty"],
    ["Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Water"]
    ]

    purchase_selection = ["Air", "Earth", "Fire", "Water"]

    gold = 100
    payment = 100
    
    turns_to_next_cycle = 10
    luck = 4
    bought_from_store = False
    previous_click_status = False
    previous_reactions = []

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        window.fill((5, 5, 5))

        draw.ui(window, gold)

        # previous reactions list. has to be done right after UI.
        while len(previous_reactions) > 14:
            del previous_reactions[0]
        draw.previous_reactions(window, previous_reactions)

        mouse_x, mouse_y = pygame.mouse.get_pos()   # getting mouse pos for collision checks later
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)
        valid_click = False                         # click status for collision checks later
        if pygame.mouse.get_pressed()[0] and not previous_click_status:
            valid_click = True

        elements_not_clicked = 32                   # used later to cancel selection if nothing is clicked.

        # drawing & selection loop
        x = 75
        y = 184
        for row in deck:
            for element in row:
                
                element_rect = pygame.Rect(x, y, 75, 75)    

                # selecting elements
                
                if mouse_rect.colliderect(element_rect) and valid_click:
                    valid_click = False         # stops one click registering as multiple
                    elements_not_clicked -= 1   # registers it as a clicked element

                    # grid x (used for deck later) from iteration x (used for drawing)
                    grid_x = int((x-75)/90)
                    grid_y = int((y-184)/89)

                    # selection allows to move things around
                    # pick is the selected object. selected_element was way too long, used pick instead.
                    if pick == []:                  # if nothing selected, selects.
                        pick = [grid_x, grid_y]
                    elif pick == [grid_x, grid_y]:  # if select 1 = select 2, cancels.
                        pick = []
                    else:
                        # swaps.
                        deck[pick[1]][pick[0]], deck[grid_y][grid_x] = deck[grid_y][grid_x], deck[pick[1]][pick[0]]
                        pick = []
                    
                draw.element_background(window, x, y, mouse_rect, pick)
                draw.element_interior(window, x, y, element, mouse_rect)
                x += 90
            y += 89
            x = 75

        x = 765
        y = 184
        for element in purchase_selection:
            element_rect = pygame.Rect(x, y, 75, 75)  
            if not bought_from_store:
                draw.shop_background(window, x, y, mouse_rect)
                draw.element_interior(window, x, y, element, mouse_rect)
            else:
                draw.shop_curtains(window)

            if mouse_rect.colliderect(element_rect) and valid_click:
                valid_click = False         # stops one click registering as multiple
                # grid x (used for deck later) from iteration x (used for drawing)
                grid_x = int((x-845)/150)

                if not bought_from_store:
                    if pick == []:              # if nothing selected, places into first slot.

                        if first_empty_slot_in(deck) != None:
                            y_location, x_location = first_empty_slot_in(deck)
                            deck[y_location][x_location] = element
                            # after replacing element, resets shop
                            bought_from_store = True
                            purchase_selection = pick_for_shop(luck)

                    elif deck[pick[1]][pick[0]] == "Empty": # buys in selected slot
                        deck[pick[1]][pick[0]] = purchase_selection[grid_x]
                        pick = []
                        # after replacing element, resets shop
                        bought_from_store = True
                        purchase_selection = pick_for_shop(luck)
                    
                    else:           # if selected slot is an element (only remaining circumstance),
                        pick = []   # cancels
            x += 93

        # if no elements were clicked during a click, cancels the selection.
        if valid_click and (elements_not_clicked == 32):
            pick = []
        
        # next cycle things
        touching_next_cycle_button = mouse_rect.colliderect(pygame.Rect(480, 555, 135, 40))
        draw.next_cycle(window, touching_next_cycle_button, turns_to_next_cycle, payment)
        if touching_next_cycle_button and valid_click:
            turns_to_next_cycle -= 1
            bought_from_store = False
            
            dx = 0
            dy = 0
            change_list = []
            previous_reactions = []

            # cycles through each element for reactions
            for row in deck:
                for element in row:
                    # gold earnt is tracked throughout, given all at once in the end.
                    gold_earnt = gold_from(element)

                    # seeing adjacency and comparing with the synergy list.
                    if element != "Empty":
                        adjacenct_list = ((dx, dy+1), (dx, dy-1), (dx+1, dy+1), (dx+1, dy-1), (dx+1, dy),
                                    (dx-1, dy+1), (dx-1, dy-1), (dx-1, dy))
                        for adjacency in adjacenct_list:
                            # only does it for valid adjacencies (i.e. not off the map, not empty)
                            if 0 <= adjacency[1] <= 3 and 0 <= adjacency[0] <= 6:
                                elements_to_check = (deck[dy][dx], deck[adjacency[1]][adjacency[0]])
                                if elements_to_check[1] != "Empty":

                                    # gets information from check_for_synergy function
                                    synergy_present, synergy = check_for_synergy(elements_to_check)
                                    
                                    if synergy_present:  # if there is a synergy, proceeds to next step.

                                        # splits synergy into easier-to-understand pieces
                                        reactants, products, gold_from_reaction = synergy
                                        
                                        # assumes synergy is valid. invalidates if the first element has already been consumed.
                                        valid = True
                                        for change in change_list:
                                            if change[0] == dy and change[1] == dx:     # seeing if the element is in the list
                                                if deck[dy][dx] != change[2]:           # seeing if it was used (i.e. changed)
                                                    valid = False                       # if consumed, cannot do another synergy.

                                        if valid:   # only valid changes are done.
                                            gold_earnt += gold_from_reaction
                                            if reactants[0] != products[0]:             # only adds the change if it changes something.
                                                change_list.append((dy, dx, products[0]))

                                            # seeing how the adjacent should react.
                                            if reactants[1] != products[1]:
                                                change = True
                                                for change_2 in change_list:
                                                    # if it was already consumed before, won't react.
                                                    # you can still double-use it if it always is the adjacent, never if it is the main.
                                                    if change_2[0] == adjacency[1] and change_2[1] == adjacency[0]:
                                                        change = False
                                                        break
                                                if change:
                                                    change_list.append((adjacency[1], adjacency[0], products[1]))
                                            previous_reactions.append(synergy)
                    
                    # giving gold
                    gold += gold_earnt
                    draw.add_gold(str(gold_earnt), ((90*dx)+98), ((dy*89)+184))

                    dx += 1
                dy += 1
                dx = 0
            
            for change in change_list:                  # does all changes at once at the end.
                deck[change[0]][change[1]] = change[2]
        
        # playing the animation for the coins and doing payment things.
        draw.gold_animation(window)
        if turns_to_next_cycle == 0:
            gold -= payment
            turns_to_next_cycle = 8
            payment += 100   
            luck += 0.5
            if gold < 0:
                break

        # changing click status based on current frame to be used next frame.
        if pygame.mouse.get_pressed()[0]:
            previous_click_status = True
        else: 
            previous_click_status = False
        
        
        fpsClock.tick(FPS)
        pygame.display.update()
    
    lose_screen(gold, payment)


if __name__ == "__main__":
    menu()
