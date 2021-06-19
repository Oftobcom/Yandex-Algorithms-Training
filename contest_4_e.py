N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
#print(lst)

d = dict()
for x in lst:
    if x[0] in d:
        d[x[0]].append(x[1])
    else:
        d[x[0]] = [x[1]]

#print(d)

s = 0
for x in d:
    #print(x)
    s += max(d[x])

print(s)
    
