list1=[12,45,6,7,9,10,23,13,5,4]
i=0
sum=0
while i<len(list1):
    sum=sum+list1[i]
    avg=sum/len(list1)
    i+=1
print(sum)
print(avg)