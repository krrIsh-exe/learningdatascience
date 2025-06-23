''' 
what is numpy ?
numpy is a python library used for working with arrays
it also has functions for working in domain of linear algebra, fourier transform, and matrices
Numpy was created by the travis oliphant in 2005 . it is open source project and you can also use it freely
numpy standsb for numerical python

In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.






'''
import numpy as np

arr= np.array([1,2,3,4,5,6,7,8])
print (arr)
print(type(arr))
# use tuple to create qa array
arrtuple=np.array((1,2,3,4,5,6))
print(arrtuple)


#Learning by diurectly doing challenges

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])
print(arr1)
print(arr2)


print (arr1- arr2 , "substraction")
print (arr1+ arr2 , "addition")
print(arr1*arr2,"multiplication")
print(arr1/arr2,"division")



# here we took inp[ut in string]

firstinputstring= input( "enter a number")
secondinputstring= input( "enter a number")


# now we will convert it into integer via using loop than we will perform operations on it

firstarray= np.array(int(x) for x in firstinputstring.split)
secondarray=np.array(int(x) for x in secondinputstring.split)


print (firstarray-secondarray,"substraction")
print(firstarray/secondarray, "divison")
print(firstarray+secondarray,"addition")
print(firstarray*secondarray,"multiplication")

# remember for this type of operations arrays must be of the same length and numeric
try:
    input1 = input("Enter numbers for the first array (space-separated): ")
    input2 = input("Enter numbers for the second array (space-separated): ")

    array1 = np.array([int(x) for x in input1.split()])
    array2 = np.array([int(x) for x in input2.split()])

    if len(array1) != len(array2):
        print("❌ Arrays must be of the same length.")
    else:
        print("\nFirst Array:", array1)
        print("Second Array:", array2)
        print("Addition:", array1 + array2)
        print("Subtraction:", array1 - array2)
        print("Multiplication:", array1 * array2)
        print("Division:", array1 / array2)

except ValueError:
    print("❌ Invalid input. Please enter numbers only.")