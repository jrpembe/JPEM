import h5py
import numpy as np

filename = 'C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/L-L1_LOSC_4_V1-1126259446-32.hdf5' 
data = h5py.File(filename, 'r')
print(type(data))

for key in data.keys():
    print(key)
    
for key in data['meta'].keys():
    print(key)
    
print(np.array(data['meta']['Description']), np.array(data['meta']['Detector']))