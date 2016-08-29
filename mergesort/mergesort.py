# Jared Raby 2016
# Mergesort Implementation in Python
# Reading in an array and sorting it

import math

def mergesort(array):
    n = len(array)
    newArray = []
    
    y = 1
    while ( y < n):
        i = 0
        newArray = []
        while ( i < n):
            merge(array, i, min(i + y, n), min(i + 2*y, n), newArray) 
            i = i + 2 * y
        y =  y * 2

        array = newArray

    print array

def merge(array, leftIndex, rightIndex, endPoint, newArray):

    i = leftIndex
    j = rightIndex

    k = leftIndex
    while (k < endPoint):
        # Declare working variables to perform the switch if the values are different
        if i < rightIndex and ( j >= endPoint or array[i] <= array[j] ):
            newArray.append(array[i])
            i = i + 1
        else: 
            newArray.append(array[j])
            j = j + 1

        k = k + 1
    
def main():

    mergesort([1,8,2,4,5,9,3,6,1,8,7])


if __name__=="__main__":
    main()
