#Create a plot of the values
import numpy as np
import matplotlib.pyplot as plt
import warnings
from col_check import *

def plot(start,goal,obs,T=0,Path=0,Predx=0,Predy=0, basic = True,
			Show_Path=True,Show_Unused_Path=False,Show_First_Path=True,
			Fitted=False,Optimize=False, Optimize_Pred=False):

	#Create plot
	fig, ax = plt.subplots()

	#plot start
	ax.plot(start[0],start[1], 'bo')

	#plot Goal
	goal_x = np.array([goal[0][0], goal[0][2], goal[0][4], goal[0][6]])
	goal_y = np.array([goal[0][1], goal[0][3], goal[0][5], goal[0][7]])
	ax.fill(goal_x,goal_y,'g')

	#plot obs
	for i_obs in range(obs.shape[0]):
	    obs_x = np.array([obs[i_obs,0]+1, obs[i_obs,2]-1, obs[i_obs,4]-1, obs[i_obs,6]+1])
	    obs_y = np.array([obs[i_obs,1]+1, obs[i_obs,3]+1, obs[i_obs,5]-1, obs[i_obs,7]-1])
	    ax.fill(obs_x,obs_y,'r')
 											

	if Show_Path:
		#Create Best Path if passing T
		if basic:
			if Show_Unused_Path:
			#Show Path
				for i in range(T.shape[0]):
					#Show Path
					Path = np.array([T[T.shape[0]-1-i][0],T[T.shape[0]-1-i][1]])
					parent = int(T[T.shape[0]-1-i][2])
					while parent != 0:
						Path = np.vstack([Path,[T[parent][0],T[parent][1]]])
						parent = int(T[parent][2])
					Path = np.vstack([Path,[T[parent][0],T[parent][1]]])
					ax.plot(Path[:,0],Path[:,1],'y--')
			Path = np.array([T[T.shape[0]-1][0]  ,T[T.shape[0]-1][1]])
			parent = int(T[T.shape[0]-1][2])
			while parent != 0:
				Path = np.vstack([Path,[T[parent][0],T[parent][1]]])
				parent = int(T[parent][2])
			Path = np.vstack([Path,[T[parent][0],T[parent][1]]])
			#Show RRT Decision Path
			if Show_First_Path:
				ax.plot(Path[:,0],Path[:,1],'m')
				Optimize = True
			#Optimize the path
			if Optimize:
				j = 4
				for k in range(j):
					check = 0
					for i in range(Path.shape[0]-2):
						if col_foundS(Path[i-check][0],Path[i-check][1],Path[i+2-check][0],Path[i+2-check][1],obs) == 0:
							Path = np.delete(Path,i+1-check,0)
							check = check+1
			#Create a curve fitting matrix for the path
			if Fitted:
				with warnings.catch_warnings():
					warnings.simplefilter('ignore', np.RankWarning)
					z = np.polyfit(Path[:,0],Path[:,1],10)
					p = np.poly1d(z)
					ax.plot(Path[:,0],p(Path[:,0]),'r--')
			else:
				ax.plot(Path[:,0],Path[:,1],'r--')
		else:
			#Show RRT Decision Path
			if Show_First_Path:
				ax.plot(Path[:,0],Path[:,1],'m')
				Optimize = True
			#Optimize the path
			if Optimize:
				j = 4
				for k in range(j):
					check = 0
					for i in range(Path.shape[0]-2):
						if col_foundS(Path[i-check][0],Path[i-check][1],Path[i+2-check][0],Path[i+2-check][1],obs) == 0:
							Path = np.delete(Path,i+1-check,0)
							check = check+1
			#Create a curve fitting matrix for the path
			if Fitted:
				with warnings.catch_warnings():
					warnings.simplefilter('ignore', np.RankWarning)
					z = np.polyfit(Path[:,0],Path[:,1],10)
					p = np.poly1d(z)
					ax.plot(Path[:,0],p(Path[:,0]),'r--')
			else:
				ax.plot(Path[:,0],Path[:,1],'r--')

	#connect start and goal
	Predy = np.insert(Predy,0,start[1])
	Predx = np.insert(Predx,0,start[0])
	Predy = np.insert(Predy,Predy.shape,(goal[0][1]+goal[0][5])/2)
	Predx = np.insert(Predx,Predx.shape,(goal[0][0]+goal[0][2])/2)
	if Optimize_Pred:
		Path = np.vstack([Predx,Predy]).T
		j = 4
		for k in range(j):
			check = 0
			for i in range(Path.shape[0]-2):
				if col_foundS(Path[i-check][0],Path[i-check][1],Path[i+2-check][0],Path[i+2-check][1],obs) == 0:
					Path = np.delete(Path,i+1-check,0)
					check = check+1
		ax.plot(Path[:,0],Path[:,1],'g--')
	ax.plot(Predx,Predy,'b--')


	#Set Figure Limits and Show
	plt.xlim(0, 100)
	plt.ylim([0, 100])
	plt.show()