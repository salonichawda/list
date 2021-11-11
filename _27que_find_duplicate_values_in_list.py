n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
a=[]
i=0
while i<len(n): 
    j=0  
    count=0
    while j<len(n):
        if n[i]==n[j]:
            count+=1
        j+=1
    if n[i] in a:
        i+=1
        continue
    a.append(n[i])
    print(n[i],"=",count) 
print(a)