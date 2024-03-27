n=5
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)          
print(fact(n))      #--> Here were returning n not return 1 so it will give n stored latest value 





# fact(5) * 4 = 20
# fact(4) * 3 = 60
# fact(3) * 2 = 120
# fact(2) * 1 = 120


# This is old one 

# x= int(input("entr the number hat you whant bto factorial :"))
# def factorial(x):
#     if x==0:
#         return 1
#     return x*factorial(x-1)
# sum=factorial(x)
# print(sum)