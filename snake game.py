import pygame,sys,random 
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = 4
        self.y = 3
        self.pos = Vector2(self.x,self.y)
 # create x and  y position  
 
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(200,150,90),fruit_rect)

        
pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #changed screen color to RGB
    screen.fill((160,200,50)) 
    fruit.draw_fruit()     
    pygame.display.update() 
    clock.tick(50)





