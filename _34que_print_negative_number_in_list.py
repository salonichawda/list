list=[1,-2,3,-4,5,-6,7,-8,9,-10]
i=0
list1=[]
while i<len(list):
    if list[i]<0:
       list1.append(list[i])
    i+=1
print(list1)