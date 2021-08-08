from gen_obs import *
from rrt import *
from get_path import *
from sklearn.neural_network import MLPClassifier
import numpy as np
import csv

def train_start():
	[start, goal, obs] = obs_make()
	T = rrt(start,goal,obs)
	Path = np.flip(get_path(T))
	Pathsize = Path.shape[0]
	Path = np.vstack([Path,np.zeros([100-Path.shape[0],2])])
	Path = np.array([np.hstack([Path[:,0],Path[:,1]])])
	data = np.hstack([[start],goal,Path,[[Pathsize]]])
	np.savetxt('training_data.txt',data, fmt='%1.3f')

def train(num):
	f=open('training_data.txt','a')
	for i in range(num):
		[start, goal, obs] = obs_make()
		T = rrt(start,goal,obs)
		Path = np.flip(get_path(T))
		Pathsize = Path.shape[0]
		Path = np.vstack([Path,np.zeros([100-Path.shape[0],2])])
		Path = np.array([np.hstack([Path[:,0],Path[:,1]])])
		data = np.hstack([[start],goal,Path,[[Pathsize]]])
		np.savetxt(f, data, fmt='%1.3f', newline="\n")
	f.close()

def test_ten():
	f=open('test_data.txt','a')
	for i in range(9):
		[start, goal, obs] = obs_make()
		T = rrt(start,goal,obs)
		Path = np.flip(get_path(T))
		Pathsize = Path.shape[0]
		Path = np.vstack([Path,np.zeros([100-Path.shape[0],2])])
		Path = np.array([np.hstack([Path[:,0],Path[:,1]])])
		data = np.hstack([[start],goal,Path,[[Pathsize]]])
		np.savetxt(f, data, fmt='%1.3f', newline="\n")
	f.close()

def test_start():
	[start, goal, obs] = obs_make()
	T = rrt(start,goal,obs)
	Path = np.flip(get_path(T))
	Pathsize = Path.shape[0]
	Path = np.vstack([Path,np.zeros([100-Path.shape[0],2])])
	Path = np.array([np.hstack([Path[:,0],Path[:,1]])])
	data = np.hstack([[start],goal,Path,[[Pathsize]]])
	np.savetxt('test_data.txt',data, fmt='%1.3f')
	test_ten()

def read_txt(txtname="test"):
	for i in range(211):
		if txtname == "test":
			file = open('test_data.txt')
		else:
			file = open('training_data.txt')
		col = [column[i] for column in csv.reader(file,delimiter=' ')]
		var = np.array([float(col[0])])
		for j in range(1,len(col)):
			temp_var = float(col[j])
			var = np.vstack([var,temp_var])
		if i == 0:
			data = np.array(var)
		else:
			data = np.hstack([data,var])
		file.close()
	return data