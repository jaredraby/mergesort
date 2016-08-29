# Jared Raby 2016
# Mergesort Implementation in Python
# Reading in an array and sorting it

import math
import random
import timeit

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

arr1 = None
arr2 = None
def setup(high):
    global arr1
    global arr2
    arr1 = [random.randint(0, high) for _ in xrange(high)]
    arr2 = [random.randint(0, high) for _ in xrange(high)]

def test1():
    return mergesort(arr1)

def test2():
    return arr2.sort()


def main():

    for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        #print 'Elements: ', i
        setup(i)
        print 'Mergesort: %s' % timeit.timeit(test1, number=1)
        print 'Built in: %s' % timeit.timeit(test2, number=1)
        print ''

if __name__=="__main__":
    main()
        

