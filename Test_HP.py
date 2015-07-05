import pygame, sys
from random import randint
from pygame.locals import *
import time, math
import numpy as np

from Object import Object

#########GRAVITY##################
G = 1
def gravity(a, b):
    if a.mass != 0 and b.mass != 0:
        r = math.pow(b.pos[0] - a.pos[0], 2) + math.pow(b.pos[1] - a.pos[1], 2)
        F = G * a.mass * b.mass / r
        a.acc += (F * (b.pos - a.pos))/(a.mass * math.sqrt(r))
        #b.acc += (F * (a.pos - b.pos))/(b.mass * r)

def merge(a, b):
    if dist(a.pos, b.pos) < a.radius / 1.5 + b.radius / 1.5:
        print "Here"
        a.collided = True
        b.collided = True
        P = a.mass * a.pos + b.mass * b.pos
        V = a.mass * a.vit + b.mass * b.vit
        A = a.mass * a.acc + b.mass * b.acc
        M = a.mass + b.mass
        P /= M
        V /= M
        A /= M
        objects.append(Object(P[0], P[1], M, 1, (0, 255, 0)))
        objects[len(objects) - 1].acc = A
        objects[len(objects) - 1].vit = V
        


##################################

#################################


shift = np.array([0, 0])
def coor_pol_cart(r, t):
    return (r*math.cos(t), r*math.sin(t))
def coor_calc_disp(coor):
    return np.array([coor[0] + shift[0], height - coor[1] + shift[1]])
def coor_disp_calc(coor):
    return np.array([coor[0] - shift[0], height - coor[1] + shift[1]])

pygame.init()
def rename():
    global refresh
    refresh = pygame.display.flip
rename()

def update():
    fenetre.blit(fond,(0,0))
    for i in range(0, len(objects)):
        if objects[i].collided == False:
            pos = zoom * coor_calc_disp(objects[i].pos) #+ np.array([width, height])/2
            pygame.draw.circle(fenetre, objects[i].color, (int(pos[0]), int(pos[1])), int(objects[i].radius * zoom))
            pygame.draw.line(fenetre, (255, 255, 255), pos, np.asarray((pos[0] + objects[i].vit[0], pos[1] - objects[i].vit[1])))
    pygame.display.flip()
    pygame.display.update()

width, height = 1366, 768
zoom = 1

fenetre = pygame.display.set_mode((width, height))

fond = pygame.Surface(fenetre.get_size())
fond.fill((0, 0, 0))
fenetre.blit(fond,(0,0))

clock = pygame.time.Clock()

refresh()

############UTILS#################
def dist(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))


def choose_object_vit(l):
    time.sleep(0.5)
    B1= True
    #objects[l].modVit = input("Speed module: ")
    objects[l].modVit =  20
    #e = input("1 Mouse; 2 Theta")
    e=1
    if e == 1:
	    while B1:
                pygame.event.get()
                (x, y) = pygame.mouse.get_pos()
                coor = coor_disp_calc(np.asarray((x, y)) / zoom)
                objects[l].vit = (coor - objects[l].pos) 
		R1 = pygame.mouse.get_pressed()
		if(R1[0] == True):
		    #objects[l].vit = (coor - objects[l].pos) * (objects[l].modVit /  dist(objects[l].pos, coor))
                    objects[l].vit *= 0.5
		    B1 = False
		update()
    elif e == 2:
		t = input("Theta: ")
		t = t * math.pi/180

		objects[l].vit[0] = objects[l].modVit * math.cos(t)
		objects[l].vit[1] = objects[l].modVit * math.sin(t)

def proto_disk(R):
    theta = 0
    while theta < 2*math.pi:
	for i in range(1, 10):
	    mod = i * R / 9
	    (x, y) = coor_pol_cart(mod, theta)
	    objects.append(Object(x+randint(1, 100), y- randint(1, 100), randint(500000, 10000000), 1, [255, 0, 0]))
	theta += math.pi / 8

def add_object(a):
    B = True
    #a = input("Mass: ")
    #b = input("Radius: ")
    #c = input("Red 1, Green 2, Blue 3:")
    b = 1
    c = 1
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
        objects[len(objects)-1].pos = coor_disp_calc(np.asarray((x, y)) / zoom)
        R = pygame.mouse.get_pressed() 
        if(R[0] == True):
            print (x, y)
            choose_object_vit(len(objects)-1)
            B = False
        update()
#################################
        '''
n = input("How many planets do you want: ")
    for i in range(0, n):
    add_object()
        '''
#choose_object_vit(1)
#choose_object_vit(0)
time.sleep(1)
#CONTINUE?
pygame.key.set_repeat(1, 20)

objects = []

#proto_disk(1700)

dT = 0.005
t = 6 
#objects.append(Object(0, 0, 10000000, 100, (0, 0, 255)))
#objects.append(Object(220, 0, 1000, 100, (0, 0, 255)))
#objects[1].vit = np.asarray((0, 20))
#objects.append(Object(D, 0, 10000000, 100, (0, 0, 255)))
continuer = 1
time.sleep(0.5)
t = time.time()
while continuer:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed() 
            if pressed[0] == 1:
                (x, y) = pygame.mouse.get_pos()
                while pressed != 0:
                    shift -= (np.array([x, y]) - np.asarray(pygame.mouse.get_pos())) / zoom 
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
            if event.key == K_a:
                add_object(1000)
            if event.key == K_z:
                add_object(10000)
            if event.key == K_e:
                add_object(100000)
            if event.key == K_r:
                add_object(1000000)
            if event.key == K_t:
                add_object(10000000)

###############
    for k in range(0, 10):
        for i in range(0, len(objects)):
            objects[i].acc = 0
            for j in range(0, len(objects)):
                if i != j and not objects[i].collided and not objects[j].collided:
                    gravity(objects[i], objects[j])
                    merge(objects[i], objects[j])
        objects = [i for i in objects if not i.collided]
        for i in range(0, len(objects)):
            objects[i].vitCalc(dT)
            objects[i].posCalc(dT)
    

    #dT *= 10


    #print dist(objects[0].pos, objects[1].pos)
    #print "Module acc: " + str(dist((0, 0), objects[1].acc))
    #print "Module vit: " + str(dist((0, 0), objects[1].vit))

    update()

    clock.tick(60)
