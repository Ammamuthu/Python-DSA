# o(1)
# o(n)
# o( log n)
# o(n log n)
# o(n^2)


# ----------------------------
# o(1) ---> Constant
# Eg -1

print(1)
print(2)
print(3)

# o(n)  --> Linear
L = [1,2,3,4,5]
for i in L:
    print(i)

K = [2,4,5,7,1,0]
a=0
for i in K:
    if a == i:
        print (True)
        break

# o(logn) Logarathmic--> Binary search

#o(NlogN) linear Logarathmic --> Merge Short

# o(n^2) --> Quadratic

# it's just a Linear square   (N*N)

l =[1,2,3,4,5]     #n=5 n2 = 25 this program perform n^2 operation , so it is a Quadratic
for i in l:       # ---n
    for j in l:   # ----n         n2
        print(i,j)


