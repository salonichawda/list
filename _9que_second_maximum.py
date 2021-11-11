number=[4,5,6,8,9,12,34,45,67,90]
i=0
max=number[i]
second_mx=number[i]
while i<len(number):
    if number[i]>max:
       second_mx=max
       max=number[i]
    elif number[i]>second_mx:
        second_mx=number[i]
    i+=1
print(second_mx)








































