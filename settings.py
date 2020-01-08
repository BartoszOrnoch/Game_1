import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_WIDTH = 64
SHIP_HEIGHT = 64
ENEMY_WIDTH = 64
ENEMY_HEIGHT = 64
BULLET_WIDTH = 32
BULLET_HEIGHT = 32
PLAYER_BASE_X = SCREEN_WIDTH // 2 - SHIP_WIDTH // 2
PLAYER_BASE_Y = SCREEN_HEIGHT - (SHIP_HEIGHT + 10)

SHIP_IMG = pygame.image.load("images/space-invaders.png")
ENEMY_IMG = pygame.image.load("images/outer-space-alien.png")
BULLET_IMG = pygame.image.load("images/favicon.png")
GAME_ICON = pygame.image.load("images/ufooo.png")
ENEMY_BULLET_IMG = pygame.image.load("images/enemy_bullet.png")

DEFAULT_SHIP_DELTA_X = 4
DEFAULT_SHIP_DELTA_Y = 4
DEFAULT_ENEMY_DELTA_X = 4
DEFAULT_ENEMY_DELTA_Y = 4
DEFAULT_SHIP_BULLET_SPEED = 8
DEFAULT_ENEMY_BULLET_SPEED = 8
