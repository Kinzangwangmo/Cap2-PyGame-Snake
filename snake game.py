import pygame,sys,random 
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(4,10),Vector2(3,10),Vector2(2,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size) 
            pygame.draw.rect(screen,(250,150,130),block_rect)
        
    def move_snake(self):
        if self.new_block == True:
           body_copy = self.body[:]
           body_copy.insert(0,body_copy[0] + self.direction)
           self.body = body_copy[:]
           self.new_block = False
        else:   
           body_copy = self.body[:-1] 
           body_copy.insert(0,body_copy[0] + self.direction) 
           self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class FRUIT:
    def __init__(self):
        self.randomize()
           
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(200,150,90),fruit_rect)
        
 # create x and  y position 

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(Orange,fruit_rect)
       # pygame.draw.rect(screen,(200,150,90),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number -1)
        self.y = random.randint(0,cell_number -1) 
        self.pos = Vector2(self.x,self.y)   
 
  
class MAIN: 
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()  

    def draw_elements(self):
        self.snake.draw_snake() 
        self.fruit.draw_fruit()  

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
    # check if snake is outside the screen
    # check if snake hit itself
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()    


    def game_over(self):
        pygame.quit()
        sys.exit()
              
                

pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_number * cell_size))
clock = pygame.time.Clock()
Orange = pygame.image.load('Orange.png').convert_alpha() 
Orange = pygame.transform.scale(Orange, (20, 20))



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
                if main_game.snake.direction.y !=1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key ==pygame.K_DOWN:
               if main_game.snake.direction.y != -1:
                   main_game.snake.direction = Vector2(0,1)
            if event.key ==pygame.K_RIGHT:
               if main_game.snake.direction.x != -1:
                   main_game.snake.direction = Vector2(1,0) 
            if event.key ==pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

    
    #changed screen color to RGB
    screen.fill((160,200,50)) 
    main_game.draw_elements()
    pygame.display.update() 
    clock.tick(50)





