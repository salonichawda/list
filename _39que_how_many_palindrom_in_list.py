list=["saloni","mom","nayan"]
i=0
a=[]
sum=0
sum1=0
while i<len(list):
    length=len(list[i])-1
    j=length
    while j>0:
        a.append(list[i])
        j-=1
    if list[i]==a[i]:
        sum+=1
    else:
        sum1+=1        
    i+=1
print(sum,"palindrom")
print(sum1,"not palindrom")