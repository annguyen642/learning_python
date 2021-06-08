#!/usr/bin/env python3

#Numpy is a Python library that can be use to contruct different dimension arrays, and matrixes
#Make sure to install Numpy in terminal
#When doing operations with numpy DO NOT name file "numpy.py" "as the "import numpy as np" would not work as it would import an empty file will import itself resulting in an error 
#pip install numpy and matplotlib onto terminal 

#Import the numpy libray and the numpy library can be define as np 
import math 
import numpy as np
import random 

# The elements within the array are indexed [] as a tuple ()
#The dimension of teh array depends on the axe/ the number of indexes
#The lenght of numbers is in the first set of list while the set the number of columns was the next sets of lists
#the list in the array have to be the same length or there will be an error 
a = np.array([12,9,4,16])
print(a)
print('dimension:',a.ndim,'array shape:',a.shape)
#Math functions can be done on items in the array and printed out as a list 
print('max:',a.max(),'min:',a.min(),'sum:',a.sum(),'mean:', a.mean(), 'st dev:',a.std())

#Math functions can be done to each item in the array
print(a/3)
print('array a divided by 3') 

print(np.sqrt(a))
print('sqrt of array a')

print(a**2)
print('st dev of arrray a')

#the dimension of the array depends on the number of rows. ex. add another set of brackets to create a 2D array
#And print the array along with the dimension and shape
b = np.array([[4,5,6,7],[10,14,16,18]])
print(b)
print('dimension:',b.ndim, 'shape:',b.shape)

#The shape of the matrx can be reverse, but the shape have the same numbers as either the row or column
#Rows and columns cannot be added or substracted with the 'reshape' command, shapes have to be the same value
b_reverse= b.reshape(4,2)
print(b_reverse)
print('revese shape of b')
#A random matrix can be generated with a given size the range of numbers
c=np.random.randint(1,15, size=[3,4])
print(c)
print('randomly generated 3X4 aray')


#A diganogal array can be created with the numbers in the list being in the diagonal 
diagonal=np.diag(np.array([6,8,10,12]))
print(diagonal)
print('diagonal array')

#-------------------------------Operations on Numpy--------------------------------------------------#
#Basic math operations such as addition are applied to arrays meaning that you can do math operations in each element of an array
# if  array_1=[a,b,c,d] and array_2=[e,f,g,h]
# then array_1 + array_2 = [a+e,b+f,c+g,d+h]
#Additon, substraction, multiplocation, divison of array to each other only works if arrays are the same size
# change the operation (substraction, divison, multiplication) on the math variable to apply other math operations on arrays to each other 
e= np.array([4,6,8,10])
f= np.array([1,2,3,4])
math= e + f
multi= e*f
print(math, 'adding arrays')
print(multi,'multiplying arrays')

#Numpy can be used for scientific computing and calculations
#Inaddition to forming matrixes it can perform function with matrices what are useful tools in linear algebra and Fourier transformation
# A common linear algebra  function that is perforom on arrays is finding the dot product
# Dot product is an alegbraic operation that is the sum of the multiplied product of each corresponding elements of two or more arrays of the same shape and returning a single number
# In vector geometry, the result of the dot product of two arrays( which are the vectors) gives the scalar value (angular regulationship) between two vectors
#A vector is something with a magnitude in direction EX. a 1000kg car moving east is a vector
# example: A=[a1,a2,a3,a4] and B=[b1,b2,b3,b4];  (*)= dot product
#  A dot B = A*B= a1b1 +a2b2 + a3b3 + a4b4
i= np.array([1,4,5,2])
j=np.array([4,5,6,3])
dot_prod= np.dot(j,i) 
print( 'dot product=', dot_prod)






#!/usr/bin/env python3

#Numpy is a Python library that can be use to contruct different dimension arrays, and matrixes
#Make sure to install Numpy in terminal
#When doing operations with numpy DO NOT name file "numpy.py" "as the "import numpy as np" would not work as it would import an empty file will import itself resulting in an error 
#pip install numpy and matplotlib onto terminal 

#Import the numpy libray and the numpy library can be define as np 
import math 
import numpy as np
import random 

# The elements within the array are indexed [] as a tuple ()
#The dimension of teh array depends on the axe/ the number of indexes
#The lenght of numbers is in the first set of list while the set the number of columns was the next sets of lists
#the list in the array have to be the same length or there will be an error 
a = np.array([12,9,4,16])
print(a)
print('dimension:',a.ndim,'array shape:',a.shape)
#Math functions can be done on items in the array and printed out as a list 
print('max:',a.max(),'min:',a.min(),'sum:',a.sum(),'mean:', a.mean(), 'st dev:',a.std())

#Math functions can be done to each item in the array
print(a/3)
print('array a divided by 3') 

print(np.sqrt(a))
print('sqrt of array a')

print(a**2)
print('st dev of arrray a')

#the dimension of the array depends on the number of rows. ex. add another set of brackets to create a 2D array
#And print the array along with the dimension and shape
b = np.array([[4,5,6,7],[10,14,16,18]])
print(b)
print('dimension:',b.ndim, 'shape:',b.shape)

#The shape of the matrx can be reverse, but the shape have the same numbers as either the row or column
#Rows and columns cannot be added or substracted with the 'reshape' command, shapes have to be the same value
b_reverse= b.reshape(4,2)
print(b_reverse)
print('revese shape of b')
#A random matrix can be generated with a given size the range of numbers
c=np.random.randint(1,15, size=[3,4])
print(c)
print('randomly generated 3X4 aray')


#A diganogal array can be created with the numbers in the list being in the diagonal 
diagonal=np.diag(np.array([6,8,10,12]))
print(diagonal)
print('diagonal array')

#-------------------------------Operations on Numpy--------------------------------------------------#
#Basic math operations such as addition are applied to arrays meaning that you can do math operations in each element of an array
# if  array_1=[a,b,c,d] and array_2=[e,f,g,h]
# then array_1 + array_2 = [a+e,b+f,c+g,d+h]
#Additon, substraction, multiplocation, divison of array to each other only works if arrays are the same size
# change the operation (substraction, divison, multiplication) on the math variable to apply other math operations on arrays to each other 
e= np.array([4,6,8,10])
f= np.array([1,2,3,4])
math= e + f
multi= e*f
print(math, 'adding arrays')
print(multi,'multiplying arrays')

#Numpy can be used for scientific computing and calculations
#Inaddition to forming matrixes it can perform function with matrices what are useful tools in linear algebra and Fourier transformation
# A common linear algebra  function that is perforom on arrays is finding the dot product
# Dot product is an alegbraic operation that is the sum of the multiplied product of each corresponding elements of two or more arrays of the same shape and returning a single number
# In vector geometry, the result of the dot product of two arrays( which are the vectors) gives the scalar value (angular regulationship) between two vectors
#A vector is something with a magnitude in direction EX. a 1000kg car moving east is a vector
# example: A=[a1,a2,a3,a4] and B=[b1,b2,b3,b4];  (*)= dot product
#  A dot B = A*B= a1b1 +a2b2 + a3b3 + a4b4
i= np.array([1,4,5,2])
j=np.array([4,5,6,3])
dot_prod= np.dot(j,i) 
print( 'dot product=', dot_prod)
#!/usr/bin/env python3

#Numpy is a Python library that can be use to contruct different dimension arrays, and matrixes
#Make sure to install Numpy in terminal
#When doing operations with numpy DO NOT name file "numpy.py" "as the "import numpy as np" would not work as it would import an empty file will import itself resulting in an error 
#pip install numpy and matplotlib onto terminal 

#Import the numpy libray and the numpy library can be define as np 
import math 
import numpy as np
import random 

# The elements within the array are indexed [] as a tuple ()
#The dimension of teh array depends on the axe/ the number of indexes
#The lenght of numbers is in the first set of list while the set the number of columns was the next sets of lists
#the list in the array have to be the same length or there will be an error 
a = np.array([12,9,4,16])
print(a)
print('dimension:',a.ndim,'array shape:',a.shape)
#Math functions can be done on items in the array and printed out as a list 
print('max:',a.max(),'min:',a.min(),'sum:',a.sum(),'mean:', a.mean(), 'st dev:',a.std())

#Math functions can be done to each item in the array
print(a/3)
print('array a divided by 3') 

print(np.sqrt(a))
print('sqrt of array a')

print(a**2)
print('st dev of arrray a')

#the dimension of the array depends on the number of rows. ex. add another set of brackets to create a 2D array
#And print the array along with the dimension and shape
b = np.array([[4,5,6,7],[10,14,16,18]])
print(b)
print('dimension:',b.ndim, 'shape:',b.shape)

#The shape of the matrx can be reverse, but the shape have the same numbers as either the row or column
#Rows and columns cannot be added or substracted with the 'reshape' command, shapes have to be the same value
b_reverse= b.reshape(4,2)
print(b_reverse)
print('revese shape of b')
#A random matrix can be generated with a given size the range of numbers
c=np.random.randint(1,15, size=[3,4])
print(c)
print('randomly generated 3X4 aray')


#A diganogal array can be created with the numbers in the list being in the diagonal 
diagonal=np.diag(np.array([6,8,10,12]))
print(diagonal)
print('diagonal array')

#-------------------------------Operations on Numpy--------------------------------------------------#
#Basic math operations such as addition are applied to arrays meaning that you can do math operations in each element of an array
# if  array_1=[a,b,c,d] and array_2=[e,f,g,h]
# then array_1 + array_2 = [a+e,b+f,c+g,d+h]
#Additon, substraction, multiplocation, divison of array to each other only works if arrays are the same size
# change the operation (substraction, divison, multiplication) on the math variable to apply other math operations on arrays to each other 
e= np.array([4,6,8,10])
f= np.array([1,2,3,4])
math= e + f
multi= e*f
print(math, 'adding arrays')
print(multi,'multiplying arrays')

#Numpy can be used for scientific computing and calculations
#Inaddition to forming matrixes it can perform function with matrices what are useful tools in linear algebra and Fourier transformation
# A common linear algebra  function that is perforom on arrays is finding the dot product
# Dot product is an alegbraic operation that is the sum of the multiplied product of each corresponding elements of two or more arrays of the same shape and returning a single number
# In vector geometry, the result of the dot product of two arrays( which are the vectors) gives the scalar value (angular regulationship) between two vectors
#A vector is something with a magnitude in direction EX. a 1000kg car moving east is a vector
# example: A=[a1,a2,a3,a4] and B=[b1,b2,b3,b4];  (*)= dot product
#  A dot B = A*B= a1b1 +a2b2 + a3b3 + a4b4
i= np.array([1,4,5,2])
j=np.array([4,5,6,3])
dot_prod= np.dot(j,i) 
print( 'dot product=', dot_prod)







