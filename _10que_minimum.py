a=[1,3,67,89,904,4,6,8,12,0]
i=0
min=a[i]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
print(min)