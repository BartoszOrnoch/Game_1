import pygame
import random
import math
import settings
from ships import Ship, Enemy


pygame.init()
screen = pygame.display.set_mode(
    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()
title = pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(settings.GAME_ICON)


def initialize_enemies(number_of_enemies):
    return [Enemy(random.randint(0, settings.SCREEN_WIDTH-64), random.randint(0, 400), random.randint(1, 4)) for _ in range(number_of_enemies)]


def detect_colision(x1, y1, x2, y2, max_distance=32):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if distance < max_distance:
        return True


def draw(img, coord_tuple):
    screen.blit(img, coord_tuple)


def main():
    time = 0
    running = True
    playership = Ship(settings.PLAYER_BASE_X, settings.PLAYER_BASE_Y)
    enemies = initialize_enemies(3)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playership.shoot()
                if event.key == pygame.K_r:
                    playership.ammo = 0
                    playership.reloading = True
                    reload_time = time
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                playership.set_direction_X('left')
            if keys[pygame.K_RIGHT]:
                playership.set_direction_X('right')
            if keys[pygame.K_UP]:
                playership.set_direction_Y('up')
            if keys[pygame.K_DOWN]:
                playership.set_direction_Y('down')
            if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                playership.set_direction_X('stop')
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                playership.set_direction_X('stop')
            if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
                playership.set_direction_Y('stop')
            if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                playership.set_direction_Y('stop')
        enemies[:] = [enemy for enemy in enemies if enemy.alive]
        Ship.bullets[:] = [
            bullet for bullet in Ship.bullets if bullet.coordY > 0 and not bullet.hit]
        Enemy.bullets[:] = [bullet for bullet in Enemy.bullets if bullet.coordY <
                            settings.SCREEN_HEIGHT and not bullet.hit]

        screen.fill((255, 255, 255))

        for enemy in enemies:
            if detect_colision(*enemy.give_position(1), *playership.give_position(1), max_distance=64) and not playership.invincible:
                enemy.alive = False
                playership.reduce_lifes()
                invincible_time = time
                continue
            for bullet in playership.bullets:
                if bullet.hit:
                    continue
                if detect_colision(*enemy.give_position(1), *bullet.give_position(1)):
                    enemy.alive = False
                    bullet.hit = True
                    break
            else:
                draw(enemy.img, enemy.give_position(0))
                enemy.move()
                if random.randint(1, 100) == 100:
                    enemy.shoot()

        for bullet in Ship.bullets:
            draw(bullet.img, bullet.give_position(0))
            bullet.move()

        for bullet in Enemy.bullets:
            if detect_colision(*bullet.give_position(1), *playership.give_position(1)) and not playership.invincible:
                playership.reduce_lifes()
                bullet.hit = True
                invincible_time = time
            else:
                draw(bullet.img, bullet.give_position(0))
                bullet.move()

        if playership.reloading:
            if time-3000 > reload_time:
                playership.reload()

        if playership.invincible:
            draw(Enemy.img, playership.give_position(0))
            if time - 3000 > invincible_time:
                playership.invincible = False

        if playership.lifes > 0:
            playership.move()
            draw(playership.img, playership.give_position(0))

        pygame.display.update()
        dt = clock.tick(60)
        time += dt


main()
