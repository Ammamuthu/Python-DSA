# Space complexicity also has the same as 5 of notaions

# o(1)
# o(N)
# o(logN)
# o(NlogN)
# 0(N^2)
# These two were very very raare
# o(n^3)
# o(2n)

# o(1) ---> Constant Space (Each and every data type has an size so even if i gave 1000 also it remains same size that's o(1))
a=15            #--> bothis same size the value is diferent but size is same
a=100

#o(n)
l=[1,2,3,4,5,6,7]
# we dont know the value of list so that why it's o(n)
k=[1,2,3]               #--> this is smaller value also is o(n)


# case : If a function has both o(1) and o(n)
a=100
b=20
l=[1,2,3,4,5,6,7,8]         #o(1)>>0(n)   == ans o(n)

# this means we have a bigger one 0(n) that one support both buth o(1) is not support for list so always pick the greater one

#o(logN) -->(Recursive and Back tracking concept) Recursion.py

# 0(nLogN) --> We don't use it anywhere 

# O(n^2) --> Quadratic space (Matrix)

l= [[1,2,3],
    [4,5,6],
    [7,8,9,]        #This is o(n^2)  n coloumn should match n row 3x3 ,4x4 .. NxN 
    ]

# =====================================================================

# Auxilary Space

l= [1,2,3,4,5,1] # we need to add a unique value in another list   --> o(n)

k=[]
for i in l:
    if i not in k:              #--> o(n) 
        k.append(i)
print(k)

# Note : List is 0(n) and the logic is also o(n) so both is called o(n)


# Another Eg:  we have to print the value till the variable value
l=10            #--> o(1) input value is o(1)

k=[]            #--o(n) auxilary space is o(n)
for i in range(1,l+1):
    k.append(i)
print(k)

# When we pick logic it's auxillary space 
# ===========================================Time complexity=================================================================

# Theory

# order

# o(1)            ---------> Best (Because it's only constent that why wjat we give that wil be result o(10,100,1000))
# o(logN)       -->(log input(value))
# o(N)          -->(input value)
# o(NlogN)      -->o(n=linear log n=Logarthmic) linear x logarthmic
# o(n^2)        --> o(input value *2)
# o(n^3)        --> o(input value *3)
# o(2^n)          -------->Worst


# When we decrease the runtime we increase the code effceincy this is the order of the code 
# This is called Time complexity

# ===========================================Space complexity=================================================================

# same as time order

# o(1)            ---------> Best (Because it's only constent that why wjat we give that wil be result o(10,100,1000))
# o(logN)       -->(log input(value))
# o(N)          -->(input value)
# o(NlogN)      -->o(n=linear log n=Logarthmic) linear x logarthmic
# o(n^2)        --> o(input value *2)
# o(n^3)        --> o(input value *3)
# o(2^n)          -------->Worst
