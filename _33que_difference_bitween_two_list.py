list1 = [1,2,3,4,5,6,7]

list2 = [1,2,3,0,1,6,7]
i=0
a=[]
while i<len(list1):
    if i not in list2:
        a.append(i)
    i+=1
print(a)