class Bullet():
    
    def __init__(self, coordX, coordY, deltaY, deltaX=0):
        self.coordX = coordX + 16
        self.coordY = coordY + 16
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.hit = False
    
    def give_position(self):
        return (self.coordX, self.coordY)
    
    def move(self):
        self.coordY += self.deltaY
    
    def give_center(self):
        return (self.coordX + 16, self.coordY + 16)

class Ship():
    direction_of_bullets = -1
    bullets = []
    def __init__(self, coordX, coordY, deltaX=0, deltaY=0):
        self.coordX = coordX
        self.coordY = coordY
        self.deltaX = deltaX
        self.deltaY = deltaY
    
    def give_center(self):
        return (self.coordX + 32, self.coordY + 32)
    
    def give_position(self):
        return (self.coordX, self.coordY)
    
    def move(self, width):
        if self.coordX > width - 64:
            self.coordX = width - 64
        elif self.coordX < 0:
            self.coordX = 0
        else:
            self.coordX += self.deltaX
            self.coordY += self.deltaY

    def shoot(self, speed=7):
        Ship.bullets.append(Bullet(self.coordX, self.coordY, speed*Ship.direction_of_bullets))


class Enemy(Ship):
    direction_of_bullets = 1
    bullets = []
    def __init__(self, coordX, coordY, deltaX=0, deltaY=0):
        super().__init__(coordX, coordY, deltaX, deltaY)
        self.alive = True
    
    def move(self, width):
        if self.coordX > width - 64:
            self.coordX = width - 64
            self.deltaX *= -1
            self.coordY += 5
        elif self.coordX < 0:
            self.coordX = 0
            self.deltaX *= -1
            self.coordY += 5
        else:
            self.coordX += self.deltaX
            
    
    def shoot(self, speed=7):
        Enemy.bullets.append(Bullet(self.coordX, self.coordY, speed*Enemy.direction_of_bullets))