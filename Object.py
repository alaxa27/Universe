import numpy as np
import math


class Object:
    """Here states the variables and methods for a given object"""


    def __init__(self, x, y, m, r, c):
        self.mass = m
        self.radius = r
        self.modVit = 0
        self.pos = np.array([x, y])
        self.color = c
        self.vit = np.array([0, 0])
        self.acc = np.array([0, 0])
        self.oldPos = np.array([0, 0])
	self.radiusCalc()
        self.collided = False

    def posCalc(self, dT):
        self.oldPos = self.pos
        #self.pos = self.acc * math.pow(dT, 2) / 2 + self.vit * dT + self.oldPos
     	self.pos = self.vit * dT + self.pos
    def vitCalc(self, dT):
        #self.vit = (self.pos - self.oldPos) / dT
        self.vit = self.acc * dT + self.vit#self.acc * dT
    def radiusCalc(self):
	#self.radius = self.mass / 100000 + 10
        self.radius = math.log(self.mass/1000 + math.e)
        #self.radius = math.pow(self.mass, 1/2) * 10
