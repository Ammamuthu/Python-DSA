# In a list of array [ , , , , , ,]  we declare one min value as 1 array 
# After that we compare the 1st min value with next value to end of list
# After that we gave the min value index to stored min variable 
# Then we swap that to the value we pick as i iteration


arr = [6,1,2,8,3,9]

print(len(arr))                                 #One Iteraton

for i in range(len(arr)-1):                     #6,1,2,8,3   -- > for these many count it Will run
    min=i                                       #min=0
    
    for j in range(min+1,len(arr)):             #(  j=1 , 1 to 9)
        # print(arr[min],">"arr[j])
        if arr[min] > arr[j]:                   #[6] > [1]   yes - >again run last min is arr[1]
            min=j                               #min=1
    arr[min],arr[i]=arr[i],arr[min]             #[1][6]=[6][1]
print(arr)


# [6, 1, 2, 8, 3, 9]

# [1, 6, 2, 8, 3, 9]

#   i  min
#  [6, 1, 2, 8, 3, 9]    # Compare with 1
#  [6, 1, 2, 8, 3, 9]    # Compare with 2
#  [6, 1, 2, 8, 3, 9]    # Compare with 8
#  [6, 1, 2, 8, 3, 9]    # Compare with 3
#  [6, 1, 2, 8, 3, 9]    # Compare with 9

# [1, 2, 6, 8, 3, 9]

