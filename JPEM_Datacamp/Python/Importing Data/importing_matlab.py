import scipy.io
filename = 'C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/ja_data2.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))
print(type(mat['x']))