import pygame
pygame.init()
background_colour = (58, 58, 58)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('My First Game Screen')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
