a=int(input())
b=int(input())
c=int(input())
x=int(input())
n=0
for ia in range(a+1):
    for ib in range(b+1):
        for ic in range(c+1):
            if 500*ia+100*ib+50*ic==x:
                n+=1
print(n)