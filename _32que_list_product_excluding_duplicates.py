list=[6,1,3,5,6,3,1]
b=1
i=0
list1=[]
while i<len(list):
    j=1+i
    while j<len(list):
        if list[i]==list[j]:
            list1.append(list[i])
            del(list[j])
            b*=list1[i]
        j+=1
    i+=1
print(list1)
print(b)






