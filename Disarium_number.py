n=int(input())
sum=0
n1=n
while n>0:
    r=n%10
    sum+=r**(len(str(n)))
    n=n//10
if n1==sum:
    print("True")
else:
    print("False")