name=[ 'n', 'i', 't', 'i', 'n' ]
list1=[]
length=len(name)
i=length-1
while i>=0:
    list1.append(name[i])
    if list1==name:
        print(list1,"is palindrome")
    else:
        print(list1,"not palindrome")
    i-=1