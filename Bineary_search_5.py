source = [1, 3, 5, 7, 9, 11, 13, 15, 17]

Target=7

# Pretend that you dont know the value and size of an array only know the varaiable/array name

print(len(source)) #---> It will give you the count of an value but we need index

l=0
r=len(source)-1

while l<=r:
    M=(l+r)//2
    if Target == source[M]:
        print(M)
        break     #--> With out break it's multiple time print 7
    elif source[M]>Target:
        r=M-1
    elif source[M]<Target:
        l=M+1
else:
    print("Nope.")

#tHEory part
# Original Array: [1, 3, 5, 7, 9, 11, 13, 15, 17]

# Step 1:
# | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
# ^                        ^
# |                        |
# |             R          L
# |                        Target (12)

# Step 2:
# | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
# ^                ^
# |                |
# |       R        L
# |                Target (6)

# Step 3:
# | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
# ^        ^
# |        |
# |  R     L
# |        Target (5)

# Step 4:
# | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
# ^  ^
# |  |
# |R  L
# |  Target (2)

# Step 5:
# | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
# ^  ^
# |  |
# RL
# |  Target (1)

# Target found at position 0.
