import pygame

# Intialize the pygame
pygame.init()

# Create the Screen Size 800 x 600
screen = pygame.display.set_mode((800,600))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False