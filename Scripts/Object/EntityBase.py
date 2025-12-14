from enum import Enum
import pygame
from Scripts.Utilities.Maths import Vector2

class Entity(object):
    def __init__(self, x, y, width, height, size , ):

        self.sceenpos = Vector2(7,4)
        self.pos = Vector2
        self.size = size
        self.rect = pygame.Rect(x*64*size, y*64*size, width*size, height*size)
        self.alive = True
        self.active = True
        self.cooldown = 5
        self.timer = 0
        self.direction = direction(3)

    def getposgrid(self):
        return self.sceenpos 

    def getpos(self):
        return (self.sceenpos.x * 64 * self.size, self.sceenpos.y * 64 * self.size - 64*self.size)

class direction(Enum):
    Up = 1
    Dn = 2
    Lf = 3
    Rt = 4

class Block(object):
    def __init__(self, x, y , img):
        self.sceenpos = Vector2(x,y)
        self.image = img

    def getposgrid(self):
        return self.sceenpos

    def getpos(self):
        return Vector2(self.sceenpos.x * 64 * self.Size, self.sceenpos.y * 64 * self.size)

    def Update(self, win):
        win.blit(self.image, (self.sceenpos.x, self.sceenpos.y))
