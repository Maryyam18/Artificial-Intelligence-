import numpy as np


###array of 10 zeros
array1=np.zeros(10)
print(array1)

###array of 10 ones
array2=np.ones(10)
print(array2)

###array of 10 fives
array3=np.ones(10)
array3=array3*5
print(array3)

###array of integers 10 to 50
array4=np.arange(10,51)
print(array4)

###array of all even integers from 10 to 50
array5=np.arange(10,51,2)
print(array5)

#### Create a 3x3 matrix with values ranging from 0 to 8
array6=np.arange(0,9).reshape(3,3)
print(array6)


#### Create a 3x3 identity matrix
array7=np.identity(3)
print(array7)

#### Use NumPy to generate a random number between 0 and 1
import random
array8=np.random.uniform(0,1)
print(array8)

#### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
array9=np.std((0,25))
print(array9)


#### Create the following matrix:
array10=np.linspace(0.01,1,100).reshape(10,10)
print(array10)


#### Create an array of 20 linearly spaced points between 0 and 1:
array11=np.linspace(0,1,20)
print(array11)



#####
array11=np.arange(1,26).reshape(5,5)
print(array11)

aray14=np.array([[[2],[7],[12]]])
aray14.hstack()
print(aray14)