a=[1,3,67,89,904,4,6,8,12,0]
i=0
min=a[i]
sec_min=a[i]
while i<len(a):
    if a[i]<min:
        sec_min=min
        min=a[i]
    elif a[i]<sec_min:
        sec_min=a[i]
    i=i+1
print(sec_min)