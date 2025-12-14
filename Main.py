import pygame

from os import listdir
from os.path import join
from Scripts.Utilities.Maths import Vector2
from Scripts.Event import Event
from Scripts.World.World import World
from Scripts.Object.Player import player

pygame.init()

pygame.display.set_caption("Snake")

WIDTH , HEIGHT = 1280,720
SIZE = 1.4
window = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

offset = Vector2(0,0)
textFont = pygame.font.SysFont("Arial" ,16)
isMap = False

tilesmapimage = []

World = World(20)
World.Start(SIZE)

pl = player(7,4, 64, 128,SIZE,window)


def setMap(name):
    image = pygame.image.load(join("Assets","SpriteSheet" ,"TileMap",name)).convert_alpha()
    image = pygame.transform.scale(image, (16*SIZE, 16*SIZE)) 
    _,_,width,height = image.get_rect()
    tiles = []

    for i in range(WIDTH// width + 1):
        for j in range(HEIGHT// height +1):
            pos = ( i*width + offsetX, j*height +offsetY)
            tiles.append(pos)
    
    return tiles, image

def loadimage(name):
    image = pygame.image.load(join("Assets","SpriteSheet" ,"TileMap",name)).convert_alpha()
    image = pygame.transform.scale(image, (32*SIZE, 32*SIZE))
    
    _,_,width,height = image.get_rect()
    return image


def drawText(text, font, text_col, x, y):
    img = font.render(text , True, text_col)
    window.blit(img,(x,y)) 

while True:
    
    pygame.display.fill =(255,255,255)
    window.fill((0,0,0))
    
    Event.Start()

    World.Update(window,(offset.x,offset.y))
    pl.Update(offset)
    drawText("FPS " + str(clock.get_fps()), textFont, (0,0,0), 1180,20)
    drawText(str(pl.State), textFont, (0,0,0), 1180,40)
    drawText(str(pl.direction), textFont, (0,0,0), 1180,60)
    pygame.display.update()
    
    clock.tick(60)