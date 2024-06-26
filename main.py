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
playerY = 550

# New width and height for player will be (40, 40)
player_resize = pygame.transform.scale(playerImg, (40, 40))


# Function
def player(x,y):
    # screen.blit(playerImg, (playerX,playerY)) 
    screen.blit(player_resize, (x,y)) # Drop player to screenGame
    

# Game Loop
running = True
while running:

    # Add blackBG
    screen.fill((0,0,0))

    speedX = 0.3
    speedY = 0.2
    keys = pygame.key.get_pressed()
    playerX += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speedX
    playerY += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speedY

    print(playerX)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player(playerX,playerY)
    pygame.display.update()