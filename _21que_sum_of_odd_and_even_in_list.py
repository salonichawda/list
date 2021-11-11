elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
count_odd=0
count_even=0
count_odd=0
while i<len(elements):
    if elements[i]%2==0:
        even+=1
        count_even+=elements[i]
    else:
        odd+=1
        count_odd+=elements[i]
    i+=1
print(even,"total even number of list")
print(odd,"total odd number of list")
print(count_even,"total sum of even numbers")
print(count_odd,"total sum of odd numbers")