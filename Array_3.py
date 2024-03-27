import array

arr = array.array('i',[2,4,7,8,5,2])

print(arr)
# Accessing a Element
print("==================================Accessing==================================")
print(arr[2])
print(arr[4])

for i in range(0,len(arr)):
    print(arr[i] , end="")
print()


#inserting

arr[1]=7
# or
arr.insert(2,8)
print("==================================inserting==================================")
print(arr)


#deleting
arr.pop(0)          #--> It delete that index
# or
arr.pop()           #--> This one will delete a last one default
print("==================================Deleting==================================")
print(arr)


#Searching
print("==================================Searching==================================")
a=5                    #Check this value is present or not
for i in range(0,len(arr)):
    if arr[i] == a :
        print(i)        #--> through the index
        print(True)
        break