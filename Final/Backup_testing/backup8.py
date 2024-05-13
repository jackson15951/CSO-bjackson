import time
import pygame
import random 
import pathlib

# VARIABLES
SURFACE_COLOR = (100, 100, 255)  
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
contwin = 0
copy_size = 0
puzz = []
xsize = 7
ysize = 6
did_win, modepuzzle, click_loss, timed_loss, oprandom, opclicks, opmono, optimed = False, False, False, False, False, False, False, False 

# Functions
def what_level(x,y):
    global level_what 
    level_what = (x,y)
    level_list = (('Level-%s' %(3*row+num+1), num*110+49, row*60+150) for num in range(3) for row in range(7)) 
    for level in list(level_list): 
        if x == level[1] and y == level[2]: pygame.display.set_caption(level[0])

def puzzle(puzzle):
    global cur_puzz, puzz_copy, copy_size, modepuzzle, puzz
    modepuzzle = puzzle
    puzz = []
    if modepuzzle:
        cur_puzz = random.choice(puzz_list)
        puzz_copy = [([ClickableSprite(pygame.Surface((40, 40)), xcords[num]+1, ycords[row]+(len(ycords)*100), ((BLACK if cur_puzz[(len(xcords)*row)+num] == 0 else WHITE))) for num in range(len(xcords))]) for row in range(len(ycords))]
        puzz_copy = pygame.sprite.Group(puzz_copy)
        copy_size = len(ycords)+180

def run_quit(events):
    global exit, level_exit, game_exit
    for event in events: 
        if event.type == pygame.QUIT:
            level_exit = False
            game_exit = False
            exit = False

def screen_size(): 
    global screen, copy_size 
    if modepuzzle == False: copy_size = 0
    screen = pygame.display.set_mode((xcords[-1]+90, ycords[-1]+180+copy_size)) if len(xcords) > 6 else pygame.display.set_mode((440, ycords[-1]+180))
    
def expand_cords(cols,row): # Expand the board
    global xcords, ycords
    xcords = [] #[50, 100, 150, 200, 250, 300, 350]
    ycords = [] #[50, 100, 150]
    for i in range(cols): xcords.append(i * 50 + 50)
    for i in range(row): ycords.append(i * 50 + 50)

def level_custom(custom_mode):
    global exit, level_exit, game_exit, oprandom, optimed, opclicks
    # Sprites Custom
    sprcords = ((49, 50),(47, 150), (157, 150), (267, 150), (47, 250), (157, 250), (267, 250)) # timed, random, max-clicks
    sprites_custom = [ClickableSprite(pygame.Surface((100, 40)), cord[0], cord[1], BLACK) for cord in list(sprcords)]
    sprites_level_custom = pygame.sprite.Group(sprites_custom)
    screen = pygame.display.set_mode((440, 600))
    level_exit = True 
    while level_exit:              
        events = pygame.event.get()
        run_quit(events) # Allows you to exit the game
        
        # Updates and draws sprites and screen (47, 250), (157, 250), (267, 250)
        screen.fill(SURFACE_COLOR)
               
        if custom_mode:
            sprites_level_custom.draw(screen)
            # Text
            text_timed = smallfont.render('Timed' , True , (0, 255, 0))
            text_random = smallfont.render('Random' , True , (0, 255, 0))
            text_maxclicks = smallfont.render('Max Clicks' , True , (0, 255, 0))
            screen.blit(text_timed , (70,260))
            screen.blit(text_random , (173,260))
            screen.blit(text_maxclicks , (273,260))
        #sprites_level = [([ClickableSprite(pygame.Surface((100, 40)), num*110+49, row*60+150, BLACK) for num in range(3)]) for row in range(7)] 
        else: 
            oprandom = False
            optimed = False
            opclicks = False
            
            sprback = ClickableSprite(pygame.Surface((100, 40)), 49, 50, BLACK)
            sprites_level = [([ClickableSprite(pygame.Surface((100, 40)), num*110+49, row*60+150, BLACK) for num in range(3)]) for row in range(7)] 
            sprites_level_custom = pygame.sprite.Group(sprites_level, sprback)
            sprites_level_custom.draw(screen)
            # Text
            for row in range(7): 
                for num in range(3): screen.blit(smallfont.render('Level-%s' %(3*row+num+1) , True , WHITE) , (110*num+60, 60*row+160)) 
            
        screen.blit(text_back , (65,60))
        sprites_level_custom.update(events)
        # Updates screen
        pygame.display.update()
    
def run_game(row_group):
    global xcords, ycords, game_exit, exit, level_exit, clicks, end, start, screen, click_loss, timed_loss, did_win, next_level
    click_loss, timed_loss = False , False
    win_check = 0
    clicks = 0
    start = time.time()
    end = start
    game_exit = True 
    while game_exit:              
        events = pygame.event.get()
        run_quit(events) # Allows you to exit the game

        # Updates sprites and checks win condition
        did_win = False
        for i in list(row_group):
            if win(i.update(events)): win_check = win_check + 1
            if win_check > 2: did_win = True
        
        if (sprmenu.update(events)) == True:
            game_exit = False 
            level_exit = False
            pygame.display.set_caption("Game Thing")
            screen = pygame.display.set_mode((440, 500))
            expand_cords(xsize,ysize)
        
        # text stuff
        text_menu = smallfont.render('Menu' , True , WHITE) # Menu
        text_reset = smallfont.render('Reset' , True , WHITE) # Reset
        text_levels = smallfont.render('Levels' , True , WHITE) # Levels
        text_win = smallfont.render('You Won!     Next-->' , True , WHITE) # Win
        text_loss = smallfont.render('You Lose!' , True , WHITE) # loss
        
        text_clicks = smallfont.render(('%s Clicks' %(len(xcords)*len(ycords)+5 - clicks)) if game_click else ('Clicks: %s' %clicks), True , WHITE) # Clicks
        text_time = smallfont.render(('Time Left: %ss' %(10 - int(end - start))) if game_timed else ('Time: %ss' %int(end - start)), True , BLACK) # Timer
                       
        # Draws sprites, screen, and text
        screen.fill(SURFACE_COLOR) 
        row_group.draw(screen)
        screen.blit(text_levels , (68, ycords[-1]+60)) # Levels
        screen.blit(text_reset , (172, ycords[-1]+60)) # Reset
        screen.blit(text_menu , (270, ycords[-1]+60)) # Menu
        screen.blit(text_clicks , (60, ycords[-1]+110)) # Clicks
        screen.blit(text_time , (50, 20)) # Timer
        
        if modepuzzle: puzz_copy.draw(screen)
        
        # if won or losed, informs the player, else updates timer
        if game_click == True: click_loss = clicks > len(xcords)*len(ycords)+5
        if game_timed == True: timed_loss = int(end - start) == 10 

        if timed_loss or click_loss:
            win_lose_sprite.draw(screen)
            screen.blit(text_loss , (190, ycords[-1]+110))
        
        elif did_win:
            win_lose_sprite.draw(screen)
            screen.blit(text_win , (190, ycords[-1]+110))
            win_lose_sprite.update(events)
            next_level = (level_what[0]+110 if level_what[0]+110 != 379 else 49), (level_what[1] if level_what[0]+110 != 379 else level_what[1]+60)

            pygame.display.update()
            
        else: end = time.time() 
        
        # Updates screen
        pygame.display.update()

def change(sprite):
    #change color
    color = BLACK if sprite.image.get_at((0, 0)) != BLACK else WHITE
    sprite.image.fill(color)

def win(group):
    # if all sprites are white you won
    global contwin, puzz, modepuzzle, puzz_list  
    if group == WHITE:
        if contwin < (len(xcords)*len(ycords)): contwin = contwin + 1
    else: contwin = 0
    
    if len(puzz) < len(xcords)*len(ycords)+4: puzz.append(contwin) 
    else: 
        puzz = []
        puzz.append(contwin)
    
    if modepuzzle == True: 
        if puzz == cur_puzz: return True
        print(puzz)
        print(cur_puzz)
    elif contwin == (len(xcords)*len(ycords)): return True

def self_neighbor(x,y): # Changes the colors of its self and its neighbors
    global rows, clicks, game_mono
    clicks = clicks + 1
    aval = xcords.index(x)
    bval = ycords.index(y)
    change(rows[bval][aval]) # its self 
    if not game_mono:
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
        global game_exit, level_exit, oprandom, optimed, opclicks, opmono, modepuzzle, puzz, did_win
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # finds self cords
                    x = self.rect.x 
                    y = self.rect.y 

                    if x == 180 and y == ycords[-1]+100 and did_win:
                        did_win = False
                        x, y = next_level
                        print('yes')
                    
                    if x in xcords: self_neighbor(x,y) # Game buttons
                    if x == 251 and y == ycords[-1]+50: return True # Menu
                    if x == 51 and y == ycords[-1]+50: level_custom(False) # Level
                    if x == 49 and y == 50: # Back
                        level_exit = False
                        screen_size()
                    
                    #if x == 268 and y == 250: screen_size(), game(oprandom, optimed, opclicks) # Tutorial
                    if x == 48 and y == 250: expand_cords(xsize,ysize), level_custom(False) # Normal
                    if x == 158 and y == 250: level_custom(True) # Custom

                    if x == 151 and y == ycords[-1]+50: # Reset
                        game_exit = False
                        puzz = []
                        game(norm_rand, game_timed, game_click, game_mono)

                    if x == 157 and y == 250: # Random
                        oprandom = True if oprandom == False else False 
                        change(self) 
                    
                    if x == 47 and y == 250: # Timed
                        optimed = True if optimed == False else False
                        change(self)
                    
                    if x == 267 and y == 250: # Max clicks
                        opclicks = True if opclicks == False else False
                        change(self)
                    
                    if x == 49 and y == 150: what_level(x,y), expand_cords(2,2), puzzle(False), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-1 yes
                    if x == 159 and y == 150: what_level(x,y), expand_cords(3,2), puzzle(False), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-2 yes
                    if x == 269 and y == 150: what_level(x,y), expand_cords(3,3), puzzle(False), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-3 yes
                    if x == 49 and y == 210: what_level(x,y), expand_cords(4,3), puzzle(False), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-4 yes
                    if x == 159 and y == 210: what_level(x,y), expand_cords(5,3), puzzle(False), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-5 yes
                    if x == 269 and y == 210: what_level(x,y), expand_cords(6,3), puzzle(False), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-6 yes
                    if x == 49 and y == 270: what_level(x,y), expand_cords(7,3), puzzle(False), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-7 yes
                    if x == 159 and y == 270: what_level(x,y), expand_cords(7,3), puzzle(True), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-8 yes
                    if x == 269 and y == 270: what_level(x,y), expand_cords(7,3), puzzle(True), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-9 yes
                    if x == 49 and y == 330: what_level(x,y), expand_cords(7,3), puzzle(True), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-10 yes
                    if x == 159 and y == 330: what_level(x,y), expand_cords(7,3), puzzle(True), screen_size(), game(oprandom, optimed, opclicks, opmono) # level-11 
                    if x == 269 and y == 330: what_level(x,y), expand_cords(3,3), puzzle(False), screen_size(), game(True, optimed, opclicks, opmono) # level-12 yes
                    if x == 49 and y == 390: what_level(x,y), expand_cords(4,3), puzzle(False), screen_size(), game(True, optimed, opclicks, opmono) # level-13 yes
                    if x == 159 and y == 390: what_level(x,y), expand_cords(7,3), puzzle(False), screen_size(), game(True, optimed, opclicks, opmono) # level-14 
                    if x == 269 and y == 390: what_level(x,y), expand_cords(3,3), puzzle(False), screen_size(), game(True, optimed, True, opmono) # level-15 
                    if x == 49 and y == 450: what_level(x,y), expand_cords(3,3), puzzle(False), screen_size(), game(True, optimed, True, opmono) # level-16
                    if x == 159 and y == 450: what_level(x,y), expand_cords(3,3), puzzle(False), screen_size(), game(oprandom, optimed, opclicks, True) # level-17
                    if x == 269 and y == 450: what_level(x,y), expand_cords(7,3), puzzle(True), screen_size(), game(oprandom, True, opclicks, True) # level-18
                    if x == 49 and y == 510: what_level(x,y), expand_cords(7,3), puzzle(True), screen_size(), game(True, True, opclicks, True) # level-19
                    if x == 159 and y == 510: what_level(x,y), expand_cords(7,3), puzzle(True), screen_size(), game(True, True, opclicks, True) # level-20
                    if x == 269 and y == 510: what_level(x,y), expand_cords(7,3), puzzle(True), screen_size(), game(True, True, opclicks, True) # level-21
                    
        # finds and reports it's current color
        color = self.image.get_at((0, 0))
        return color

# init
pygame.init() 

# Menu Screen  
pygame.display.set_caption("Game Thing")

path = pathlib.Path(__file__).parent.resolve()
win_img = pygame.image.load('%s/how_to.png' %path)
win_img = pygame.transform.scale(win_img, (360,150))

# defining a font  
smallfont = pygame.font.SysFont('Corbel',25) 

# text
text_back = smallfont.render('<-- Back' , True , WHITE)
text_norm = smallfont.render('Normal' , True , WHITE)
text_howtoplay = smallfont.render('How To Play!' , True , WHITE)
text_howto = smallfont.render('Click on the tiles untill they are all white.' , True , WHITE)
text_custom = smallfont.render('Custom' , True , WHITE)
text_tutorial = smallfont.render('Tutorial' , True , WHITE)
text_gamemod = smallfont.render('--- Game Modes ---' , True , WHITE)

# Sprites Main Menu
sprcords = ((48, 250), (158, 250), (268, 250), (48, 350), (158, 350), (268, 350)) # normal, easy, hard, timed, random, max-clicks
sprites_menu = [ClickableSprite(pygame.Surface((100, 40)), cord[0], cord[1], BLACK) for cord in list(sprcords)]
sprites_list = pygame.sprite.Group(sprites_menu)

# list of puzzles
p1 = [0, 1, 0, 0, 0, 1, 0, 0, 1, 2, 3, 4, 5, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
p2 = [1, 0, 0, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
p3 = [1, 2, 0, 1, 0, 1, 2, 0, 0, 1, 2, 3, 0, 0, 1, 2, 0, 1, 0, 1, 2, 0, 0, 0, 0]
p4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0]
p5 = [1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
p6 = [0, 0, 1, 2, 3, 0, 0, 1, 2, 3, 0, 1, 2, 3, 0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0]
p7 = [1, 2, 3, 0, 1, 2, 3, 0, 1, 0, 1, 0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 0, 0, 0, 0]
p8 = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
p9 =  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]                      #[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
p10 = [0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0]
p11 = [0, 1, 2, 0, 1, 2, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 2, 0, 1, 2, 0, 0, 0, 0, 0]
p12 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
p13 = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
p14 = [1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
p15 = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
p16 = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
p17 = [0, 1, 2, 0, 1, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1, 2, 0, 0, 0, 0, 0]
puzz_list = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17)

# Game something
def game(random_tf, timed, clicks_lim, monomode):
    global norm_rand, sprmenu, sprreset, win_lose_sprite, rows, sprexpand, game_timed, game_click, puzz_copy, game_mono
    norm_rand = random_tf # <--this is part of Reset
    game_timed = timed
    game_click = clicks_lim
    game_mono = monomode
    
    sprexpand= ClickableSprite(pygame.Surface((88, 40)), 51, ycords[-1]+50, BLACK) # levels
    sprreset = ClickableSprite(pygame.Surface((88, 40)), 151, ycords[-1]+50, BLACK) # reset
    sprmenu = ClickableSprite(pygame.Surface((88, 40)), 251, ycords[-1]+50, BLACK) # menu
    sprclicks = ClickableSprite(pygame.Surface((118, 40)), 51, ycords[-1]+100, BLACK) # clicks
    win_lose_sprite = pygame.sprite.Group(ClickableSprite(pygame.Surface((180, 40)), 180, ycords[-1]+100, BLACK)) # You Win! / You Lose!

    rows = [([ClickableSprite(pygame.Surface((40, 40)), xcords[num], ycords[row], (random_color(random_tf))) for num in range(len(xcords))]) for row in range(len(ycords))]
    run_game(pygame.sprite.Group(rows, sprmenu, sprreset, sprexpand, sprclicks))

def main():
    expand_cords(xsize,ysize) # Expand the board
    screen_size()
    global exit
    exit = True
    while exit: 
        events = pygame.event.get()
        run_quit(events) # Allows you to exit the game

        # Updates and draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        sprites_list.draw(screen)
        sprites_list.update(events)
        
        # Adds text to the screen 
        screen.blit(win_img , (39,80))  
        screen.blit(text_norm , (67,260)) 
        screen.blit(text_howtoplay , (170,30))
        screen.blit(text_howto , (50,60))
        screen.blit(text_custom , (174,260)) 
        screen.blit(text_tutorial , (285,260)) 
        screen.blit(text_gamemod , (67,225))
        
        if exit == False: screen.fill(SURFACE_COLOR)

        pygame.display.update() 
        
main()
pygame.quit()

