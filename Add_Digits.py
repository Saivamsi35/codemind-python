n=int(input())
sum=0
s1=0
s2=0
while n>0:
    r=n%10
    n=n//10
    sum=sum+r
while sum>0:
    r1=sum%10
    sum=sum//10
    s1+=r1
if len(str(s1))==1:
    print(s1)
elif len(str(s1))>=2:
    while s1>0:
        r2=s1%10
        s1=s1//10
        s2+=r2
    print(s2)