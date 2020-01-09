import settings


class Bullet():

    img = settings.BULLET_IMG
    direction = -1

    def __init__(self, coordX, coordY, deltaY, deltaX=0):
        self.coordX = coordX + settings.BULLET_WIDTH // 2
        self.coordY = coordY + settings.BULLET_HEIGHT // 2
        self.deltaX = deltaX
        self.deltaY = deltaY * self.direction
        self.hit = False

    # 0 - left, bottom corner, 1 - center
    def give_position(self, position):
        if position == 0:
            return (self.coordX, self.coordY)
        if position == 1:
            return (self.coordX + settings.BULLET_WIDTH // 2, self.coordY + settings.BULLET_WIDTH // 2)

    def move(self):
        self.coordY += self.deltaY


class EnemyBullet(Bullet):

    direction = 1
    img = settings.ENEMY_BULLET_IMG


class Ship():

    bullets = []
    img = settings.SHIP_IMG

    def __init__(self, coordX, coordY, deltaX=0, deltaY=0):
        self.coordX = coordX
        self.coordY = coordY
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.lifes = 3
        self.alive = True
        self.reloading = False
        self.ammo = 6
        self.invincible = False

    def reduce_lifes(self):
        if self.lifes > 0:
            self.lifes -= 1
            self.coordX = settings.PLAYER_BASE_X
            self.coordY = settings.PLAYER_BASE_Y
            self.invincible = True
        else:
            print('game_over')

    def give_position(self, position):
        if position == 0:
            return (self.coordX, self.coordY)
        if position == 1:
            return (self.coordX + settings.SHIP_WIDTH // 2, self.coordY + settings.SHIP_HEIGHT // 2)

    def move(self):
        if self.coordX > settings.SCREEN_WIDTH - settings.SHIP_WIDTH and self.deltaX > 0:
            self.deltaX = 0
        elif self.coordX < 0 and self.deltaX < 0:
            self.deltaX = 0
        self.coordX += self.deltaX

        if self.coordY < 0 and self.deltaY < 0:
            self.deltaY = 0
        elif self.coordY > settings.SCREEN_HEIGHT - settings.SHIP_HEIGHT and self.deltaY > 0:
            self.deltaY = 0
        self.coordY += self.deltaY

    def set_direction_X(self, direction):
        if direction == 'left':
            self.deltaX = settings.DEFAULT_SHIP_DELTA_X * -1
        elif direction == 'right':
            self.deltaX = settings.DEFAULT_SHIP_DELTA_X
        elif direction == 'stop':
            self.deltaX = 0

    def set_direction_Y(self, direction):
        if direction == 'up':
            self.deltaY = settings.DEFAULT_SHIP_DELTA_Y * -1
        elif direction == 'down':
            self.deltaY = settings.DEFAULT_SHIP_DELTA_Y
        elif direction == 'stop':
            self.deltaY = 0

    def shoot(self, speed=settings.DEFAULT_SHIP_BULLET_SPEED):
        if self.ammo > 0:
            Ship.bullets.append(Bullet(self.coordX, self.coordY, speed))
            self.ammo -= 1

    def reload(self):
        self.ammo = 6
        self.reloading = False


class Enemy(Ship):
    bullets = []
    img = settings.ENEMY_IMG

    def __init__(self, coordX, coordY, deltaX=0, deltaY=0):
        super().__init__(coordX, coordY, deltaX, deltaY)

    def move(self):
        if self.coordX > settings.SCREEN_WIDTH - settings.ENEMY_WIDTH:
            self.coordX = settings.SCREEN_WIDTH - settings.ENEMY_WIDTH
            self.deltaX *= -1
            self.coordY += 5
        elif self.coordX < 0:
            self.coordX = 0
            self.deltaX *= -1
            self.coordY += 5
        else:
            self.coordX += self.deltaX

    def shoot(self, speed=settings.DEFAULT_ENEMY_BULLET_SPEED):
        Enemy.bullets.append(EnemyBullet(self.coordX, self.coordY, speed))
