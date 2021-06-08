input()
lst = []
lst = list(map(int, input().split()))
k = int(input())

print(lst)
print(k)

n = len(lst)
idx = 0
dist = abs(k - lst[0])
for i in range(1,n):
    x = abs(k - lst[i])
    if dist > x:
        dist = x
        idx = i
print(lst[idx])

    
