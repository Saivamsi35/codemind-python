n=int(input())
m1=0
while n>0:
    r1=n%10
    n=n//10
    m1=m1+(r1*r1)
    if n==0 and m1>9:
        n=m1
        m1=0
if m1==1 or m1==7:
    print("True")
else:
    print("False")