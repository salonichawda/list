list=[1,2,2,5,8,4,4,8]
i=0
a=[]
for i in list:
    if i not in a:
        a.append(i)
        count=len(a)
    i+=1
print("count=",count)
print("unique values=",a)
