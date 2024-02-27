import pygame

# VARIABLES
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
xcords = (50, 100, 150, 200, 250, 300, 350)
ycords = (50, 100, 150)

# Functions
def change(sprite): # Changes color
    color = BLACK if sprite.image.get_at((0, 0)) != BLACK else WHITE
    sprite.image.fill(color)

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

                    if y == 50: self_neighbor(x, rows[0]) # top row
                    if y == 100: self_neighbor(x, rows[1]) # mid row   
                    if y == 150: self_neighbor(x, rows[2]) # bottom row 

pygame.init() 

screen = pygame.display.set_mode((440, 400)) 

# Sprites
rows = [([ClickableSprite(pygame.Surface((40, 40)), xcords[num], ycords[row], (BLACK)) for num in range(7)]) for row in range(3)]
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