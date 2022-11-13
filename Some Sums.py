n,a,b=map(int,input().split())
s=0
for i4 in range(10):
    for i3 in range(10):
        for i2 in range(10):
            for i1 in range(10):
                if i4*1000+i3*100+i2*10+i1<=n:
                    if i4+i3+i2+i1>=a and i4+i3+i2+i1<=b:
                       s+=i4*1000+i3*100+i2*10+i1
if a==1 and n==10000:
    s+=10000
print(s)