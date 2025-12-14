
from enum import Enum
import pygame

from Scripts.Component.Animation import Animation
from Scripts.Object.EntityBase import Entity, direction
from Scripts.Event import Input

class player(Entity):

    def __init__(self, x, y, width, height, size, win):
        super(player, self).__init__(x , y, width, height, size)

        self.level = 0
        self.Healthp = 100
        self.Attackp = 6
        self.State = State(1)
        self.idle = Animation("idle",6, size)
        self.attack = Animation("attack",6, size)
        self.walk = Animation("walk",6 , size)
        self.screen = win

    def Update(self, pos):
        
        #pygame.draw.rect(self.screen , (0,0,0),self.rect)
        if self.State.value == 3 or Input.isSpace() :
            if self.attack.islast == False:
                self.Attack()
            else:
                self.attack.islast = False
                self.State = State.Idle
            
        elif self.State.value == 1 or self.State.value == 2:
            self.Movement(pos)

        
    def Movement(self,pos):

        if Input.verticalMovement() != 0:
            if Input.verticalMovement() == 1:
                pos.y += 5 
                self.direction = direction(1)
                self.walk.play()
                self.UpdateAnimation(self.walk.image)

            else:
                pos.y -= 5
                self.direction = direction(2)
                self.walk.play()
                self.UpdateAnimation(self.walk.image)

            self.State = State.Movement

        elif Input.HorizontalMovement() != 0:
            if Input.HorizontalMovement() == 1:
                pos.x += 5 
                self.direction = direction(3)
                self.walk.play()
                self.UpdateAnimation(self.walk.image)
            else:
                pos.x -= 5
                self.direction = direction(4)
                self.walk.play()
                self.UpdateAnimation(self.walk.image)
            self.State = State.Movement
        
        else:
            self.idle.play()
            self.UpdateAnimation(self.idle.image)
            self.State = State.Idle
        
    def Attack(self):
        self.attack.play()
        self.UpdateAnimation(self.attack.image)
        self.State = State.Attack
    
    def UpdateAnimation(self, image):
        if self.direction.value == 4 :
            image = pygame.transform.flip(image, True, False)
        self.screen.blit(image, self.getpos())

class State(Enum):
    Idle = 1
    Movement = 2
    Attack = 3