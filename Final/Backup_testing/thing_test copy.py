import pygame
import random 
import pathlib

# VARIABLES
SURFACE_COLOR = (100, 100, 255)  
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
contwin = 0
xsize = 7
ysize = 3

# Functions
def expand_cords(cols,row): # Expand the board
    global xcords, ycords
    xcords = [] #[50, 100, 150, 200, 250, 300, 350]
    ycords = [] #[50, 100, 150]
    x = 0
    y = 0
    for i in range(cols):
        x = x + 50
        xcords.append(x)
    for i in range(row):
        y = y + 50
        ycords.append(y)

def run_game(row_group):
    # Allows you to exit the game
    global xcords, ycords, menu_exit, exit
    screen = pygame.display.set_mode((xcords[-1]+90, ycords[-1]+180))
    menu_exit = True 
    while menu_exit:                
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT:
                menu_exit = False
                exit = False
        
        # Updates sprites and checks win condition
        did_win = False
        for i in list(row_group):
            if win(i.update(events)): did_win = True
        
        if (sprmenu.update(events)) == True:
            menu_exit = False 
            screen = pygame.display.set_mode((440, 450))
            expand_cords(xsize,ysize)
                       
        # Draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        row_group.draw(screen)
        screen.blit(text_menu , (70, ycords[-1]+60))
        screen.blit(text_reset , (172, ycords[-1]+60)) 
        screen.blit(text_size , (272, ycords[-1]+60))

        # if won, informs the player
        if did_win:
            win_sprite.draw(screen)
            screen.blit(text_win , (160, ycords[-1]+110)) 
        
        # Updates screen
        pygame.display.update()

def change(sprite):
    #change color
    color = BLACK if sprite.image.get_at((0, 0)) != BLACK else WHITE
    sprite.image.fill(color)

def win(group):
    # if all sprites are white you won
    global contwin 
    if group == WHITE:
        if contwin < (xsize*ysize): contwin = contwin + 1
        if contwin == (xsize*ysize): return True
    else: contwin = 0

def self_neighbor(x,y): # Changes the colors of its self and its neighbors
    global rows
    aval = xcords.index(x)
    bval = ycords.index(y)
    change(rows[bval][aval]) # its self
    # Find neighbors on Y axis
    if y != 50: change(rows[bval-1][aval])
    if y != ycords[-1]: change(rows[bval+1][aval])
    # Find neighbors on X axis
    if x != 50: change(rows[bval][aval-1])
    if x != xcords[-1]: change(rows[bval][aval+1])
        
def random_color(randomc): return random.choice((BLACK, WHITE)) if randomc else BLACK
               
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
        global menu_exit
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # finds self cords
                    x = self.rect.x
                    y = self.rect.y
                    
                    if x in xcords: self_neighbor(x,y) # Game buttons
                    if x == 49 and y == 250: game(True) # Random 
                    if x == 49 and y == 300: game(False) # Normal
                    if x == 51 and y == ycords[-1]+50: return True # Menu
                    if x == 151 and y == ycords[-1]+50: # Reset
                        menu_exit = False
                        game(norm_rand)
                    if x == 251 and y == ycords[-1]+50: # Expand
                        menu_exit = False
                        if len(xcords) == xsize: expand_cords(xsize+6,ysize+6)
                        else: expand_cords(xsize,ysize)
                        game(norm_rand)
                    
        # finds and reports it's current color
        color = self.image.get_at((0, 0))
        print(color)
        return color

# init
pygame.init() 

# screen  
screen = pygame.display.set_mode((440, 450)) 
pygame.display.set_caption("Game Thing")

path = pathlib.Path(__file__).parent.resolve()
win_img = pygame.image.load('%s/win_img.png' %path)
win_img = pygame.transform.scale(win_img, (360,150))

# defining a font  
smallfont = pygame.font.SysFont('Corbel',25) 

# text
text_random = smallfont.render('Random' , True , WHITE)
text_size = smallfont.render('Size' , True , WHITE)
text_norm = smallfont.render('Normal' , True , WHITE)
text_menu = smallfont.render('Menu' , True , WHITE)
text_reset = smallfont.render('Reset' , True , WHITE)
text_win = smallfont.render('You Won!' , True , WHITE)
text_howtoplay = smallfont.render('How To Play!' , True , WHITE)
text_howto = smallfont.render('Click on the tiles untill they are all white.' , True , WHITE)

# sprites stuff
sprrandom = ClickableSprite(pygame.Surface((100, 40)), 49, 250, BLACK) # random
sprnorm = ClickableSprite(pygame.Surface((100, 40)), 49, 300, BLACK) # normal
sprites_list = pygame.sprite.Group(sprrandom, sprnorm)

# game something
def game(true_or_false):
    global norm_rand, sprmenu, sprreset, win_sprite, rows, sprexpand  
    norm_rand = true_or_false # <--this is part of Reset
    
    sprmenu = ClickableSprite(pygame.Surface((88, 40)), 51, ycords[-1]+50, BLACK) # menu
    sprreset = ClickableSprite(pygame.Surface((88, 40)), 151, ycords[-1]+50, BLACK) # reset
    sprexpand = ClickableSprite(pygame.Surface((88, 40)), 251, ycords[-1]+50, BLACK) # expand
    win_sprite = pygame.sprite.Group(ClickableSprite(pygame.Surface((140, 40)), 150, ycords[-1]+100, BLACK)) # You Win!

    rows = [([ClickableSprite(pygame.Surface((40, 40)), xcords[num], ycords[row], (random_color(true_or_false))) for num in range(len(xcords))]) for row in range(len(ycords))]
    run_game(pygame.sprite.Group(rows, sprmenu, sprreset, sprexpand))

def main():
    expand_cords(xsize,ysize) # Expand the board
    global exit
    exit = True
    while exit: 
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: exit = False

        # Updates and draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        sprites_list.draw(screen)
        sprites_list.update(events)
        
        # Adds text to the screen    
        screen.blit(win_img, (39,80))  
        screen.blit(text_random , (63,260)) 
        screen.blit(text_norm , (63,310))
        screen.blit(text_howtoplay , (170,30))
        screen.blit(text_howto , (50,60))
        
        if exit == False: screen.fill(SURFACE_COLOR)

        pygame.display.update() 
        
main()
pygame.quit()


