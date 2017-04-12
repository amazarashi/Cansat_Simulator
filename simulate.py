# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt
from math import acos
from math import sqrt
from math import pi

import math
from datetime import datetime
import random
import time

import gpioController

class Simulator(object):

    def __init__(self,goal=False):
        self.name = "Simulator"
        self.figure_path = "./flow.png"
        self.debug_path = "./debug.png"
        self.debug_vector_path = "./debug_v.png"
        self.goal = goal
        self.maxAxisX = 1500
        self.maxAxisY = 1000
        self.wheelDiametor = 1
        self.wheelCicle_for_round = 10
        self.vectorNorm = 10
        self.moveNorm = 100
        self.GoStraightTime = 5
        self.goalPoint,self.startPoint,self.startVector = self.initPoint()
        self.points = []
        self.vectors = []
        self.gpioHandle = gpioController.GPIO()

    def initPoint(self):
        goalPoint = (random.randint(1,self.maxAxisX),random.randint(1,self.maxAxisY))
        startPoint = (random.randint(1,self.maxAxisX),random.randint(1,self.maxAxisY))
        u = self.moveNorm * random.uniform(-1,1)
        v = self.moveNorm * random.uniform(-1,1)
        norm = math.sqrt(u ** 2 + v ** 2)
        startVector = (u/norm, v/norm)
        #goalPoint = (1000,1000)
        #startPoint = (0,0)
        return (goalPoint,startPoint,startVector)

    # def updateFigure(self,currentPoint):
    #     plt.figure()
    #     goalX,goalY = self.goalPoint
    #     currentX,currentY = currentPoint
    #     # points
    #     X = goalX,currentX
    #     Y = goalY,currentY
    #     # vector
    #     U = 0,0
    #     V = 0,0
    #
    #     plt.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
    #     plt.xlim([0,self.maxAxisX])
    #     plt.ylim([0,self.maxAxisY])
    #     plt.grid()
    #     plt.draw()
    #     plt.savefig(self.figure_path)
    #     return

    # def debugFigure(self):
    #     X = [x[0] for x in self.points]
    #     Y = [y[1] for y in self.points]
    #     print("#### DEBUG FIGURE####")
    #     print(X)
    #     print(Y)
    #     plt.clf()
    #     plt.plot(X, Y, 'o',markersize=10)
    #     goalX,goalY = self.goalPoint
    #     plt.plot(goalX,goalY, 'o',label='train')
    #     plt.xlim([0,self.maxAxisX])
    #     plt.ylim([0,self.maxAxisY])
    #     plt.legend()
    #     plt.draw()
    #     plt.savefig(self.debug_path)

    # def debugFigureWithVector(self):
    #     X = [x[0] for x in self.points]
    #     Y = [y[1] for y in self.points]
    #     U = np.array([u[0] for u in self.vectors]) * self.moveNorm
    #     V = np.array([v[1] for v in self.vectors]) * self.moveNorm
    #
    #     plt.figure()
    #
    #     # 矢印（ベクトル）
    #     plt.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
    #
    #     # グラフ表示
    #     plt.xlim([0,self.maxAxisX])
    #     plt.ylim([0,self.maxAxisY])
    #     goalX,goalY = self.goalPoint
    #     plt.plot(goalX,goalY, 'o',label='GOAL')
    #     startX,startY = self.startPoint
    #     plt.plot(startX,startY, 'o',label='START')
    #     plt.grid()
    #     plt.draw()
    #     plt.savefig(self.debug_vector_path)

    def calcVector(self,currentPoint,currentVector):
        goalPoint = self.goalPoint
        gx,gy = goalPoint
        cx,cy = currentPoint

        distance = [gx - cx, gy - cy]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1] / norm]
        return direction

    def moveToNewPoint(self,currentPoint,vector):
        cx,cy = currentPoint
        vx,vy = vector
        newPoint = [ cx + self.moveNorm*vx, cy + self.moveNorm*vy ]
        return newPoint

    def goalCheck(self,currentPoint):
        goalPoint = self.goalPoint
        gx,gy = goalPoint
        cx,cy = currentPoint
        distance = [gx - cx, gy - cy]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        status = False
        if norm < self.moveNorm*0.1:
            status = True
        return status

    def length(self,v):
        return sqrt(v[0]**2+v[1]**2)

    def dot_product(self,v,w):
       return v[0]*w[0]+v[1]*w[1]

    def determinant(self,v,w):
       return v[0]*w[1]-v[1]*w[0]

    def inner_angle(self,v,w):
       cosx = self.dot_product(v,w)/(self.length(v)*self.length(w))
       print("cosx:",cosx)
       cosx = 1 if cosx > 1
       cosx = 0 if cosx < 0
       rad = acos(cosx) # in radians
       return rad*180/pi # returns degrees

    def angle_clockwise(self,A, B):
        """
        return degree from A to B
        ex1) A = [1,1] B = [1,0] -> -45
        ex2) A = [1,0] B = [1,0] -> +45
        """
        inner = self.inner_angle(A,B)
        det = self.determinant(A,B)
        return det*inner

    def rotate(self,vec1,vec2):
        angle = self.angle_clockwise(vec1, vec2)
        rotate_way = "Right"
        if angle < 0:
            # trun Right
            rotate_way = "Right"
        else:
            #turn Left
            rotate_way = "Left"

        rotate_time = self.wheelCicle_for_round*(angle/360)
        return (rotate_time,rotate_way)

    def run(self):
        currentPoint = self.startPoint
        currentX,currentY = currentPoint
        currentVector = self.startVector
        currentU,currentV = currentVector
        self.points.append(currentPoint)
        self.vectors.append(currentVector)

        i = 0
        while self.goal == False:
            print("moving_{0}...".format(i))
            # CHECK GOING VECTOR
            print("currentVec:",currentVector)
            vector = self.calcVector(currentPoint,currentVector)
            #ROTATE SELF DEPENDING ON VECTOR
            rotate_time,rotate_way = self.rotate(vector,currentVector)
            self.gpioHandle.TurnAround(rotate_time,rotate_way)
            currentVector = vector
            print("modifiedVec:",currentVector)
            #GO STRAIGHT
            currentPoint = self.moveToNewPoint(currentPoint,currentVector)
            self.gpioHandle.GoStraight(self.GoStraightTime)
            self.points.append(currentPoint)
            self.vectors.append(currentVector)
            print("currentPoint:",currentPoint)
            #CHECK CURRENT AND GOAL POINT
            goalCheck = self.goalCheck(currentPoint)
            #self.updateFigure(currentPoint)
            if goalCheck:
                print("GOAL!!")
                self.goal = True
                self.gpioHandle.ClearGPIO()
                #self.debugFigure()
                #self.debugFigureWithVector()
            i += 1
            if i > 18:
                print("OverTime,,,")
                #self.debugFigure()
                #self.debugFigureWithVector()
                self.goal = True
            time.sleep(3)
        return
