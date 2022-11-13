n=input()
a=list(map(int,input().split()))
s=0
while True:
    for i,ai in enumerate(a):
        if ai%2==1:
            print(s)
            break
        else:
            a[i]=ai/2
    else:
        s+=1
        continue
    break