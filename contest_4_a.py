N = int(input())
d1 = dict()
d2 = dict()

for i in range(N):
    a, b = input().split()
    d1[a] = b
    d2[b] = a

q = input()
if q in d1:
    print(d1[q])
else:
    print(d2[q])


