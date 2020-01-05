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
playerX = 400 - 32
playerY = (HEIGHT-50) - 32
running = True

class Ship():

    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY
        self.deltaX = 0
        self.deltaY = 0
    
    def draw(self):
        screen.blit(playership_img, (self.coordX, self.coordY))
    
    def update_coords(self):
        if self.coordX > WIDTH - 64:
            self.coordX = WIDTH - 64
        elif self.coordX < 0:
            self.coordX = 0
        else:
            self.coordX += self.deltaX

class Enemy():

    def __init__(self):
        self.coordX = random.randint(0, WIDTH - 64)
        self.coordY = random.randint(64, HEIGHT//2)
        self.deltaX = 0.2
        self.deltaY = 0
    
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




playership = Ship(playerX, playerY)
enemy_1 = Enemy()


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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playership.deltaX = 0
    playership.update_coords()
    playership.draw()
    enemy_1.move()
    enemy_1.draw()
    pygame.display.update()
