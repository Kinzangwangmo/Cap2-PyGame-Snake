import pygame,sys,random 
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(4,10),Vector2(5,10),Vector2(6,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size) 
            pygame.draw.rect(screen,(250,150,130),block_rect)
        
    def move_snake(self):
        body_copy = self.body[:-1] 
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]   

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.x = 0
        self.y = 9
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
snake = SNAKE()

screen_UPDATE = pygame.USEREVENT
pygame.time.set_timer(screen_UPDATE,160)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_UPDATE:
            snake.move_snake()  
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key ==pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key ==pygame.K_RIGHT:
                snake.direction = Vector2(1,0) 
            if event.key ==pygame.K_LEFT:
                snake.direction = Vector2(-1,0)

    
    #changed screen color to RGB
    screen.fill((160,200,50)) 
    fruit.draw_fruit() 
    snake.draw_snake()    
    pygame.display.update() 
    clock.tick(50)





