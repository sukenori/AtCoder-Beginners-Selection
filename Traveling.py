n=int(input())
tx=[input() for _ in range(n)]
ext=0
exx=0
exy=0
for i in range(n):
    t,x,y=map(int,tx[i].split())
    if not(t-ext>=abs(x-exx)+abs(y-exy) and (t-ext-(abs(x-exx)+abs(y-exy)))%2==0):
        print("No")
        break
    ext=t
    exx=x
    exy=y
else:
    print("Yes")