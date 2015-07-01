import numpy as np
import math


class Object:
    """Here states the variables and methods for a given object"""


    def __init__(self, x, y, m, r, v, c):
        self.mass = m
        self.radius = r
        self.modVit = v
        self.pos = np.array([x, y])
        self.color = c
        self.vit = np.array([0, 0])
        self.acc = np.array([0, 0])
        self.oldPos = np.array([0, 0])

    def posCalc(self, dT):
        self.oldPos = self.pos
        self.pos = self.acc * math.pow(dT, 2) / 2 + self.vit * dT + self.oldPos
    def vitCalc(self, dT):
        self.vit = (self.pos - self.oldPos) / dT

