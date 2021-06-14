t1 = tuple(map(int, input().split()))
print(t1)

p1 = [num for num in t1 if num >= 0]
lst_max = []
lst_max.append(max(p1))
print(lst_max)

idx1 = p1.index(max1)
##p2 = p1[:idx1] + p1[idx1+1::]
##print(p2)
##max2 = max(p2)
##print(max2)
##
##n1 = [num for num in t1 if num < 0]
##
##min1 = min(n1)
##idx1 = n1.index(min1)
##n2 = n1[:idx1] + n1[idx1+1::]
##print(p2)
##min2 = min(n2)
##print(min2)
##
##print(neg_nos)
