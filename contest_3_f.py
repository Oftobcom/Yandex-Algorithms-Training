const_A = ord('A')
##print(const_A)

str1 = input()
str2 = input()

##print(str1)
##print(str2)

hash_table = [set() for i in range(26)]

i = 0
x_prev = -1
for c in str2:
    code = ord(c) - const_A
    if i > 0:
        hash_table[x_prev].add(code)
    x_prev = code
    i += 1

count = 0
i = 0
x_prev = -1
for c in str1:
    x = ord(c) - const_A
##    print(c," - ",x)
    if i > 0:
        for code in hash_table[x_prev]:
            if x == code:
                count += 1
##            print(x_prev," -- ",x," -- ",code," | ",count)
    x_prev = x
    i += 1

##print(hash_table)
print(count)
