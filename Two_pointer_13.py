arr=[1,2,3,4,5,6]                                   #0 1 2 3 4 5 

T=11                                        #Traget
l=0                                         #Left pointer in array started as 0
r=len(arr)-1                                #Right Pointer in array of len fun it will give actual count so for aray stated with 0 so -1 is fine 
# print(len(arr))
flag=0                                      #If sum not found

while l < r:                                    #i dont want l pointer croos r pointer and same of both also
    ans = arr[l]+arr[r]                          # ans = 1 + 6 ==> 7
    if ans == T:                                    # no   if yes
        flag=1                                      # I changed a flag as 1 
        print( arr[l] , "+" , arr[r] ,"=" ,ans )                                 # values +ans
        break                                           #stoped the while looop
    elif ans < T:                                       # 7 < 10 we want to increse so
        l=l+1                                           # we move the left point (Note)
    elif ans > T:                                    # if we want 4 ,  7 > 4
        r=r-1                                           # we have to decrease the Right pointer

if flag == 0:                                        #if above flag not changes to 1 means the sum operation not done so there is not found 
        print("The sum value is not found")


# =============================================Diagram=========================================
# arr:  [1, 2, 3, 4, 5, 6]
# T:    11
# l:    0
# r:    5
# flag: 0

#   l
#   ↓
# [1, 2, 3, 4, 5, 6]  # Calculate sum (1 + 6 = 7)
#   ↑
#   r

#    l
#    ↓
# [1, 2, 3, 4, 5, 6]  # Move left pointer
#      ↑
#      r

#     l
#     ↓
# [1, 2, 3, 4, 5, 6]  # Calculate sum (2 + 6 = 8)
#      ↑
#      r

#     l
#     ↓
# [1, 2, 3, 4, 5, 6]  # Move left pointer
#        ↑
#        r

#      l
#      ↓
# [1, 2, 3, 4, 5, 6]  # Calculate sum (3 + 6 = 9)
#        ↑
#        r

#      l
#      ↓
# [1, 2, 3, 4, 5, 6]  # Move left pointer
#          ↑
#          r

#       l
#       ↓
# [1, 2, 3, 4, 5, 6]  # Calculate sum (4 + 6 = 10)
#          ↑
#          r

#       l
#       ↓
# [1, 2, 3, 4, 5, 6]  # Move left pointer
#            ↑
#            r

#        l
#        ↓
# [1, 2, 3, 4, 5, 6]  # Calculate sum (5 + 6 = 11)
#            ↑
#            r

#        l
#        ↓
# [1, 2, 3, 4, 5, 6]  # Sum matches target, update flag
#            ↑
#            r

#        l
#        ↓
# [1, 2, 3, 4, 5, 6]  # Print pair and sum
#            ↑
#            r

