import numpy as np
filename = 'C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/mnist.txt'
data = np.loadtxt(filename, delimiter=',') 
# use skiprows= to bypass text headers
# use dtype= eg str to enure all entries are imported as strings
data