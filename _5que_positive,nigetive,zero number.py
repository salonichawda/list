list=[4,-6,76,8,90,-98,75,-3,13,-23,12,2,24,-45,65,5,-91,80,8,0]
i=0
positive=0
negative=0
zero=0
while i<len(list):
    if list[i]>0:
        positive+=1
    elif list[i]<0:
        negative+=1
    else:
        zero+=1
    i+=1
print(positive)
print(negative)
print(zero)

# a="12hourses"
# print(str(12*2)+"hourses")