n=int(input())
v=n*n
sum=0
while v>0:
    r=v%10
    sum+=r
    v=v//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")