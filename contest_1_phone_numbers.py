lst = [ ] 
n = 4  
for i in range(n): 
    lst.append(input().replace('-', '').\
        replace('(', '').replace(')', '').replace('+7', '8')) 

for i in range(n):
    if len(lst[i]) == 7:
        lst[i] = '8495' + lst[i]

for i in range(1,n):
    if lst[0] == lst[i]:
        print('YES')
    else:
        print('NO')
