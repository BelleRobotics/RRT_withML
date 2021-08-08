import numpy as np

def get_path(T):
	#Create Best Path
	Path = np.array([ T[T.shape[0]-1][0]  ,T[T.shape[0]-1][1]  ])
	parent = int(T[T.shape[0]-1][2])
	while parent != 0:
		Path = np.vstack([Path,[T[parent][0],T[parent][1]]])
		parent = int(T[parent][2])
	Path = np.vstack([Path,[T[parent][0],T[parent][1]]])
	return Path
