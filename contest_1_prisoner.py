def Check(x,y):
    global d,e
    if (x <= d and y <= e) or (y <= d and x <= e):
        return True
    else:
        return False

n = 5
lst = []
for i in range(n): 
    lst.append(int(input()))

a,b,c,d,e = lst
##print(a,b,c)

result = ''
if Check(a,b):
    result = 'YES'
elif Check(a,c):
    result = 'YES'
elif Check(b,c):
    result = 'YES'
else:
    result = 'NO'

print(result)

