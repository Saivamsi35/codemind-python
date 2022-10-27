n=int(input())
a=x=0
b=y=1
i=0
print(x,y,end=" ")
while i<(n-2):
    c=a+b
    a=b
    b=c
    i+=1
    print(c,end=" ")