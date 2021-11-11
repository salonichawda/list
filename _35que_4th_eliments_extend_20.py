a=[1,2,8,7,6,3,4,8,9,5,10,11,12]
i=4
x=20
while i<len(a):
    a.insert(i,x)
    i+=4+1
print(a)