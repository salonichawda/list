number=[4,5,6,8,9,12,90,34,45,67,]
i=0
max=number[i]
while i<len(number):
    if number[i]>max:
      max=number[i]
    i+=1
print(max)