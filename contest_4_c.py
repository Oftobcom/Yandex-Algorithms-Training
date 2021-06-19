import sys

text = sys.stdin.read()
lst1 = list(text.split())
##print(lst1)

max_ = 1
max_key = lst1[0]
d = dict()
for x in lst1:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
    if max_ < d[x]:
        max_ = d[x]
        max_key = x

##print(dict)
##print(max_key)
lst2 = []
for key in d:
    if d[key] == max_:
        lst2.append(key)
lst2.sort()
print(lst2[0])
