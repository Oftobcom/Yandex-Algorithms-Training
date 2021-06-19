N = int(input())
nums = list(map(int, input().split()))
K = int(input())
keys = list(map(int, input().split()))

d = dict()
for x in keys:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

for key in range(N):
    if d[key+1] > nums[key]:
        print('YES')
    else:
        print('NO')
    
