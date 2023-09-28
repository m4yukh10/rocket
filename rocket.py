import pygame
import os
WIDTH,HEIGHT = 700,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")
#correct syntax = pygame.image.load(os.path.join('name_of_folder','name of file'))
#changes are done here for some issues

RED_SPACESHIP = pygame.image.load(os.path.join('red_spaceship_100.png'))
YELLOW_SPACESHIP = pygame.image.load(os.path.join('yellow_spaceship.png'))
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
#resized versions of spaceships are below: 
RESIZED_RED = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
RESIZED_YELLOW = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

WHITE = (255,255,255)
FPS = 60
def window(red,yellow):
    WIN.fill(WHITE)
    WIN.blit(RESIZED_RED,(red.x,red.y))
    WIN.blit(RESIZED_YELLOW,(yellow.x,yellow.y))
    pygame.display.update()
    

def main():
    red = pygame.Rect(100,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        red.x += 2
        yellow.x += 1
        window(red,yellow)
                
    pygame.quit(red,yellow)

if __name__ == "__main__":
    main()
    
