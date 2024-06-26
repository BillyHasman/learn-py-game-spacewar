import pygame
import random

# Initialize the pygame
pygame.init()

# Create the Screen Size 1366 x 788
screen = pygame.display.set_mode((1366 ,788))

# Init Background
background = pygame.image.load('Assets/img/bg_main.jpg')
background = pygame.transform.scale(background, (1366, 788))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Assets/img/spaceship.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('Assets/img/player.png')
playerX = 645 
playerY = 550
speedX = 0.4
speedY = 0.3

# New width and height for player will be (40, 40)
player_resize = pygame.transform.scale(playerImg, (60, 60))

# Enemy
playerImg = pygame.image.load('Assets/img/enemy.png')
enemyX = random.randint(0,1323)
enemyY = 50
enemyX_change = 0.4
enemyY_change = 15
enemy_resize = pygame.transform.scale(playerImg, (80, 80))

# bullet

bulletImg = pygame.image.load('Assets/img/bullet.png')
bulletX = 0
bulletY = 550
bulletX_change = 0
bulletY_change = 1.5
bullet_resize = pygame.transform.scale(bulletImg, (32, 32))

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet_state = "ready"

# Function Player
def player(x, y):
    screen.blit(player_resize, (x, y))  # Drop player to screenGame

# Function Enemy
def enemy(x, y):
    screen.blit(enemy_resize, (x, y))  # Drop enemy to screenGame

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_resize, (x + 16, y + 16 ))  # Drop bullet to screenGame

# Game Loop
running = True
while running:

    # Add blackBG
    screen.fill((0, 0, 0))

    # background Image
    screen.blit(background, (0,0))

    # Player Movement
    keys = pygame.key.get_pressed()
    playerX += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speedX
    playerY += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speedY

     # Bullet Trigger
    if keys[pygame.K_SPACE]:
        fire_bullet(playerX,bulletY)

    # Bullet Movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Boundaries player inside screen
    playerX = max(0, min(playerX, 1323))
    playerY = max(0, min(playerY, 750))
    

    player(playerX, playerY)

    # Enemy Movement
    enemyX += enemyX_change

    # Check boundaries and update direction and position
    if enemyX <= 0 or enemyX >= 1323:
        enemyX_change *= -1
        enemyY += enemyY_change



    enemy(enemyX, enemyY)
    pygame.display.update()

pygame.quit()
