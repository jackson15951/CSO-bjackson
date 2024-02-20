import pygame
import random 
  
# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (100, 100, 255) 
WIDTH = 500
HEIGHT = 500
  
# Object class 
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height)) 
  
        
        self.rect = self.image.get_rect() 
  
  
pygame.init() 

# colors  
BLACK = (0, 0, 0) 

WHITE = (255, 255, 255)

# screen  
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Creating Sprite") 
  
# sprites
all_sprites_list = pygame.sprite.Group() 
  
object_ = Sprite(BLACK, 20, 20) 
object_.rect.x = 200
object_.rect.y = 300
  
object2_ = Sprite(WHITE, 20, 20) 
object2_.rect.x = 200
object2_.rect.y = 400

all_sprites_list.add(object_, object2_ ) 


# Main 
exit = True
clock = pygame.time.Clock() 
  
while exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = False
  
    all_sprites_list.update() 
    screen.fill(SURFACE_COLOR) 
    all_sprites_list.draw(screen) 
    pygame.display.flip() 
    clock.tick(60) 
  
pygame.quit() 