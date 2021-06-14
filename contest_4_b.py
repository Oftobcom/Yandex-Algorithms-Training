import sys

text = sys.stdin.read()
lst1 = list(text.split())
#print(lst)

lst2 = []
d = dict()
for x in lst1:
    if x in d:
        d[x] += 1
    else:
        d[x] = 0
    lst2.append(d[x])

result = ' '.join([str(elem) for elem in lst2])
print(result)
