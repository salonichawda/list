# num=int(input("enter the number"))
# i=1
# while i==1:
#     num=int(input("enter the number"))
#     if num%2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")
#     i+=1



# list1=[1,2,3,4,5,6,7,8,9]
# i=0
# a=[]
# b=[]
# sum=0
# sum1=0
# even=0
# odd=0
# while i<len(list1):
#     if list1[i]%2==0:
#         a.append(list1[i])
#         sum+=list1[i]
#         even+=1
#     else:
#         b.append(list1[i])
#         sum1+=list1[i]
#         odd+=1
#     i+=1
# print(a,"=",sum,"count-",even)
# print(b,"=",sum1,"count-",odd)



name=input("enter the name-:")
i=0
count=0
count1=0
while i<len(name):
    if name[i]=="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u":
        count+=1
    else:
        count1+=1
    i+=1
print(count,"vovales")
print(count1,"consonents")