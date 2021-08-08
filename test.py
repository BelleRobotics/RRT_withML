import numpy as np
from init_training import *
import pandas as pd

#Read Test Data
data_test = pd.DataFrame(read_txt(txtname="test"))
input_data_test = data_test.iloc[:,:10]
output_data_test = np.array(data_test.iloc[:,10:])
#print(output_data_test.shape)



Predy = np.array(output_data_test[0,0:int(output_data_test[0][200])])

print(Predy)

np.insert(Predy,0,12)
np.insert(Predy,Predy.shape,12)