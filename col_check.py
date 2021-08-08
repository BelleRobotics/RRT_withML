import numpy as np

def col_foundS(x1,y1,x2,y2,obs):

	a = x2 - x1
	b = y2 - y1
	m = b/a

	for i in range(obs.shape[0]):

		obsx1 = obs[i][0]
		obsy1 = obs[i][1]
		obsx2 = obs[i][2]
		obsy2 = obs[i][3]
		obsx3 = obs[i][4]
		obsy3 = obs[i][5]
		obsx4 = obs[i][6]
		obsy4 = obs[i][7]

		#Checking Segment y value at obs x1 value
		y_at_obsX1 = m*(obsx1-x1) + y1
		m_y_at_obsX1 = (obsx1-x1)/a

		#Checking Segment y value at obs x2 value
		y_at_obsX2 = m*(obsx2-x1) + y1
		m_y_at_obsX2 = (obsx2-x1)/a
		
		#Checking Segment x value at obs y1 value
		x_at_obsY1 = (obsy1-y1)/m + x1
		m_x_at_obsY1 = (obsy1-y1)/b

		#Checking Segment x value at obs y3 value
		x_at_obsY3 = (obsy3-y1)/m + x1
		m_x_at_obsY3 = (obsy3-y1)/b

		if y_at_obsX1 >= obsy1 and y_at_obsX1 <= obsy3 and m_y_at_obsX1 >= 0 and m_y_at_obsX1 <= 1:
			return 1
		elif y_at_obsX2 >= obsy1 and y_at_obsX2 <= obsy3 and m_y_at_obsX2 >= 0 and m_y_at_obsX2 <= 1:
			return 1
		elif x_at_obsY1 >= obsx1 and x_at_obsY1 <= obsx2 and m_x_at_obsY1 >= 0 and m_x_at_obsY1 <= 1:
			return 1
		elif x_at_obsY3 >= obsx1 and x_at_obsY3 <= obsx2 and m_x_at_obsY3 >= 0 and m_x_at_obsY3 <= 1:
			return 1
		
	return 0

def col_foundP(X,Y,obs):

	for i in range(obs.shape[0]):

		obsx1 = obs[i][0]
		obsy1 = obs[i][1]
		obsx2 = obs[i][2]
		obsy2 = obs[i][3]
		obsx3 = obs[i][4]
		obsy3 = obs[i][5]
		obsx4 = obs[i][6]
		obsy4 = obs[i][7]

		if X >= obsx1 and X <= obsx2 and Y >= obsy1 and Y <= obsy3:
			return 1
	return 0

def check_goal(X,Y,goal):

	x1 = goal[0][0]
	x2 = goal[0][2]
	y1 = goal[0][1]
	y2 = goal[0][5]

	if x1<x2 and y1<y2:
		if X >= x1 and X <= x2 and Y >= y2 and Y <= y1:
			return 1
	elif x1<x2 and y1>y2:
		if X >= x1 and X <= x2 and Y >= y2 and Y <= y1:
			return 1
	elif x1>x2 and y1>y2:
		if X >= x2 and X <= x1 and Y >= y2 and Y <= y1:
			return 1
	elif x1>x2 and y1<y2:
		if X >= x2 and X <= x1 and Y >= y1 and Y <= y2:
			return 1
	return 0