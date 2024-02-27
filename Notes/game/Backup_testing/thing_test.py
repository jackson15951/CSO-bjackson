import pygame
import random 

# Colors 
SURFACE_COLOR = (100, 100, 255)  
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)

# Stuff
xcords = (50, 100, 150, 200, 250, 300, 350)
ycords = (50, 100, 150)
contwin = 0

# Functions
def random_color(randomc):
    return random.choice((BLACK, WHITE)) if randomc else BLACK

def run_game(row_group):
    # Allows you to exit the game
    global menu_exit
    menu_exit = True 
    global exit
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
                       
        # Draws sprites and screen
        screen.fill(SURFACE_COLOR) 
        row_group.draw(screen)
        screen.blit(text_menu , (70, 210))
        screen.blit(text_reset , (172, 210)) 

        # if won, informs the player
        if did_win:
            win_sprite.draw(screen)
            screen.blit(text_win , (160, 260)) 
        
        # Updates screen
        pygame.display.update()

def change(sprite):
    #change color
    color = BLACK if sprite.image.get_at((0, 0)) != BLACK else WHITE
    sprite.image.fill(color)

def win(group):
    # checks to see if you won
    # if all 21 sprites are white
    global contwin 
    if group == WHITE:
        if contwin < 21: contwin = contwin + 1
        print(contwin)
        if contwin == 21: return True
    else: contwin = 0

def self_neighbor(x, row): # Changes the colors of its self and its neighbors
    aval = xcords.index(x)
    change(row[aval]) # its self
    # Find neighbors on Y axis
    if row == rows[0] or row == rows[2]: change(rows[1][aval])
    if row == rows[1]: change(rows[0][aval]), change(rows[2][aval])
    # Find neighbors on X axis
    if x != 50: change(row[aval-1])
    if x != 350: change(row[aval+1])
        
               
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
                    
                    if y == 50: self_neighbor(x, rows[0]) # top row
                    if y == 100: self_neighbor(x, rows[1]) # mid row   
                    if y == 150: self_neighbor(x, rows[2]) # bottom row 
                    
                    # Other buttons
                    if x == 50 and y == 250: game(True) # Random 
                    if x == 50 and y == 300: game(False) # Normal
                    if x == 50 and y == 200: return True # Menu
                    
                    if x == 150 and y == 200: # Reset
                        menu_exit = False
                        game(norm_rand)
                    
        # finds and reports it's current color
        color = self.image.get_at((0, 0))
        print(color)
        return color

# init
pygame.init() 

# screen  
size = (440, 450) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Game Thing")

win_img = pygame.image.load('/Users/brandonjackson/cs110/CSO-bjackson/Notes/game/Backup_testing/win_img.png')
win_img = pygame.transform.scale(win_img, (360,150))

# defining a font  
smallfont = pygame.font.SysFont('Corbel',25) 

# text
text_random = smallfont.render('Random' , True , WHITE)
text_norm = smallfont.render('Normal' , True , WHITE)
text_menu = smallfont.render('Menu' , True , WHITE)
text_reset = smallfont.render('Reset' , True , WHITE)
text_win = smallfont.render('You Won!' , True , WHITE)
text_howtoplay = smallfont.render('How To Play!' , True , WHITE)
text_howto = smallfont.render('Click on the tiles untill they are all white.' , True , WHITE)

# sprites stuff
win_sprite = pygame.sprite.Group(ClickableSprite(pygame.Surface((140, 40)), 150, 250, BLACK)) # You Win!
sprrandom = ClickableSprite(pygame.Surface((100, 40)), 50, 250, BLACK) # random
sprnorm = ClickableSprite(pygame.Surface((100, 40)), 50, 300, BLACK) # normal
sprmenu = ClickableSprite(pygame.Surface((90, 40)), 50, 200, BLACK) # menu
sprreset = ClickableSprite(pygame.Surface((90, 40)), 150, 200, BLACK) # reset
sprites_list = pygame.sprite.Group(sprrandom, sprnorm)

# Game sprites
def sprrows(row, true_or_false):
    sprites = [ClickableSprite(pygame.Surface((40, 40)), xcords[num], ycords[row], (random_color(true_or_false))) for num in range(7)]
    return sprites

# game something
def game(true_or_false):
    global norm_rand # <--this is part of Reset
    norm_rand = true_or_false 
    
    global rows
    rows = [(sprrows(row, true_or_false)) for row in range(3)]
    run_game(pygame.sprite.Group(rows, sprmenu, sprreset))

def main():
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


