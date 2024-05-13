import pygame

# VARIABLES
xcords = [50, 100, 150, 200, 250, 300, 350]
ycords = [50, 100, 150]

# Functions
def change(sprite): sprite.image.fill((0, 0, 0)) if sprite.image.get_at((0, 0)) != (0, 0, 0) else sprite.image.fill((255, 255, 255)) # Changes color

def self_neighbor(x,y): # Changes the colors of its self and its neighbors
    change(rows[ycords.index(y)][xcords.index(x)]) # its self
    # Find neighbors on Y axis
    if y != 50: change(rows[ycords.index(y)-1][xcords.index(x)])
    if y != 150: change(rows[ycords.index(y)+1][xcords.index(x)])
    # Find neighbors on X axis
    if x != 50: change(rows[ycords.index(y)][xcords.index(x)-1])
    if x != 350: change(rows[ycords.index(y)][xcords.index(x)+1])

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
                if self.rect.collidepoint(event.pos): self_neighbor(self.rect.x,self.rect.y) # Game buttons

pygame.init() 
screen = pygame.display.set_mode((435, 250)) 

# Sprites
rows = [([ClickableSprite(pygame.Surface((40, 40)), xcords[num], ycords[row], ((0, 0, 0))) for num in range(7)]) for row in range(3)]
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

