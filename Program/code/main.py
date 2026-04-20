#libraries
import pygame
import subprocess
import sys
import os

#inits
pygame.init()
pygame.joystick.init()

#setup
clock = pygame.time.Clock()
fps = 75
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("whuy")

#main loops(hehe no s)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.update()
    clock.tick(fps)

pygame.quit