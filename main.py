import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the Screen Size 1366 x 788
screen = pygame.display.set_mode((1366, 788))

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
speedX = 0.5
speedY = 0.4

# New width and height for player will be (60, 60)
player_resize = pygame.transform.scale(playerImg, (60, 60))

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_resize = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Assets/img/enemy.png'))
    enemyX.append(random.randint(0, 1323))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.7)
    enemyY_change.append(30)
    enemy_resize.append(pygame.transform.scale(enemyImg[i], (80, 80)))

# Bullet
bulletImg = pygame.image.load('Assets/img/bullet.png')
bulletX = 0
bulletY = playerY - 10
bulletX_change = 0
bulletY_change = 3
bullet_resize = pygame.transform.scale(bulletImg, (32, 32))

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet_state = "ready"

# Init Score
score = 0

# Function Player
def player(x, y):
    screen.blit(player_resize, (x, y))  # Drop player to screenGame

# Function Enemy
def enemy(x, y, i):
    screen.blit(enemy_resize[i], (x, y))  # Drop enemy to screenGame

# Function Bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_resize, (x + 16, y + 16))  # Drop bullet to screenGame

# Function Collision
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 28:
        return True
    else:
        return False

# Game Loop
running = True
while running:
    # Add blackBG
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))

    # Player Movement
    keys = pygame.key.get_pressed()
    playerX += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speedX
    playerY += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speedY

    # Bullet Trigger
    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bulletX = playerX
            fire_bullet(bulletX, bulletY)

    # Bullet Movement
    if bulletY < -20:
        bulletY = playerY - 10
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Boundaries player inside screen
    playerX = max(0, min(playerX, 1323))
    playerY = max(0, min(playerY, 750))

    # Enemy Movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        # Check boundaries and update direction and position
        if enemyX[i] <= 0 or enemyX[i] >= 1323:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY - 10
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 1323)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
