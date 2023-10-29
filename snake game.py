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

 #verified code and indentation
     
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(200,150,90),fruit_rect)
 
  
class MAIN: 
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()  

    def draw_elements(self):
        self.snake.draw_snake() 
        self.fruit.draw_fruit()     

pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_number * cell_size))
clock = pygame.time.Clock()


screen_UPDATE = pygame.USEREVENT
pygame.time.set_timer(screen_UPDATE,160)

main_game = MAIN()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_UPDATE:
            main_game.update()
            #added more code to move snake 
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key ==pygame.K_DOWN:
               main_game.snake.direction = Vector2(0,1)
            if event.key ==pygame.K_RIGHT:
               main_game.snake.direction = Vector2(1,0) 
            if event.key ==pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)

    
    #changed screen color to RGB
    screen.fill((160,200,50)) 
    main_game.draw_elements()
    pygame.display.update() 
    clock.tick(50)





