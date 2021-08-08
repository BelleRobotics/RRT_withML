import numpy as np
import random
import math
from col_check import *

def get_obs():
	#generate only obs
	#Obs Gen 			x1,y1,x2,y2,x3,y3,x4,y4
	obs = np.array([[ 5, 10, 15, 10, 15, 20,  5, 20],
					[10, 40, 20, 40, 20, 50, 10, 50],
					[20, 70, 30, 70, 30, 80, 20, 80],
					[30, 20, 40, 20, 40, 30, 30, 30],
					[40, 50, 50, 50, 50, 60, 40, 60],
					[50,  5, 60,  5, 60, 15, 50, 15],
					[55, 80, 65, 80, 65, 90, 55, 90],
					[60, 40, 70, 40, 70, 50, 60, 50],
					[70, 20, 80, 20, 80, 30, 70, 30],
					[75, 65, 85, 65, 85, 75, 75, 75]])
	return obs

def obs_make():
	#Generate start, goal and obstacles

	#Obs Gen 			x1,y1,x2,y2,x3,y3,x4,y4
	obs = np.array([[ 5, 10, 15, 10, 15, 20,  5, 20],
					[10, 40, 20, 40, 20, 50, 10, 50],
					[20, 70, 30, 70, 30, 80, 20, 80],
					[30, 20, 40, 20, 40, 30, 30, 30],
					[40, 50, 50, 50, 50, 60, 40, 60],
					[50,  5, 60,  5, 60, 15, 50, 15],
					[55, 80, 65, 80, 65, 90, 55, 90],
					[60, 40, 70, 40, 70, 50, 60, 50],
					[70, 20, 80, 20, 80, 30, 70, 30],
					[75, 65, 85, 65, 85, 75, 75, 75]])
	
	#Set centroids of obs
	centroids = np.array([[10, 15],[15, 45],[25, 75],[35, 35],[45, 55],
						[55, 85],[50, 10],[65, 45],[75, 25],[80, 70]])


	#Find Start Pos
	possible = 0
	while possible == 0:
		possible = 1
		#Create a random start position and make sure its far enough away from obs
		start = np.array([random.random()*100, random.random()*100]) #Start Position (x,y)
		for i in range(centroids.shape[0]):
			dist = math.sqrt((start[0]-centroids[i][0])**2 + (start[1]-centroids[i][1])**2)
			if dist < 11:
				possible = 0

	#Determine the quad that the start location is in
	if start[0] <= 50 and start[1] <= 50:
		q = 3
	elif start[0] >= 50 and start[1] <= 50:
		q = 4
	elif start[0] >= 50 and start[1] >= 50:
		q = 1
	else:
		q = 2


	#Goal Region (x1 y1 x2 y2 x3 y3 x4 y4)
	possible = 0
	while possible == 0:
		possible = 1
		x_goal = random.random()
		y_goal = random.random()

		#Assign goal based on quad
		if q == 1:
			#x 0-50 / y 0-50
			x_goal = x_goal*50
			y_goal = y_goal*50
			if x_goal < 10:
				x_goal = 10
			if y_goal < 10:
				y_goal = 10
			goal = np.array([[x_goal-5, y_goal+5, x_goal+5, y_goal+5, x_goal+5, y_goal-5, x_goal-5, y_goal-5]])

		elif q == 2:
			#x 50-100 / y 0-50
			x_goal = x_goal*50 + 50
			y_goal = y_goal*50
			if x_goal > 90:
				x_goal = 90
			if y_goal < 10:
				y_goal = 10
			goal = np.array([[x_goal-5, y_goal+5, x_goal+5, y_goal+5, x_goal+5, y_goal-5, x_goal-5, y_goal-5]])

		elif q == 3:
			#x 0-50 / y 0-50
			x_goal = x_goal*50 + 50
			y_goal = y_goal*50 + 50
			if x_goal > 90:
				x_goal = 90
			if y_goal > 90:
				y_goal = 90
			goal = np.array([[x_goal-5, y_goal+5, x_goal+5, y_goal+5, x_goal+5, y_goal-5, x_goal-5, y_goal-5]])

		else:
			#x 0-50 / y 0-50
			x_goal = x_goal*50
			y_goal = y_goal*50 + 50
			if x_goal < 10:
				x_goal = 10
			if y_goal > 90:
				y_goal = 90
			goal = np.array([[x_goal-5, y_goal+5, x_goal+5, y_goal+5, x_goal+5, y_goal-5, x_goal-5, y_goal-5]])
		
		#Check to make sure goal is not intersecting with obs
		if col_foundP(goal[0][0],goal[0][1],obs):
			possible = 0
		elif col_foundP(goal[0][2],goal[0][3],obs):
			possible = 0
		elif col_foundP(goal[0][4],goal[0][5],obs):
			possible = 0
		elif col_foundP(goal[0][6],goal[0][7],obs):
			possible = 0

	return start, goal, obs
