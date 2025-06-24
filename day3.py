# DAY 3

import numpy as np

arr1s= np.ones([8])  # it will create 1 dimensional array of 8 ones
arr2s= np.zeros([4,5]) # it will create 2 dimensional array of 4 rows and 5 columns with all zeros

print(arr1s)
print(arr2s)


# arrange

arrarrange= np.arange(1,10)
print(arrarrange)

arrarrangestepwise=np.arange(1,10,2) # in the end we wrote 2 hence it goes by 2 steps
print(arrarrangestepwise)

# Reshaping array  1d to 2d

arrayr1=np.arange(1,7)
print(arrayr1)
arrayr1=np.reshape(arrayr1,(2,3))
print(arrayr1)

# flatten array  means we are converting multidimensional array to 1d array back to 1d array
# we can use flatten() or ravel() function to do this

array2d= np.ones([3,3])
print(array2d)
flatarray= array2d.flatten()
print(flatarray)

# 3 linspace() generates evenly spaced values

linearsarray = np.linspace(0,1,5) # it will give 5 evenly spaced values
print(linearsarray)


matrix = np.random.randint(10,100, size= (3,3))
print("this is 3*3 matrix")
print (matrix)

print("Mean"  , matrix.mean())
print("median", matrix.max())
print("median" ,matrix.min())

print ("elements >60:")
print(matrix[matrix>60])