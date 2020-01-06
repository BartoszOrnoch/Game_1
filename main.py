import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
title = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufooo.png")
pygame.display.set_icon(icon)
playership_img = pygame.image.load("space-invaders.png")
enemy_img = pygame.image.load("outer-space-alien.png")
bullet_img = pygame.image.load("favicon.png")


playerX = 400 - 32
playerY = (HEIGHT-50) - 32


class Bullet():
    
    def __init__(self, coordX, coordY):
        self.coordX = coordX + 32
        self.coordY = coordY + 32
        self.deltaY = -0.5
    
    def draw(self):
        screen.blit(bullet_img, (self.coordX, self.coordY))
    
    def move(self):
        self.coordY += self.deltaY
    

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


    def __init__(self):
        self.coordX = random.randint(0, WIDTH - 64)
        self.coordY = random.randint(64, HEIGHT//2)
        self.deltaX = 0.2
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


def initialize_enemies(number_of_enemies):
    return [Enemy() for i in range(number_of_enemies)]

def detect_colision(bullet, alien):
    if bullet.coordX > alien.coordX + 20:
        return False
    if bullet.coordX < alien.coordX - 20:
        return False
    if bullet.coordY > alien.coordY + 5:
        return False
    if bullet.coordY < alien.coordY - 5:
        return False
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
                    playership.deltaX = -0.5
                if event.key == pygame.K_RIGHT:
                    playership.deltaX = 0.5
                if event.key == pygame.K_SPACE:
                    playership.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playership.deltaX = 0
        playership.update_coords()
        playership.draw()
        for bullet in playership.bullets:
            bullet.draw()
            bullet.move()
            for enemy in enemies:
                if detect_colision(bullet, enemy):
                    enemy.alive = False
        for enemy in enemies:
            if enemy.alive:
                enemy.move()
                enemy.draw()
        playership.bullets = [bullet for bullet in playership.bullets if bullet.coordY > 0]
        pygame.display.update()

main()
