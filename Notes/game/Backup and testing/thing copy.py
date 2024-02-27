import pygame
import random 

# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (100, 100, 255) 
WIDTH = 440
HEIGHT = 450

# Colors  
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
COLORS = (BLACK, WHITE)

# Stuff
xcords = (50, 100, 150, 200, 250, 300, 350)
ycords = (50, 100, 150)
contwin = 0
game_exit = True

#functions
def random_color(randomc):
    return random.choice(COLORS) if randomc else BLACK

def run_game(row_group):
    # Allows you to exit the game
    menu_exit = True 
    global game_exit
    while menu_exit:                
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT:
                menu_exit = False
                game_exit = False
        
        # Updates sprites and checks win condition
        did_win = False
        for i in list(row_group):
            if win(i.update(events)):
                did_win = True
        
        if (sprmenu.update(events)) == True: 
            menu_exit = False
                       
        # Draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        row_group.draw(screen)
        screen.blit(text_menu , (60, 210))

        # if won, informs the player
        if did_win:
            won.draw(screen)
            screen.blit(textwin , (150+10, 250+10))  
        
        # Updates screen
        pygame.display.update()

def change(sprite):
    #change color
    color = BLACK if sprite.image.get_at(
        (0, 0)) != BLACK else WHITE
    sprite.image.fill(color)

def win(group):
    # checks to see if you won
    # if all 21 sprites are white
    global contwin 
    if group == WHITE:
        if contwin < 21:
            contwin = contwin + 1
            print(contwin)
        if contwin == 21:
            return True
    else:
        contwin = 0

def self_neighbor(x, row, aval):
    # Changes the colors of its self and its neighbors
    change(row[aval]) # its self
    # Find neighbors on Y axis
    if row == row1 or row == row3: 
        change(row2[aval])
    if row == row2:
        change(row1[aval])
        change(row3[aval])
    # Find neighbors on X axis
    if x != 50:
        change(row[aval-1])
    if x != 350:
        change(row[aval+1])      
               
               
# Object class 
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, color):
        super().__init__()
        # Draws itself
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color)
        
    def update(self, events):
        # checks to see if it was clicked
        global mod_normal
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # finds self cords
                    x = self.rect.x
                    y = self.rect.y
                    # Find its X valve on the list xcords, Uses that to find its x neighbors
                    aval = xcords.index(x)
                    # Changes the colors of its self and its neighbors

                    if y == 50: # top row
                        self_neighbor(x, row1, aval)

                    if y == 100: # mid row   
                        self_neighbor(x, row2, aval)

                    if y == 150: # bottom row 
                        self_neighbor(x, row3, aval)
                    
                    if x == 50 and y == 250: # Random
                        game(True)
                        
                    if x == 50 and y == 300: # Normal
                        game(False)
                        
                    if x == 50 and y == 200: # Menu
                        return True 
                    
        # finds and reports it's current color
        color = self.image.get_at((0, 0))
        #print(color)
        return color


# init
pygame.init() 

# screen  
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Game Thing")

# defining a font  
smallfont = pygame.font.SysFont('Corbel',25) 

# text
text_random = smallfont.render('Random' , True , WHITE)
text_norm = smallfont.render('Normal' , True , WHITE)
textwin = smallfont.render('You Won!' , True , WHITE)
text_menu = smallfont.render('Menu' , True , WHITE)
text_howtoplay = smallfont.render('How To Play!' , True , WHITE)
text_howto = smallfont.render('Click on the tiles untill they are all white.' , True , WHITE)

# sprites stuff
# sprites for game options
sprrandom = ClickableSprite(pygame.Surface((100, 40)), 50, 250, BLACK) # random
sprnorm = ClickableSprite(pygame.Surface((100, 40)), 50, 300, BLACK) # normal
sprmenu = ClickableSprite(pygame.Surface((90, 40)), 50, 200, BLACK) # menu
sprites_list = pygame.sprite.Group(sprrandom, sprnorm)

# sprites for, if won
winsprite = ClickableSprite(pygame.Surface((140, 40)), 150, 250, BLACK)
won = pygame.sprite.Group(winsprite)

# Game sprites
def sprrows(row, true_or_false):
    sprsize = (40, 40)
    sprites = [ClickableSprite(pygame.Surface(sprsize), xcords[num], ycords[row], (random_color(true_or_false))) for num in range(7)]
    return sprites

# game something
def game(true_or_false):
    global row1,row2,row3
    row1,row2,row3 = [(sprrows(ro, true_or_false)) for ro in range(3)]
    
    run_game(pygame.sprite.Group(row1, row2, row3, sprmenu))

def main():
    global rows
    global game_exit
    exit = True
    while exit: 
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: 
                exit = False
 
        # Updates and draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        sprites_list.draw(screen)
        sprites_list.update(events)
        
        # Adds text to the screen       
        screen.blit(text_random , (WIDTH/7,HEIGHT/2+35)) 
        screen.blit(text_norm , (WIDTH/7,HEIGHT/2+85))
        screen.blit(text_howtoplay , (170,30))
        screen.blit(text_howto , (50,60))

        pygame.display.update()
        
main()
pygame.quit() 