lst = list(map(int, input().split()))
n = len(lst)

k = 0
for i in range(0,n-1):
    if lst[i] < lst[i+1]:
        k += 1

if k == n-1:
    result = 'YES'
else:
    result = 'NO'

print(result)

