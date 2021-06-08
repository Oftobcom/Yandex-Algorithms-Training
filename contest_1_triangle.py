def Check(a,b,c):
    if a < b + c:
        return 1
    else:
        return 0

x = int(input())
y = int(input())
z = int(input())

r = Check(x,y,z)
r += Check(y,z,x)
r += Check(z,x,y)

if r == 3:
    print("YES")
else:
    print("NO")
