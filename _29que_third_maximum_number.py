# number=[4,5,6,8,9,12,34,45,67,90]
# length=len(number)
# number.sort()
# print(length)
# print("largest value is",number[length-1])
# print("third largest value is",number[length-3])





number=[4,5,6,8,9,12,34,45,67,90]
i=0
max=number[i]
third_mx=number[i]
while i<len(number):
    if number[i]>max:
       third_mx=max
       max=number[i]
       number.remove(max)
    elif number[i]>third_mx:
        third_mx=number[i]
    i+=1
print("third maximum value is",third_mx)

