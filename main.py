import pygame
import random
import math


pygame.init()

WIDTH = 800
HEIGHT = 600
SHIP_WIDTH = 64
SHIP_HEIGHT = 64


screen = pygame.display.set_mode((WIDTH, HEIGHT))
title = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufooo.png")
pygame.display.set_icon(icon)
playership_img = pygame.image.load("space-invaders.png")
enemy_img = pygame.image.load("outer-space-alien.png")
bullet_img = pygame.image.load("favicon.png")


playerX = WIDTH // 2 - SHIP_WIDTH // 2
playerY = HEIGHT - (SHIP_HEIGHT + 10)
clock = pygame.time.Clock()


class Bullet():
    
    def __init__(self, coordX, coordY):
        self.coordX = coordX + 16
        self.coordY = coordY + 16
        self.deltaY = 4
        self.hit = False
    
    def draw(self):
        screen.blit(bullet_img, (self.coordX, self.coordY))
    
    def move(self):
        self.coordY += self.deltaY

class EnemyBullet(Bullet):
    def __init__(self, coordX, coordY):
        self.coordX = coordX + 16
        self.coordY = coordY + 16
        self.deltaY = 4
        self.hit = False  

class Ship():

    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY
        self.deltaX = 0
        self.deltaY = 0
        self.bullets = []
    
    def draw(self):
        screen.blit(playership_img, (self.coordX, self.coordY))
    
    def update_coords(self):
        if self.coordX > WIDTH - 64:
            self.coordX = WIDTH - 64
        elif self.coordX < 0:
            self.coordX = 0
        else:
            self.coordX += self.deltaX
    def shoot(self):
        self.bullets.append(Bullet(self.coordX, self.coordY))

class Enemy():

    enemy_bullets = []
    def __init__(self):
        self.coordX = random.randint(0, WIDTH - 64)
        self.coordY = random.randint(64, HEIGHT//2)
        self.deltaX = 2
        self.deltaY = 0
        self.alive = True
    
    def draw(self):
        screen.blit(enemy_img, (self.coordX, self.coordY))
    
    def move(self):
        if self.coordX > WIDTH - 64:
            self.coordX = WIDTH - 64
            self.deltaX *= -1
            self.coordY += 5
        elif self.coordX < 0:
            self.coordX = 0
            self.deltaX *= -1
            self.coordY += 5
        else:
            self.coordX += self.deltaX
    
    def shoot(self):
        if random.randint(1, 200) == 1:
            self.enemy_bullets.append(EnemyBullet(self.coordX, self.coordY))


    


def initialize_enemies(number_of_enemies):
    return [Enemy() for i in range(number_of_enemies)]

def detect_colision(bullet, alien):
    alien_center_x = alien.coordX + 32
    alien_center_y = alien.coordY + 32
    bullet_center_x = bullet.coordX + 16
    bullet_center_y = bullet.coordY + 16
    distance = math.sqrt((alien_center_x - bullet_center_x)**2 + (alien_center_y - bullet_center_y)**2)
    if distance < 32:
        return True
        

def main():
    running = True
    playership = Ship(playerX, playerY)
    enemies = initialize_enemies(3)


    while running:

        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playership.deltaX = -4
                if event.key == pygame.K_RIGHT:
                    playership.deltaX = 4
                if event.key == pygame.K_SPACE:
                    playership.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playership.deltaX = 0
        playership.update_coords()
        playership.draw()
        for bullet in playership.bullets:
            for enemy in enemies:
                if detect_colision(bullet, enemy):
                    enemy.alive = False
                    bullet.hit = True
                    break
        enemies[:] = [enemy for enemy in enemies if enemy.alive]
        playership.bullets[:] = [bullet for bullet in playership.bullets if bullet.coordY > 0 and not bullet.hit]
        for enemy in enemies:
            enemy.move()
            enemy.draw()
            enemy.shoot()
        for ebulet in Enemy.enemy_bullets:
            ebulet.move()
            ebulet.draw()
        for bulet in playership.bullets:
            bulet.move()
            bulet.draw()
        pygame.display.update()
        clock.tick(60)

main()
