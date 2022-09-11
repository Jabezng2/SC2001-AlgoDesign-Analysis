import pandas as pd
import random

data = pd.read_csv("exampleClass1DatasetSize1000.csv")
comparisons = 0

def insertionsort(arr):
    if len(arr) < 2:
        return arr

    i = 1
    while i < len(arr): #traverse through array
        global comparisons
        comparisons += 1
        if arr[i] < arr[i-1]: #if the element is smaller than the preceding element
            j = i-1
            while j > 0: #traverse through previous elements to find next smallest
                comparisons += 1
                if arr[i] > arr[j-1]:
                    break
                j -= 1
            temp = arr[i] #store element
            arr[j+1:i+1] = arr[j:i] #shift array right by one position
            arr[j] = temp #perform swap
        i += 1
    return arr

def merge(arr1, arr2):
    global comparisons
    newarr = [] #new array

    while len(arr1) > 0 and len(arr2) > 0: #check that both arrays are not empty
        comparisons += 1
        if arr1[0] <= arr2[0]: #append the bigger first element among the two arrays
            newarr.append(arr1[0])
            arr1.pop(0)
        else:
            newarr.append(arr2[0])
            arr2.pop(0)

    if len(arr1) == 0:
        newarr += arr2 #if first array empty, add second array to the back
    else:
        newarr += arr1 #if second array empty, add first array to the back

    return newarr

def mergesort(arr):
    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        return arr

    leftarr = mergesort(arr[:int(len(arr)/2)])
    rightarr = mergesort(arr[int(len(arr)/2):])
    return merge(leftarr, rightarr)


def hybridsort(arr):
    if len(arr) < 8:
        return insertionsort(arr)
    else:
        leftarr = hybridsort(arr[:int(len(arr)/2)])
        rightarr = hybridsort(arr[int(len(arr)/2):])
        return merge(leftarr, rightarr)

#arr = hybridsort([random.randint(1,1000) for x in range(0,1000000)])


