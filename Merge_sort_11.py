def merge_sort(arr):

    #spliting
    if len(arr)>1:
        min = len(arr)//2
        left = arr[:min]
        right= arr[min:]

        merge_sort(left)
        merge_sort(right)
    #sorting

        lp=0
        rp=0
        fp=0

        while lp<len(left) and rp<len(right):
            if left[lp] < right[rp]:
                arr[fp]=left[lp]
                lp=lp+1
            else:
                arr[fp]=right[rp]
                rp=rp+1
            fp = fp+1
    #merging                    --> this process is when left array complete first with value we need to merge right with it beacuse the loop we give above is and condition tht's why
                                        #for the same as right if the end is completed with left there is no iteration for left means we need to add all the right value inside a arr beacuse it's already sorted 
        while lp < len(left):           # if above array left = [2,3,4]  right=[compled] means rp=3 ,lp=0 0r 1 , so  
            arr[fp] = left[lp]          #lp < len(left)   means 1<2
            fp=fp+1                    # now we're adding that in fp = [rp values] ==> fp = [0,1,] = left[lp] [2,3,4]
            lp=lp+1

        while rp < len(right):
            arr[fp] = right[rp]
            fp=fp+1
            rp=rp+1

arr=[5,2,8,1,9]
print(arr)

merge_sort(arr)
print(arr)




# Diagram of merge and sorting concept

# left:  [2, 4, 6]
# right: [1, 3, 5]
# arr:   []
# lp: 0, rp: 0, fp: 0


# # Compare elements at lp and rp
# 2 < 1? No
# arr:   [1]          # Place smaller element (1) in arr
# lp: 0, rp: 0, fp: 1

# # Increment rp
# lp: 0, rp: 1, fp: 1

# # Compare elements at lp and rp
# 2 < 3? Yes
# arr:   [1, 2]       # Place smaller element (2) in arr
# lp: 0, rp: 1, fp: 2

# # Increment lp
# lp: 1, rp: 1, fp: 2

# # Compare elements at lp and rp
# 4 < 3? No
# arr:   [1, 2, 3]    # Place smaller element (3) in arr
# lp: 1, rp: 1, fp: 3

# # Increment rp
# lp: 1, rp: 2, fp: 3

# # Compare elements at lp and rp
# 4 < 5? Yes
# arr:   [1, 2, 3, 4] # Place smaller element (4) in arr
# lp: 1, rp: 2, fp: 4

# # Increment lp
# lp: 2, rp: 2, fp: 4

# # Compare elements at lp and rp
# 6 < 5? No
# arr:   [1, 2, 3, 4, 5]  # Place smaller element (5) in arr
# lp: 2, rp: 2, fp: 5

# # Increment rp
# lp: 2, rp: 3, fp: 5

# here the last step of merging will come 



# # Compare elements at lp and rp
# 6 < N/A? No
# arr:   [1, 2, 3, 4, 5, 6]   # Place smaller element (6) in arr
# lp: 2, rp: 3, fp: 6



# Both subarrays are fully merged
# left =[5,9] right=[3,6,7]
#  right len is 3


# 5<3  
# rp+1                1
# arr=[3]
# 5<6 
# lp+1                                    1
# arr=[3,5]
# 9<6  6
# rp+1                2
# 9<7  7
# rp+1                3
# arr=[3,5,6,7]

# rp reaches also 3 =3


# now rp reached = len(right) so nothing to compare with rp [right ] but still there is a value on left(sorted also) so ,

# while rp<len(right) : our scenario is 3=3 it wont go this loop (we have values in left array)

# while lp < len(left) : lp=1 for us (still one value is pending soooo)
# our final added arr is arr=[3,5,6,7]

# arr[fp] =left
# increase lp ++
# fp++

# if we have more values in left or right array
