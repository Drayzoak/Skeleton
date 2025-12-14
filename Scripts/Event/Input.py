import pygame

def checkInput():
    pass
    
def verticalMovement():
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        return 1
    elif key[pygame.K_s]:
        return -1
    return 0

def HorizontalMovement():
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        return 1
    if key[pygame.K_d]:
        return -1
    return 0

def isSpace():
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        return True
    return False

def isQuit(event):
    if event.type == pygame.QUIT:
        print("wadawsdw")
        return True
    return False