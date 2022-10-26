n=int(input())
sum=""
if n<0:
    n=n+(-n)+(-n)
    while n>0:
        r=n%10
        n=n//10
        sum=sum+str(r)
    print(-int(sum))
else:
    while n>0:
        r=n%10
        n=n//10
        sum=sum+str(r)
    print(int(sum))
