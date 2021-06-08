end = -2*10**9
lst = []
x = int(input())
while x != end:
    lst.append(x)
    x = int(input())

n = len(lst)
k_const = k_asc = k_w_asc = k_desc = k_w_desc = 0

for i in range(0,n-1):
    if lst[i] == lst[i+1]:
        k_const += 1
    if lst[i] < lst[i+1]:
        k_asc += 1
    if lst[i] <= lst[i+1]:
        k_w_asc += 1
    if lst[i] > lst[i+1]:
        k_desc += 1
    if lst[i] >= lst[i+1]:
        k_w_desc += 1

n -= 1            
if n == k_const:
    result = 'CONSTANT'
elif  n == k_asc:
    result = 'ASCENDING'
elif  n == k_w_asc:
    result = 'WEAKLY ASCENDING'
elif  n == k_desc:
    result = 'DESCENDING '
elif  n == k_w_desc:
    result = 'WEAKLY DESCENDING'
else:
    result = 'RANDOM'

print(result)

