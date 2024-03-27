# In a list it check every time time a list so when it pass through it will add a one current value at end and after that next value 

# List=[6,2,9,2,0,5]

# for i in range(0,len(List)):
#     for j in range(0,len(List)):
#         if List[j] < List[j+1]:
#             List[j],List[j+1]=List[j+1],List[j]
# print(List)



# for i in range(0,len(List)-1):
#     for j in range(0,len(List)-1):
#         print(j,">",j+1) 


List=[6,2,4,3,0,5]

print(type(List[0]))

# This is using if statement

# for i in range(0,len(List)-1):
#     for j in range(0,len(List)-1):
#         if List[j] > List[j+1]:
#             List[j],List[j+1] = List[j+1],List[j]
            
# print(List)

# This is using a while loop -->   Here we did not mention how long we need to run
while True:
    a=True
    for j in range(0,len(List)-1):
        if List[j] > List[j+1]:
            a=False
            List[j],List[j+1] = List[j+1],List[j]

    if (a==True):
        break
    else:
        continue
print(List )



# Each and every time it will currectly add one value at the end ( last two )

# i = 0
# [2, 6, 4, 3, 0, 5]  # j = 0: 6 and 2 are swapped
# [2, 4, 6, 3, 0, 5]  # j = 1: 6 and 4 are swapped
# [2, 4, 3, 6, 0, 5]  # j = 2: No swap
# [2, 4, 3, 0, 6, 5]  # j = 3: 6 and 0 are swapped
# [2, 4, 3, 0, 5, 6]  # j = 4: No swap

# i = 1
# [2, 4, 3, 0, 5, 6]  # No swaps (i = 1, j = 0: No swap)
# [2, 3, 4, 0, 5, 6]  # No swaps (i = 1, j = 1: No swap)
# [2, 3, 0, 4, 5, 6]  # j = 2: 4 and 3 are swapped
# [2, 3, 0, 4, 5, 6]  # No swaps (i = 1, j = 3: No swap)

# i = 2
# [2, 3, 0, 4, 5, 6]  # No swaps (i = 2, j = 0: No swap)
# [2, 0, 3, 4, 5, 6]  # j = 1: 3 and 0 are swapped
# [2, 0, 3, 4, 5, 6]  # No swaps (i = 2, j = 2: No swap)

# i = 3
# [0, 2, 3, 4, 5, 6]  # j = 0: 2 and 0 are swapped
# [0, 2, 3, 4, 5, 6]  # No swaps (i = 3, j = 1: No swap)

# i = 4
# [0, 2, 3, 4, 5, 6]  # No swaps (i = 4, j = 0: No swap)






