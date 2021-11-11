binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
i=0
d=0
a=len(binary_number)-1
while i<len(binary_number):
    d+=binary_number[i]*2**a
    i+=1
    a=a-1
print(d)



