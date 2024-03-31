# Quick sort is nothing but we have to pick a random/center/first/last any element that value called as pivot
# Based on that you could be sperate a value like > greater then the pivot and < lesser then the pivot we will spill
# question = [7,2,6,1,3,8]   pivot = 6(randomly)  ==> differentiacte   < pivot (6) left = [2,1,3]  > pivot (6) right = [7,8]
# left =[2,1,3] pivot=[6] right =[7,8] ,Middle=[Pivot values]
# Now based on that we have to make a pivot for both left and right also same random wise
# pivot =[1]  < no value , > 3 2 
# pivot=[8]   < 7 , > no

# this loop repaeat aftrer the end it will sorted 

import random
def quicksort(arr):

    if len (arr)<=1:
        return arr
    
    pivot=random.choice(arr)
    
    Left=[]
    for i in arr:
        if i<pivot:
            Left.append(i)
    Right=[]
    for i in arr:
        if i>pivot:
            Right.append(i)
    middle=[]
    for i in arr:
        if i == pivot:
            middle.append(i)


    return quicksort(Left) + middle +  quicksort(Right)

arr = [7,1,4,2,9,5]
print("Before =",arr)
print("After = ",quicksort(arr))

# =====================================================

# other step 

import random
def quicksort(arr):

    if len (arr)<=1:
        return arr
    
    pivot=arr[len(arr)//2]      #-->use middle value's
    
   
    Left=[i for i in arr if i < pivot]
    Right=[i for i in arr if i > pivot ]
    middle=[i for i in arr if i == pivot ]

    return quicksort(Left) + middle +  quicksort(Right)

arr = [7,1,4,2,9,5]
print("Before =",arr)
print("After = ",quicksort(arr))


# Content in Visuvalize

# Initial Array: [7, 1, 4, 2, 9, 5]

# Pick Pivot: 7

# Partition:
# [1, 4, 2, 5]   [7]   [9]

# Recursively Sort Left and Right Subarrays:
# Left Subarray: [1, 4, 2, 5]
# Right Subarray: [9]

#     Pick Pivot: 1

#     Partition:
#     []   [1]   [4, 2, 5]

#     Left Subarray: []
#     Middle Subarray: [1]
#     Right Subarray: [4, 2, 5]

#     Sorted Right Subarray: [2, 4, 5]

# Concatenate Sorted Subarrays: [] [1] [2, 4, 5] => [1, 2, 4, 5]

# Sorted Right Subarray: [9]

# Concatenate Sorted Subarrays: [1, 2, 4, 5] [7] [9] => [1, 2, 4, 5, 7, 9]

# Final Sorted Array: [1, 2, 4, 5, 7, 9]
