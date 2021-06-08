n = int(input())
t1 = tuple(map(int, input().split()))
#print(n)
#print(t1)

win_max = max(t1)
win_idx = t1.index(win_max)
print("win_max",win_max)
print("win_idx",win_idx)

lst = []
i = 0
for x in t1:
    if (i-1) > win_idx:
        if x_prev%5 == 0 and x_prev%2 == 1 and x < x_prev:
            lst.append(i-1)
    x_prev = x
    i += 1

print("lst",lst)

if len(lst) == 0:
    result = 0
else:
    distanceVasya = t1[lst[0]]
    for i in lst[1::]:
        x = t1[i]
        if distanceVasya < x:
            distanceVasya = x

##    lst4 = t1.copy()
##    lst4.sort(reverse=True)

    place = 0
    for x in t1:
        if x > distanceVasya:
            place += 1
##        else:
##            break
    result = place + 1

print(result)
