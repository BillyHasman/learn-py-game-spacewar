import pygame

# Intialize the pygame
pygame.init()

# Create the Screen Size 1366 x 788
screen = pygame.display.set_mode((1366 ,788))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Assets/img/spaceship.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('Assets/img/player.png')
playerX = 645 
playerY = 450

# New width and height for player will be (40, 40)
img_resize = pygame.transform.scale(playerImg, (40, 40))

# Function
def player():
    # screen.blit(playerImg, (playerX,playerY)) # Drop player to screenGame
    screen.blit(img_resize, (playerX,playerY))
    

# Game Loop
running = True
while running:

    # Add blackBG
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()