t=int(input())
for i in range(t):
    n=int(input())
    a=n
    while True:
        y=1
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                y=2
                break
        if y==1:
            break
        else:
            a=a-1
    b=n
    while True:
        x=1
        for i in range(2,int(b**0.5)+1):
            if b%i==0:
                x=2
                break
        if x==1:
            break
        else:
            b=b+1
    if (n-a)>(b-n):
        print(b)
    else:
        print(a)