import pygame

from os import listdir
from os.path import join

class Animation:
    def __init__(self, ani, speed, size):
        self.size = size
        self.loadimage(ani)
        self.timer = 0
        self.index = 0
        self.speed = speed
        self.islast = False
        self.image = self.images[self.index]
        

    def play(self):
        self.timer += 1
        if self.timer % self.speed == 0:
            if self.index < len(self.images) - 1:
                self.islast = False
                self.index += 1
            else:
                self.islast = True
                self.index = 0
        
        self.image = self.images[self.index]
        

    def loadimage(self, name):
    
        path = join("Assets","Character","Skeletoon",name)
        imagelist = listdir(path)

        self.images = []

        for x in imagelist:
            img = pygame.image.load(join(path, x))
            #img = pygame.transform.scale(img, (64 * self.size, 128 * self.size))
            self.images.append(img)