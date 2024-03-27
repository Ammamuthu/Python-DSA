for i in range(0,len(List)-1):
    for j in range(0,len(List)-1):
        if List[j] > List[j+1]:
            List[j],List[j+1] = List[j+1],List[j]
            
print(List)