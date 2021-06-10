N = int(input())
set1 = set()

lst1 = []
for i in range(N):
    a, b = tuple(map(int, input().split()))
    if a + b + 1 == N and a >=0 and b >= 0:
        set1.add((a,b))

result = len(set1)
print(result)
