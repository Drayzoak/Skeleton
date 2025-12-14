import pygame
import sys
from Scripts.Event import Input

def Start():
    for event in pygame.event.get():
        if Input.isQuit(event):
            pygame.quit()
            sys.exit()