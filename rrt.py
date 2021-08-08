import numpy as np
import random
import math
from col_check import *

def nearest_neighbor(X,Y,T):
	dist = np.zeros([T.shape[0],1])
	for i in range(T.shape[0]):
		dist[i,0] = math.sqrt((X-T[i][0])**2+(Y-T[i][1])**2)
	return min(dist), np.where(dist == np.amin(dist))


def rrt(start,goal,obs):

	esp = 2
	endloop = 0

	#Matrix of Nodes (x, y, parent)
	T = np.array([[start[0],start[1],0]])

	#Start RRT
	while endloop != 1:

		#Create random point
		Xrand = random.random()*100
		Yrand = random.random()*100

		#Find the NN to that random point
		minDist, NN = nearest_neighbor(Xrand,Yrand,T)
		
		#Check Distance With Eps
		if minDist > esp:
			#Get angle
			ang = math.atan2(Yrand-T[NN[0][0]][1],Xrand-T[NN[0][0]][0])
			#Calc Points
			Xrand = T[NN[0][0]][0] + esp*math.cos(ang)
			Yrand = T[NN[0][0]][1] + esp*math.sin(ang)

		#Check for Collision
		if col_foundS(T[NN[0][0]][0],T[NN[0][0]][1],Xrand,Yrand,obs) == 0:
			T = np.vstack([T,[Xrand,Yrand,NN[0][0]]])

		if check_goal(Xrand,Yrand,goal):
			endloop = 1

	return T
