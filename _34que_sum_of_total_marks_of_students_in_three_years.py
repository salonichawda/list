marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65, 76],

    [95, 45, 78, 52, 49]

]
i=0
count=0
while i<len(marks):
    a=type(marks[i])
    j=0
    while j<len(marks[i]):
        count+=marks[i][j]
        j+=1
    i+=1
print("total marks is-",count)