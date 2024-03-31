# Concept
# ther could be a list of array values [,7,1,5,4,3,2]
# we have to split a array in 2 form Sorted unsorted
# we take a first value as soted array and stor it in a variable
# rest of the value will be unsorted array
# 7-sorted array (Instead of storing ina separate array we will store this under variable) [1,5,4,3,2]-->unsorted array 

# 7 --> SA , 1,5,4,3,2 --> unsorted

# we have to store a 1 index as SA and rst of the all are non Sorted  then pick the first value from the Un sorted
# then compare with sorted store there

# if UNsorted value is smaller then >> sorted store the value you compare with and move the old current value with un sorted postion 


arr=[7,1,5,4,3,2]               #(1) iteration

for i in range (1,len(arr)):   #1,5,4,3,2
    curr = arr[i]              #curr=1
    j=i-1                      #j=[0] index
    while j>=0 and curr<arr[j]: #j>=0 yes always and curr[7]<[1] yes
        arr[j+1]=arr[j]         #[7,1,5,4,3,2] -- > [7,7,5,4,3,2]
        j=j-1                   #j=5 --> j=1
    arr[j+1]=curr               #[1,7,5,4,3,2]
print(arr)
    

    



