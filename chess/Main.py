# need to install pygame
import pygame

# part 1 : set up game loops and variable images
pygame.init()
pygame.display.set_mode([800,800])
font = pygame.font.Font('freesansbold', 20)
timer = pygame.time.Clock(100)
fps = 60

# part 2 : main game loop
    # event handling
