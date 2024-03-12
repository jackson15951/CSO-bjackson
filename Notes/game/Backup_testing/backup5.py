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
click_loss, timed_loss, oprandom, opclicks, optimed = False , False, False, False, False

# Functions
def run_quit():
    global exit, level_exit, game_exit
    events = pygame.event.get()
    for event in events: 
        if event.type == pygame.QUIT:
            level_exit = False
            game_exit = False
            exit = False

def screen_size(): 
    global screen 
    screen = pygame.display.set_mode((xcords[-1]+90, ycords[-1]+180)) if len(xcords) > 6 else pygame.display.set_mode((440, ycords[-1]+180))
    
def expand_cords(cols,row): # Expand the board
    global xcords, ycords
    xcords = [] #[50, 100, 150, 200, 250, 300, 350]
    ycords = [] #[50, 100, 150]
    x, y = 0, 0
    for i in range(cols):
        x = x + 50
        xcords.append(x)
    for i in range(row):
        y = y + 50
        ycords.append(y)

def level_select():
    
    global exit, level_exit, game_exit
    screen = pygame.display.set_mode((440, 500))
    level_exit = True 
    while level_exit: # Allows you to exit the game               
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT:
                level_exit = False
                game_exit = False
                exit = False
                
        # Updates and draws sprites and screen
        sprcords = ((49, 50), (49, 150), (159, 150), (269, 150)) # back, normal, easy, hard 
        sprites_menu = [ClickableSprite(pygame.Surface((100, 40)), cord[0], cord[1], BLACK) for cord in list(sprcords)]
        sprites_level = pygame.sprite.Group(sprites_menu)
        
        
        screen.fill(SURFACE_COLOR) 
        sprites_level.draw(screen)
        sprites_level.update(events)
        
        # Text
        screen.blit(text_back , (65,60))
        screen.blit(text_norm , (67,160)) 
        screen.blit(text_easy , (188,160)) 
        screen.blit(text_hard , (298,160)) 
        
        # Updates screen
        pygame.display.update()
    

def run_game(row_group):
    global xcords, ycords, game_exit, exit, level_exit, clicks, end, start, screen, click_loss, timed_loss
    click_loss, timed_loss = False , False
    win_check = 0
    clicks = 0
    start = time.time()
    end = start
    game_exit = True 
    while game_exit: # Allows you to exit the game               
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT:
                level_exit = False
                game_exit = False
                exit = False

        # Updates sprites and checks win condition
        did_win = False
        for i in list(row_group):
            if win(i.update(events)): win_check = win_check + 1
            if win_check > 2: did_win = True
        
        if (sprmenu.update(events)) == True:
            game_exit = False 
            level_exit = False
            screen = pygame.display.set_mode((440, 500))
            expand_cords(xsize,ysize)
        
        # text stuff
        text_menu = smallfont.render('Menu' , True , WHITE) # Menu
        text_reset = smallfont.render('Reset' , True , WHITE) # Reset
        text_levels = smallfont.render('Levels' , True , WHITE) # Levels
        text_win = smallfont.render('You Won!' , True , WHITE) # Win
        text_loss = smallfont.render('You Lose!' , True , WHITE) # loss
        
        text_clicks = smallfont.render(('%s Clicks' %(len(xcords)*len(ycords) - clicks)) if game_click else ('Clicks: %s' %clicks), True , WHITE) # Clicks
        text_time = smallfont.render(('Time Left: %ss' %(10 - int(end - start))) if game_timed else ('Time: %ss' %int(end - start)), True , BLACK) # Timer
                       
        # Draws sprites, screen, and text
        screen.fill(SURFACE_COLOR) 
        row_group.draw(screen)
        screen.blit(text_menu , (70, ycords[-1]+60)) # Menu
        screen.blit(text_reset , (172, ycords[-1]+60)) # Reset
        screen.blit(text_levels , (265, ycords[-1]+60)) # Levels
        screen.blit(text_clicks , (60, ycords[-1]+110)) # Clicks
        screen.blit(text_time , (50, 20)) # Timer
        
        # if won or losed, informs the player, else updates timer
        if game_click == True: click_loss = clicks > len(xcords)*len(ycords)
        if game_timed == True: timed_loss = int(end - start) == 10 

        if timed_loss or click_loss:
            win_lose_sprite.draw(screen)
            screen.blit(text_loss , (190, ycords[-1]+110))
        
        elif did_win:
            win_lose_sprite.draw(screen)
            screen.blit(text_win , (190, ycords[-1]+110))
            pygame.display.update()
            time.sleep(2)
            game_exit = False
            game(norm_rand, game_timed, game_click)
            
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
        global game_exit, level_exit, oprandom, optimed, opclicks
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # finds self cords
                    x = self.rect.x
                    y = self.rect.y
                    
                    if x in xcords: self_neighbor(x,y) # Game buttons
                    if x == 251 and y == ycords[-1]+50: level_select() # Level
                    if x == 49 and y == 50: level_exit = False # Back
                    if x == 49 and y == 150: screen_size(), game(oprandom, optimed, opclicks) # Normal
                    if x == 159 and y == 150: expand_cords(2,2), screen_size(), game(oprandom, optimed, opclicks) # Easy 
                    if x == 269 and y == 150: expand_cords(9,6), screen_size(), game(oprandom, optimed, opclicks) # Hard
                    
                    if x == 49 and y == 250: screen_size(), game(oprandom, optimed, opclicks) # Normal
                    if x == 159 and y == 250: expand_cords(2,2), screen_size(), game(oprandom, optimed, opclicks) # Easy 
                    if x == 269 and y == 250: expand_cords(9,6), screen_size(), game(oprandom, optimed, opclicks) # Hard
                    if x == 51 and y == ycords[-1]+50: return True # Menu
                    
                    if x == 151 and y == ycords[-1]+50: # Reset
                        game_exit = False
                        game(norm_rand, game_timed, game_click)

                    if x == 159 and y == 350: # Random
                        oprandom = True if oprandom == False else False 
                        change(self) 
                        
                    if x == 49 and y == 350: # Timed
                        optimed = True if optimed == False else False
                        change(self)
                        
                    if x == 269 and y == 350: # Max clicks
                        opclicks = True if opclicks == False else False
                        change(self)
                    
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
text_back = smallfont.render('<-- Back' , True , WHITE)
text_norm = smallfont.render('Normal' , True , WHITE)
text_easy = smallfont.render('Easy' , True , WHITE)
text_hard = smallfont.render('Hard' , True , WHITE)
text_timed = smallfont.render('Timed' , True , (0, 255, 0))
text_random = smallfont.render('Random' , True , (0, 255, 0))
text_maxclicks = smallfont.render('Max Clicks' , True , (0, 255, 0))
text_howtoplay = smallfont.render('How To Play!' , True , WHITE)
text_howto = smallfont.render('Click on the tiles untill they are all white.' , True , WHITE)

# Sprites Main Menu
sprcords = ((49, 250), (159, 250), (269, 250), (49, 350), (159, 350), (269, 350)) # normal, easy, hard, timed, random, max-clicks
sprites_menu = [ClickableSprite(pygame.Surface((100, 40)), cord[0], cord[1], BLACK) for cord in list(sprcords)]
sprites_list = pygame.sprite.Group(sprites_menu)

# Game something
def game(random_tf, timed, clicks_lim):
    global norm_rand, sprmenu, sprreset, win_lose_sprite, rows, sprexpand, game_timed, game_click 
    norm_rand = random_tf # <--this is part of Reset
    game_timed = timed
    game_click = clicks_lim
    
    
    sprmenu = ClickableSprite(pygame.Surface((88, 40)), 51, ycords[-1]+50, BLACK) # menu
    sprreset = ClickableSprite(pygame.Surface((88, 40)), 151, ycords[-1]+50, BLACK) # reset
    sprexpand = ClickableSprite(pygame.Surface((88, 40)), 251, ycords[-1]+50, BLACK) # expand
    sprclicks = ClickableSprite(pygame.Surface((118, 40)), 51, ycords[-1]+100, BLACK) # clicks
    win_lose_sprite = pygame.sprite.Group(ClickableSprite(pygame.Surface((140, 40)), 180, ycords[-1]+100, BLACK)) # You Win! / You Lose!

    rows = [([ClickableSprite(pygame.Surface((40, 40)), xcords[num], ycords[row], (random_color(random_tf))) for num in range(len(xcords))]) for row in range(len(ycords))]
    run_game(pygame.sprite.Group(rows, sprmenu, sprreset, sprexpand, sprclicks))

def main():
    expand_cords(xsize,ysize) # Expand the board
    global exit
    exit = True
    while exit: 
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT:
                level_exit = False
                game_exit = False
                exit = False

        # Updates and draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        sprites_list.draw(screen)
        sprites_list.update(events)
        
        # Adds text to the screen 
        screen.blit(win_img , (39,80))  
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



# need to find the lose-win then win bug