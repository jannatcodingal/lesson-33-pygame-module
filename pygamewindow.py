import pygame
pygame.init()
screen=pygame.display.set_mode((400,500))
done=False
while not True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()