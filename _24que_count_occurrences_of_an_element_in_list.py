# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# list1=[]
# a=[]
# while i<len(char_list):
#     j=0
#     count=0
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count+=1
#         j+=1
#     if char_list[i] in list1:
#         i+=1
#         continue 
#     list1.append(char_list[i])
#     print([char_list[i],count],end=" ")

#     print(char_list[i],"-",count)



char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
list1=[]
while i<len(char_list):
    j=0
    a=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count+=1
        j+=1
    a.append(char_list[i])
    a.append(count)
    if a not in list1:
       list1.append(a)
    i=i+1
print(list1)
    

