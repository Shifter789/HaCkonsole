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


#display
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("whuy")


#apps and images
apps = ["game.py"]
images = ["Program\code\Images\Game.png"]

image_scale = [(100,150)]
image_location = [(100,20)]

app_image_index = 0

Image = pygame.image.load(images[app_image_index]).convert()
Image = pygame.transform.scale(Image, image_scale[app_image_index])


#main loops(hehe no sgit)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(Image, image_location[app_image_index])
    pygame.display.update()
    clock.tick(fps)

pygame.quit