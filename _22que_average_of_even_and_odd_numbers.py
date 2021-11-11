elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
count_even=0
count_odd=0
while i<len(elements):
    if elements[i]%2==0:
        even+=1
        count_even+=elements[i]
        avg_even=count_even/even
    else:
        odd+=1
        count_odd+=elements[i]
        avg_odd=count_odd/odd
    i+=1
print(even,"total even number in list")
print(odd,"total odd number in list")
print(count_even,"sum of even numbers")
print(count_odd,"sum of odd numbers")
print(avg_even," average of even numbers")
print(avg_odd,"average of odd numbers")