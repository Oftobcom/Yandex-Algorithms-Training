def Det(x1,y1,x2,y2):
    return x1*y2 - x2*y1

n = 6
lst = []
for i in range(n): 
    lst.append(float(input()))

a,b,c,d,e,f = lst
##print(a,b,c,d,e,f)

d_main = Det(a,b,c,d)
d_1 = Det(e,b,f,d)
d_2 = Det(a,e,c,f)
##print(d_main,d_1,d_2)

result = ''
if d_main != 0:
    x = d_1 / d_main
    y = d_2 / d_main
    result = '2 ' + str(x) + ' ' + str(y)
else:
    if d_1 != 0 and d_2 != 0:
        result = '0'
    else:
        if d_1 == 0 and d_2 == 0:
            if a == 0 and b == 0 and c == 0 and d == 0 and e != f:
                result = '0'
            elif a == 0 and b ==0 and c == 0 and d == 0 and e == f:
                result = '5'
            elif b == 0 and d == 0 and a != 0:
                k = e/a
                result = '3 ' + str(k)
            elif b == 0 and d == 0 and c != 0:
                k = f/c
                result = '3 ' + str(k)
            if a == 0 and c == 0 and b != 0:
                k = e/b
                result = '4 ' + str(k)            
            elif a == 0 and c == 0 and d != 0:
                k = f/d
                result = '4 ' + str(k)            
            elif b != 0:
                k = -a/b
                b = e/b
                result = '1 ' + str(k) + ' ' + str(b)
            elif d != 0:
                k = -c/d
                b = f/d
                result = '1 ' + str(k) + ' ' + str(b)
        elif d_1 != d_2:
            result = '0'
        else:
            result = '5'
            
print(result)
