# need to install pygame
import pygame

# part 1 : set up game loops and variable images
pygame.init()
pygame.display.set_mode([800,800])
font = pygame.font.Font('freesansbold.ttf', 20)
pygame.display.set_caption('Chess game')
timer = pygame.time.Clock(100)
fps = 60
  # game variables and images

# part 2 : main game loop
    # event handling
run = True
while run:
    timer.tick(fps)
    screen.fill('black')