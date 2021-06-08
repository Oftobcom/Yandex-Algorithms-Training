digits = set(map(int, input().split()))
str1 = input()
set1 = set([int(d) for d in str1])

##print(digits)
##print(set1)

set_diff = set1.difference(digits)
print(len(set_diff))
