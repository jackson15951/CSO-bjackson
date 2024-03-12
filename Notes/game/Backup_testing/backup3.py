import time
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
game_mode = False
oprandom = False
optimed = 0

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
    global xcords, ycords, menu_exit, exit, clicks, end, start, game_mode
    win_check = 0
    clicks = 0
    end = 0
    start = time.time()
    end = time.time()
    if len(xcords) > 6: screen = pygame.display.set_mode((xcords[-1]+90, ycords[-1]+180))
    else: screen = pygame.display.set_mode((440, ycords[-1]+180))
    menu_exit = True 
    while menu_exit: # Allows you to exit the game               
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT:
                menu_exit = False
                exit = False

        # Updates sprites and checks win condition
        did_win = False
        for i in list(row_group):
            if win(i.update(events)): win_check = win_check + 1
            if win_check > 2: did_win = True
        
        if (sprmenu.update(events)) == True:
            menu_exit = False 
            screen = pygame.display.set_mode((440, 500))
            expand_cords(xsize,ysize)
        
        # text stuff
        text_clicks = smallfont.render('Clicks: %s' %clicks, True , WHITE) # Clicks
        text_time = smallfont.render('Time: %ss' %int(end - start), True , BLACK) # Timer
                       
        # Draws sprites, screen, and text
        screen.fill(SURFACE_COLOR) 
        row_group.draw(screen)
        screen.blit(text_menu , (70, ycords[-1]+60)) # Menu
        screen.blit(text_reset , (172, ycords[-1]+60)) # Reset
        screen.blit(text_size , (272, ycords[-1]+60)) # Size
        screen.blit(text_clicks , (60, ycords[-1]+110)) # Clicks
        screen.blit(text_time , (50, 20)) # Timer
        
        # if won or losed, informs the player, else updates timer
        if mode == 2: game_mode = clicks > 7
        if mode == 1: game_mode = int(end - start) == 10

        if game_mode:
            win_lose_sprite.draw(screen)
            screen.blit(text_lose , (160, ycords[-1]+110))
        
        elif did_win:
            win_lose_sprite.draw(screen)
            screen.blit(text_win , (160, ycords[-1]+110))
            pygame.display.update()
            time.sleep(2)
            menu_exit = False
            game(norm_rand, mode)
            
        else: end = time.time() 
        
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
        if contwin < (len(xcords)*len(ycords)): contwin = contwin + 1
        if contwin == (len(xcords)*len(ycords)): return True
    else: contwin = 0

def self_neighbor(x,y): # Changes the colors of its self and its neighbors
    global rows, clicks
    clicks = clicks + 1
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
        # checks to see if self was clicked
        global menu_exit, oprandom, optimed
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # finds self cords
                    x = self.rect.x
                    y = self.rect.y
                    
                    if x in xcords: self_neighbor(x,y) # Game buttons
                    if x == 269 and y == 350: game(oprandom, 2) # Max clicks
                    if x == 49 and y == 250: game(oprandom, optimed) # Normal
                    if x == 159 and y == 250: expand_cords(2,2), game(oprandom, optimed) # Easy 
                    if x == 269 and y == 250: expand_cords(9,6), game(oprandom, optimed) # Hard
                    if x == 51 and y == ycords[-1]+50: return True # Menu
                    
                    if x == 151 and y == ycords[-1]+50: # Reset
                        menu_exit = False
                        game(norm_rand, mode)
                        
                    if x == 251 and y == ycords[-1]+50: # Size
                        menu_exit = False
                        expand_cords(xsize+6,ysize+6) if len(xcords) == xsize else expand_cords(xsize,ysize)
                        game(norm_rand, mode)

                    if x == 159 and y == 350: # Random
                        oprandom = True if oprandom != True else False 
                        change(sprnorm) 
                        
                    if x == 49 and y == 350: # Timed
                        optimed = 1 if optimed == 0 else 0
                        change(sprtimed)
                    
        # finds and reports it's current color
        color = self.image.get_at((0, 0))
        return color

# init
pygame.init() 

# screen  
screen = pygame.display.set_mode((440, 500)) 
pygame.display.set_caption("Game Thing")

path = pathlib.Path(__file__).parent.resolve()
win_img = pygame.image.load('%s/how_to.png' %path)
win_img = pygame.transform.scale(win_img, (360,150))

# defining a font  
smallfont = pygame.font.SysFont('Corbel',25) 

# text
text_random = smallfont.render('Random' , True , WHITE)
text_size = smallfont.render('Size' , True , WHITE)
text_norm = smallfont.render('Normal' , True , WHITE)
text_easy = smallfont.render('Easy' , True , WHITE)
text_hard = smallfont.render('Hard' , True , WHITE)
text_timed = smallfont.render('Timed' , True , WHITE)
text_maxclicks = smallfont.render('Max Clicks' , True , WHITE)
text_menu = smallfont.render('Menu' , True , WHITE)
text_reset = smallfont.render('Reset' , True , WHITE)
text_win = smallfont.render('You Won!' , True , WHITE)
text_lose = smallfont.render('You Lose!' , True , WHITE)
text_howtoplay = smallfont.render('How To Play!' , True , WHITE)
text_howto = smallfont.render('Click on the tiles untill they are all white.' , True , WHITE)

# Sprites Main Menu
sprrandom = ClickableSprite(pygame.Surface((100, 40)), 49, 250, BLACK) # normal
spreasy = ClickableSprite(pygame.Surface((100, 40)), 159, 250, BLACK) # easy
sprhard = ClickableSprite(pygame.Surface((100, 40)), 269, 250, BLACK) # hard
sprtimed = ClickableSprite(pygame.Surface((100, 40)), 49, 350, BLACK) # timed
sprnorm = ClickableSprite(pygame.Surface((100, 40)), 159, 350, BLACK) # random
sprmaxclicks = ClickableSprite(pygame.Surface((100, 40)), 269, 350, BLACK) # max clicks
sprites_list = pygame.sprite.Group(sprrandom, sprnorm, sprtimed, sprmaxclicks, spreasy, sprhard)

# Game something
def game(random_tf, game_modes):
    global norm_rand, sprmenu, sprreset, win_lose_sprite, rows, sprexpand, mode 
    norm_rand = random_tf # <--this is part of Reset
    mode = game_modes
    
    sprmenu = ClickableSprite(pygame.Surface((88, 40)), 51, ycords[-1]+50, BLACK) # menu
    sprclicks = ClickableSprite(pygame.Surface((108, 40)), 51, ycords[-1]+100, BLACK) # clicks
    sprreset = ClickableSprite(pygame.Surface((88, 40)), 151, ycords[-1]+50, BLACK) # reset
    sprexpand = ClickableSprite(pygame.Surface((88, 40)), 251, ycords[-1]+50, BLACK) # expand
    win_lose_sprite = pygame.sprite.Group(ClickableSprite(pygame.Surface((140, 40)), 150, ycords[-1]+100, BLACK)) # You Win! / You Lose!

    rows = [([ClickableSprite(pygame.Surface((40, 40)), xcords[num], ycords[row], (random_color(random_tf))) for num in range(len(xcords))]) for row in range(len(ycords))]
    run_game(pygame.sprite.Group(rows, sprmenu, sprreset, sprexpand, sprclicks))

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
        screen.blit(text_norm , (67,260)) 
        screen.blit(text_random , (173,360))
        screen.blit(text_timed , (73,360))
        screen.blit(text_maxclicks , (275,360))
        screen.blit(text_howtoplay , (170,30))
        screen.blit(text_howto , (50,60))
        screen.blit(text_easy , (188,260)) 
        screen.blit(text_hard , (298,260)) 
        
        if exit == False: screen.fill(SURFACE_COLOR)

        pygame.display.update() 
        
main()
pygame.quit()


