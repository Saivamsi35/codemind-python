n=int(input())
a=""
b=str(n)
while n>0:
    r=n%10
    a+=str(r)
    n=n//10
if b==a:
    print("True")
else:
    print("False")