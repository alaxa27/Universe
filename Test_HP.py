import pygame, sys
from random import randint
from pygame.locals import *
import time, math
import numpy as np

from Object import Object


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
        pygame.draw.line(fenetre, (0, 0, 0), objects[i].pos, objects[i].pos + objects[i].vit)
    pygame.display.flip()
    pygame.display.update()

width, height = 1280, 960
fenetre = pygame.display.set_mode((width, height))

fond = pygame.Surface(fenetre.get_size())
fond.fill((250, 250, 250))
fenetre.blit(fond,(0,0))
clock = pygame.time.Clock()

refresh()

objects = []
############UTILS#################
def dist(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))

objects.append(Object(width/2, height/2, 1000000000, 40, 0, (0, 0, 255)))
objects.append(Object(350, 479, 2, 10, 30, (100, 200, 1)))

def choose_object_vit(l):
    time.sleep(0.5)
    B1= True
    while B1:
        pygame.event.get()
        (x, y) = pygame.mouse.get_pos()
        objects[l].vit = np.asarray((x, y)) - objects[l].pos
        R1 = pygame.mouse.get_pressed()
        if(R1[0] == True):
            print objects[l].vit
            objects[l].vit = (np.asarray((x, y)) - objects[l].pos) * (objects[l].modVit /  dist(objects[l].pos, (x, y)))
            B1 = False
        update()

def add_object():
    B = True
    a = input("Mass: ")
    b = input("Radius: ")
    f = input("Speed module: ")
    c = input("Red 1, Green 2, Blue 3:")
    if c == 1:
        c = [255, 0, 0]
    elif c == 2:
        c = [0, 255, 0]
    elif c == 3:
        c = [0, 0, 255]

    objects.append(Object(width/2, height/2, a, b, f, c))
    while B:
        pygame.event.wait()
        (x, y) = pygame.mouse.get_pos()
        objects[len(objects)-1].pos = np.asarray((x, y))
        R = pygame.mouse.get_pressed() 
        if(R[0] == True):
            print (x, y)
            choose_object_vit(len(objects)-1)
            B = False
        update()
#################################
n = input("How many planets do you want: ")
for i in range(0, n):
    add_object()
choose_object_vit(1)
#CONTINUE?
pygame.key.set_repeat(1, 20)
continuer = 1

t = time.time()
time.sleep(0.01)

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
    dT *= 10
    for i in range(0, len(objects)):
        objects[i].posCalc(dT)
        objects[i].vitCalc(dT)

    #print "Module acc: " + str(dist((0, 0), objects[1].acc))
    #print "Module vit: " + str(dist((0, 0), objects[1].vit))

    update()
    clock.tick(60)

