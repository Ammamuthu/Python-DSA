list = [63,7,74,5,2,76,2,75]

usr = int( input("Enter the array in the list you want to find "))

# print(len(list))


for i in range(0,len(list)):
    if list[i] == usr:
        print( " You value present in : ",i)
        break
else:
    print(f"This Value {usr} not there" )



# ===================================================================
# yOu should un cmd and run this file  to see the output 
    # for i in range(0,len(list)):
    # if list[i] == usr:
    #     print( " You value present in : ",i)
    #     break
    # else:
    #     print(f"This Value {usr} not there" )