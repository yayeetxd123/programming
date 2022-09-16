import pygame
import random
import math
import sys

#items needed to run the script - icon.png , enemy.png , player.png

#initializing the game
pygame.init()
timer = False
#creating screen
height = 800
width = 600
screen = pygame.display.set_mode((height , width))

#caption
pygame.display.set_caption("dodgeit")

#icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#player
temp_playerImg = pygame.image.load("player.png")
playerImg = pygame.transform.scale(temp_playerImg, (90,90))
playerX = 350
playerY = 490
player_vel = 4

#enemy class
class ENEMY:
    def __init__(self):
        self.enemyImg = pygame.transform.scale(pygame.image.load("enemy.png"), (100,100))
        self.enemyX = random.randint(10,750)
        self.enemyY = random.randint(0,250)
        self.enemy_vel = 7

    def draw_enemy(self):
        screen.blit(self.enemyImg, (self.enemyX, self.enemyY))

    def enemy_boundaries(self):
        global score_count, current_level
        if self.enemyY  >= 600:
            self.enemyY = 30
            self.enemyX = random.randint(10,750)

            score_count += 1

        #second level
        if score_count >= 100:
            current_level = 2
            self.enemy_vel += 1
            if self.enemy_vel >= 8:
                self.enemy_vel = 8
            screen.fill((255,0,0))

        #third level
        if score_count >= 250:
            current_level = 3
            self.enemy_vel += 1
            if self.enemy_vel >= 9:
                self.enemy_vel = 9
            screen.fill((0,255,0))

        #fourth level
        if score_count >= 500:
            current_level = 4
            self.enemy_vel += 1
            if self.enemy_vel >= 10:
                self.enemy_vel = 10
            screen.fill((255,255,255))

        #fifth level
        if score_count >= 750:
            current_level = 5
            self.enemy_vel += 1
            if self.enemy_vel >= 11:
                self.enemy_vel = 11
            screen.fill((0,0,0))

        if score_count >= 1000:
            pygame.time.wait(100)
            display_game_over()

        if timer == True:
            pygame.time.wait(100)
            display_lost_game()
            running = False

    def collision(self):
        global playerX, playerY, running, score_count, timer
        collision = Collision(self.enemyX,self.enemyY,playerX,playerY)
        if collision:
            playerX = 10000
            playerY = 10000
            timer = True

        self.enemyY += self.enemy_vel

enemy = ENEMY()
enemy2 = ENEMY()
enemy3 = ENEMY()
enemy4 = ENEMY()
enemy5 = ENEMY()
enemy6 = ENEMY()
enemy7 = ENEMY()
enemy8 = ENEMY()
enemy9 = ENEMY()
enemy10 = ENEMY()
#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255,255,0)
white = (255,255,255)
light_blue = (0,255,255)

#score
score_font = pygame.font.Font("freesansbold.ttf", 25)
scoreX = 15
scoreY = 15
score_count = 0

#fps
fps = 60
clock = pygame.time.Clock()

#level counter
current_level = 1
levelX = 650
levelY = 20

#game over font
game_overX = 200
game_overY = 250
game_over_font = pygame.font.Font("freesansbold.ttf", 90)


def display_game_over():
    game_over_text = game_over_font.render("You Won!", True, yellow)
    screen.blit(game_over_text, (game_overX, game_overY))

def display_lost_game():
    lost_game = game_over_font.render("You Lost!", True, yellow)
    screen.blit(lost_game, (game_overX, game_overY))
#just moved this in a function so its more readable
def enemies_boundaries():
    enemy.enemy_boundaries()
    enemy2.enemy_boundaries()
    enemy3.enemy_boundaries()
    enemy4.enemy_boundaries()
    enemy5.enemy_boundaries()
    enemy6.enemy_boundaries()
    enemy7.enemy_boundaries()
    enemy8.enemy_boundaries()
    enemy9.enemy_boundaries()
    enemy10.enemy_boundaries()

#just moved this in a function so its more readable
def enemies_collisions():
    enemy.collision()
    enemy2.collision()
    enemy3.collision()
    enemy4.collision()
    enemy5.collision()
    enemy6.collision()
    enemy7.collision()
    enemy8.collision()
    enemy9.collision()
    enemy10.collision()

#display score on the screen
def show_score(x,y):
    score_text = score_font.render("Score : " + str(score_count),True,yellow)
    screen.blit(score_text, (x,y))

#display level on the screen
def show_level(x,y):
    level_text = score_font.render("Level: " + str(current_level), True, yellow)
    screen.blit(level_text, (x,y))

#display player
def player(x,y):
    screen.blit(playerImg, (x,y))

#collision function
def Collision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False

#just moved this in a function so its more readable
def draw_enemies():
    enemy.draw_enemy()
    enemy2.draw_enemy()
    enemy3.draw_enemy()
    enemy4.draw_enemy()
    enemy5.draw_enemy()
    enemy6.draw_enemy()
    enemy7.draw_enemy()
    enemy8.draw_enemy()
    enemy9.draw_enemy()
    enemy10.draw_enemy()

running = True

#game loop
while running:
    clock.tick(fps)
    screen.fill((0,0,255))
    #checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= player_vel

    elif keys[pygame.K_RIGHT]:
        playerX += player_vel

    #player boundaries
    if playerX <= 1:
        playerX = 1
    elif playerX >= 749:
        playerX = 749

    #enemies boundaries
    enemies_boundaries()

    #checking for Collision with the enemies
    enemies_collisions()

    #calling the functions
    show_score(scoreX, scoreY)
    player(playerX, playerY)
    draw_enemies()
    show_level(levelX, levelY)
    pygame.display.update()
