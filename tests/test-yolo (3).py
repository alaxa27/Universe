import pygame, sys
from random import randint
from pygame.locals import *
import time, math
import numpy as np

from Object import Object

############UTILS#################
def dist(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))
#################################

#########GRAVITY##################
G = 6.67 * math.pow(10, -3)

def gravity(a, b):
    r = math.pow(b.pos[0] - a.pos[0], 2) + math.pow(b.pos[1] - a.pos[1], 2)
    F = G * a.mass * b.mass / r
    a.acc += (F * (b.pos - a.pos))/(a.mass * r)
    b.acc += (F * (a.pos - b.pos))/(b.mass * r)
##################################

#################################

pygame.init()
def rename():
    global refresh
    refresh = pygame.display.flip
rename()

def update():
    fenetre.blit(fond,(0,0))
    for i in range(0, len(objects)):
        pygame.draw.circle(fenetre, objects[i].color, (int(objects[i].pos[0]), int(objects[i].pos[1])), objects[i].radius)
    pygame.display.flip()
    pygame.display.update()

width, height = 1000, 800
fenetre = pygame.display.set_mode((width, height))

fond = pygame.Surface(fenetre.get_size())
fond.fill((250, 250, 250))
fenetre.blit(fond,(0,0))
clock = pygame.time.Clock()

refresh()

#CONTINUE?
pygame.key.set_repeat(1, 20)
continuer = 1

t = time.time()
time.sleep(0.5)
Y = []
X = []
tim = []
V = []
objects = []
objects.append(Object(width/2, height/2, 100, 10, 0, 0, 255))
objects.append(Object(400, height/2-80, 10000000000, 5, 0, 0, 255))
objects.append(Object(width-400, height/2-30, 10, 5, 0, 0, 255))
objects.append(Object(width/2, 0, 1000, 5, 255, 0, 0))
objects.append(Object(width/2-200, height-150, 100000000000, 100, 255, 195, 77))

objects[1].vit[0] = 100
objects[2].vit[0] = -60
objects[3].vit[1] = 200

while continuer:
    for i in range(0, len(objects)):
        objects[i].acc = 0
    for event in pygame.event.get():
        if event.type == QUIT: continuer = 0
        d = 1
        if event.type == KEYDOWN:
            if event.key == K_p:
                import matplotlib.pyplot as plt
                plt.plot(X, Y, 'r--') 
                plt.show()
###############
    for i in range(0, len(objects)):
        for j in range(0, len(objects)):
            if i != j:
                gravity(objects[i], objects[j])

    ti = t
    t = time.time()
    dT = t - ti
    for i in range(0, len(objects)):
        objects[i].posCalc(dT)
        objects[i].vitCalc(dT)

    update()
    #time.sleep(0.1)
    clock.tick(60)

