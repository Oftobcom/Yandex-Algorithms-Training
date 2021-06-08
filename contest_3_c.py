def my_print(x):
    lst = sorted(list(x))
    print(len(lst))
    result = ' '.join([str(elem) for elem in lst])
    print(result)
    
N, M = list(map(int, input().split()))
##print(N,M)

lst1 = []
for i in range(N): 
    lst1.append(int(input()))

lst2 = []
for i in range(M): 
    lst2.append(int(input()))

set1 = set(lst1)
set2 = set(lst2)
##print(set1)
##print(set2)

set_x = set1 & set2
my_print(set_x)

set1_only = set1.difference(set_x)
my_print(set1_only)

set2_only = set2.difference(set_x)
my_print(set2_only)
