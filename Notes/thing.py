import pygame
import random 
  
# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (100, 100, 255) 
WIDTH = 500
HEIGHT = 500

# colors  
BLACK = (0, 0, 0) 

WHITE = (255, 255, 255)
  
# Object class 
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height)) 
  
        
        self.rect = self.image.get_rect() 
        
###  
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
 
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()
 
 
def on_click():
    color = (255, 0, 0) if sprite.image.get_at(
        (0, 0)) != (255, 0, 0) else (0, 255, 0)
    sprite.image.fill(color)

###

pygame.init() 

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
object2_.rect.y = 325

#all_sprites_list.add(object_, object2_) 

sprite = ClickableSprite(pygame.Surface((100, 100)), 50, 50, on_click)
group = pygame.sprite.GroupSingle(sprite)


# Main 
exit = True
#clock = pygame.time.Clock() 
  
while exit: 
    events = pygame.event.get()
    for event in events: 
        if event.type == pygame.QUIT: 
            exit = False
    
    group.update(events)
    all_sprites_list.update() 
    screen.fill(SURFACE_COLOR) 
    all_sprites_list.draw(screen)
    group.draw(screen) 
    pygame.display.update() 
    #clock.tick(60) 
  
pygame.quit() 