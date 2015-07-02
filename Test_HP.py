import pygame, sys
from random import randint
from pygame.locals import *
import time, math
import numpy as np

from Object import Object

#########GRAVITY##################
G = 6.67 * math.pow(10, -11)

def gravity(a, b):
    r = math.pow(b.pos[0] - a.pos[0], 2) + math.pow(b.pos[1] - a.pos[1], 2)
    F = G * a.mass * b.mass / r
    a.acc += (F * (b.pos - a.pos))/(a.mass * r)
    b.acc += (F * (a.pos - b.pos))/(b.mass * r)
##################################

#################################


shift = np.array([0, 0])
def coor_calc_disp(coor):
    return np.array([coor[0] - shift[0], height - coor[1] - shift[1]])
def coor_disp_calc(coor):
    return np.array([coor[0] - shift[0], height - coor[1] - shift[1]])

pygame.init()
def rename():
    global refresh
    refresh = pygame.display.flip
rename()

def update():
    fenetre.blit(fond,(0,0))
    for i in range(0, len(objects)):
        pos = zoom * coor_calc_disp(objects[i].pos) + np.array([width, height])/2
        if zoom = 1:
            pos -= np.array([width, height])/2
        pygame.draw.circle(fenetre, objects[i].color, (int(pos[0]), int(pos[1])), int(objects[i].radius * zoom))
        pygame.draw.line(fenetre, (0, 0, 0), pos, (pos[0] + objects[i].vit[0], pos[1] - objects[i].vit[1]))
    pygame.display.flip()
    pygame.display.update()

width, height = 1366, 768
zoom = 1

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

objects.append(Object(width/2, height/2, math.pow(5, 24), 100, (0, 0, 255)))
objects.append(Object(10, 10, 1000, 21, (100, 200, 1)))

def choose_object_vit(l):
    time.sleep(0.5)
    B1= True
    objects[l].modVit = input("Speed module: ")
    e = input("1 Mouse; 2 Theta")
    if e == 1:
	    while B1:
		pygame.event.get()
		(x, y) = pygame.mouse.get_pos()
                coor = coor_disp_calc(np.asarray((x, y)))
		objects[l].vit = coor - objects[l].pos
		R1 = pygame.mouse.get_pressed()
		if(R1[0] == True):
		    objects[l].vit = (coor - objects[l].pos) * (objects[l].modVit /  dist(objects[l].pos, coor))
		    B1 = False
		update()
    elif e == 2:
		t = input("Theta: ")
		t = t * math.pi/180

		objects[l].vit[0] = objects[l].modVit * math.cos(t)
		objects[l].vit[1] = objects[l].modVit * math.sin(t)


def add_object():
    B = True
    a = input("Mass: ")
    b = input("Radius: ")
    c = input("Red 1, Green 2, Blue 3:")
    if c == 1:
        c = [255, 0, 0]
    elif c == 2:
        c = [0, 255, 0]
    elif c == 3:
        c = [0, 0, 255]

    objects.append(Object(width/2, height/2, a, b, c))
    while B:
        pygame.event.wait()
        (x, y) = pygame.mouse.get_pos()
        objects[len(objects)-1].pos = coor_disp_calc(np.asarray((x, y)))
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
time.sleep(0.5)

while continuer:
    for i in range(0, len(objects)):
        objects[i].acc = 0
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed() 
            if pressed[0] == 1:
                (x, y) = pygame.mouse.get_pos()
                while pressed != 0:
                    shift += (np.array([x, y]) - np.asarray(pygame.mouse.get_pos())) / zoom 
                    (x, y) = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONUP:
                            pressed = 0
                    update()
            elif event.button == 4:
                zoom *= 1.3
            elif event.button == 5:
                zoom /= 1.3
        if event.type == QUIT: continuer = 0
        d = 1
        if event.type == KEYDOWN:
            if event.key == K_p:
                zoom *= 10
            if event.key == K_m:
                zoom /= 10

###############
    for i in range(0, len(objects)):
        for j in range(0, len(objects)):
            if i != j:
                gravity(objects[i], objects[j])

    ti = t
    t = time.time()
    dT = t - ti
    #dT *= 10
    dT = 0.17
    for i in range(0, len(objects)):
        objects[i].posCalc(dT)
        objects[i].vitCalc(dT)

    #print "Module acc: " + str(dist((0, 0), objects[1].acc))
    #print "Module vit: " + str(dist((0, 0), objects[1].vit))

    update()

    clock.tick(60)

