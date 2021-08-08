from init_training import *
from plotter import *
from gen_obs import *
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import numpy as np
import time

'''
#Implement to run basic RRT search program
from gen_obs import *
from rrt import *
from get_path import *

[start, goal, obs] = obs_make()
T = rrt(start,goal,obs)
print(start[0],' ',start[1])
print(goal)
plot(start,goal,obs,T,Show_Unused_Path=True,Show_First_Path=True)
'''


### Create Data (if needed) ###

#Create a text file to write training data in
#train_start()
#Add 50 training data points to training text file
#add_train()
#create a text with ten RRT start/goal and path to test ML against
#test_start()


### Create ML Model ###

#Read Train Data
data_train = pd.DataFrame(read_txt(txtname="train"))
input_data_train = data_train.iloc[:,:10]
output_data_train = data_train.iloc[:,10:]
#print(output_data_train.shape)

#Read Test Data
data_test = pd.DataFrame(read_txt(txtname="test"))
input_data_test = data_test.iloc[:,:10]
output_data_test = np.array(data_test.iloc[:,10:])
#print(output_data_test.shape)

#Model with Decision Tree Regressor
dtr = DecisionTreeRegressor().fit(input_data_train, output_data_train)
#Test models
pred = np.array(dtr.predict(input_data_test))




'''
### Time Comparison ##
start_time = time.time()
pred = np.array(dtr.predict(input_data_test))
print("--- %s seconds ---" % (time.time() - start_time))

[start, goal, obs] = obs_make()
start_time = time.time()
for i in range(10):
	T = rrt(start,goal,obs)
print("--- %s seconds ---" % (time.time() - start_time))
'''


### Visualization ###

#Check which test you want to see
T = 0
close = 1
while close == 1:
	checktest = int(input("Enter Test (1-10) you would like to see: "))
	if checktest > 0 and checktest <11:
		checktest = checktest-1
		Predy = np.array(pred[checktest,0:int(pred[checktest][200])])
		Predx = np.array(pred[checktest,100:int(pred[checktest][200])+100])
		Pathy = np.array(output_data_test[checktest,0:int(output_data_test[checktest][200])])
		Pathx = np.array(output_data_test[checktest,100:int(output_data_test[checktest][200])+100])
		Path = np.vstack([Pathx,Pathy]).T
		start = [input_data_test[0][checktest],input_data_test[1][checktest]]
		goal = [[input_data_test[2][checktest],input_data_test[3][checktest],
				input_data_test[4][checktest],input_data_test[5][checktest],
				input_data_test[6][checktest],input_data_test[7][checktest],
				input_data_test[8][checktest],input_data_test[9][checktest]]]
		plot(start,goal,get_obs(),T,Path,Predx,Predy, basic = False,
				Show_Unused_Path=False,Show_First_Path=True,Optimize_Pred=True)
		close = int(input("Would you like to see another test? (1 = yes, any = no)\n"))
