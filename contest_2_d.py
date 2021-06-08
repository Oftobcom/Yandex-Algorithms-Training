lst = []
lst = list(map(int, input().split()))

n = len(lst)
k = 0
for i in range(1,n-1):
    if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
        k += 1
print(k)

    
