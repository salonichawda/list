magic_square = [

    [8, 3, 4],

    [1, 5, 9],

    [6, 7, 2]

]
i=0
while i<len(magic_square):
    row=0
    count=0
    while row<len(magic_square[i]):
        count+=magic_square[i][row]
        row+=1
    i+=1
    print("row:",count)
j=0
while j<len(magic_square):
    col=0
    count1=0
    while col<len(magic_square[j]):
        count1+=magic_square[j][col]
        col+=1
    j+=1
    print("col:",count1)
diagonal1=magic_square[0][0]+magic_square[1][1]+magic_square[2][2]
diagonal2=magic_square[0][2]+magic_square[1][1]+magic_square[2][0]
if diagonal1==15 and diagonal2==15:
    a=diagonal1+diagonal2
    print("total diagonal is:",a)
    if count==count==diagonal1==diagonal2==15:
        print("it is a diagonal")
    else:
        print("it is a not diagonal")
else:
    ("diagonal are not equal to 15")










magic_square = [

    [8, 3, 4],

    [1, 5, 9],

    [6, 7, 2]

]
i=0
while i<len(magic_square):
    row=0
    count=0
    while row<len(magic_square[i]):
        count+=magic_square[i][row]
        row+=1
    i+=1
    print("row:",count)
col1=magic_square[0][0]+magic_square[1][0]+magic_square[2][0]
col2=magic_square[0][1]+magic_square[1][1]+magic_square[2][1]
col3=magic_square[0][2]+magic_square[1][2]+magic_square[2][2]
count2=col1==col2==col3
print("col:",col1)
print("col:",col2)
print("col:",col3)
diagonal1=magic_square[0][0]+magic_square[1][1]+magic_square[2][2]
diagonal2=magic_square[0][2]+magic_square[1][1]+magic_square[2][0]
if diagonal1==15 and diagonal2==15:
    a=diagonal1+diagonal2
    print("total diagonal is:",a)
    if count==count2==diagonal1==diagonal2==15:
        print("it is a diagonal")
    else:
        print("it is not a diagonal")
else:
    ("diagonal are not equal to 15")