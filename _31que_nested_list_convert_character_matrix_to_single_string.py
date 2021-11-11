name=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
sum=name[i]
while i<len(name):
    if type(name[i])is list:
        j=0
        while j<len(name[i]):
            sum+=[j]
            j+=1
        i+=1
print(sum)