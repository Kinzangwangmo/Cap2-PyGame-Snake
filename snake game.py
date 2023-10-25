import pygame,sys 

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
test_surface = pygame.Surface((200,100))

test_surface.fill(pygame.Color('red'))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #  Adding in movement keys
    # More code here
    screen.fill(pygame.Color('blue'))      
    screen.blit(test_surface,(300, 250))        
    pygame.display.update() 
    clock.tick(50)  




