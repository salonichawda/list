list=[12,3,4,56,51,70,8,9,13,10]
i=0
even=0
odd=0
# sum=0
while i<len(list):
    if list[i]%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print(even)
print(odd)