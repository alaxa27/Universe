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
#objects.append(Object(width-100, height/2, 100, 10, 0, 0, 255))
#BOOBS
objects.append(Object(width/2-200, height/2, 1, 50, 254, 195, 172))
objects.append(Object(width/2-110, height/2, 1, 50, 254, 195, 172))
#TITTIES
objects.append(Object(width/2-205, height/2+5, 1, 10, 186, 155, 97))
objects.append(Object(width/2-105, height/2+5, 1, 10, 186, 155, 97))

objects.append(Object(width/2-206, height/2+6, 1, 2, 139 , 108 , 66))
objects.append(Object(width/2-104, height/2+6, 1, 2, 139 , 108 , 66))


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
    #time.sleep(1/60)
    clock.tick(60)

