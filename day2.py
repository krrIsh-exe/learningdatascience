# DAY 2
#Learning  directly by doing challenges

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])
print(arr1)
print(arr2)


print (arr1- arr2 , "substraction")
print (arr1+ arr2 , "addition")
print(arr1*arr2,"multiplication")
print(arr1/arr2,"division")



# here we took inpput in string]

firstinputstring= input( "enter a number")
secondinputstring= input( "enter a number")


# now we will convert it into integer via using loop than we will perform operations on it
#List comprehension inside function call

firstarray= np.array([int(x) for x in firstinputstring.split()])
secondarray=np.array([int(x) for x in secondinputstring.split()]) 


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

