import pygame

# VARIABLES
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
xcords = [] #[50, 100, 150, 200, 250, 300, 350]
ycords = [] #[50, 100, 150]
xsize = 7
ysize = 3

# Functions
def expand_cords(cols,rows): # Expand the board
    global xcords
    global ycords
    x = 0
    y = 0
    for i in range(cols):
        x = x + 50
        xcords.append(x)
    for i in range(rows):
        y = y + 50
        ycords.append(y)
    
def change(sprite): # Changes color
    color = BLACK if sprite.image.get_at((0, 0)) != BLACK else WHITE
    sprite.image.fill(color)

def self_neighbor(x,y): # Changes the colors of its self and its neighbors
    aval = xcords.index(x)
    bval = ycords.index(y)
    change(rows[bval][aval]) # its self
    # Find neighbors on Y axis
    if y != 50: change(rows[bval-1][aval])
    if y != ycords[-1]: change(rows[bval+1][aval])
    # Find neighbors on X axis
    if x != 50: change(rows[bval][aval-1])
    if x != xcords[-1]: change(rows[bval][aval+1])

# Object class 
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, color):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color)
        
    def update(self, events):
        # checks to see if it was clicked
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    # finds self cords
                    x = self.rect.x
                    y = self.rect.y

                    self_neighbor(x,y) # Game buttons

pygame.init() 

screen = pygame.display.set_mode((740, 550)) 

# Expand the board
expand_cords(xsize,ysize)

# Sprites
rows = [([ClickableSprite(pygame.Surface((40, 40)), xcords[num], ycords[row], (BLACK)) for num in range(xsize)]) for row in range(ysize)]
group = pygame.sprite.Group(rows)

def main():
    # Allows you to exit the game
    exit = True 
    while exit: 
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: exit = False

        # Updates and draws sprites and screen
        screen.fill((100, 100, 255))
        group.update(events), group.draw(screen)
        
        pygame.display.update() 


main()  
pygame.quit()