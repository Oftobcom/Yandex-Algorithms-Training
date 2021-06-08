n = 3
lst = []
for i in range(n): 
    lst.append(int(input()))

a,b,c = lst
##print(a,b,c)

if  c < 0:
    result = 'NO SOLUTION'
elif  a == 0:
    if b == c*c:
        result = 'MANY SOLUTIONS'
    else:
        result = 'NO SOLUTION'
else:
    x1 = (c*c - b)//a
    x2 = (c*c - b)/a
    if x1 == x2:
        result = x1
    else:
        result = 'NO SOLUTION'

print(result)

