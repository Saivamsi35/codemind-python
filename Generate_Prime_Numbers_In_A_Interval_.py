n=int(input())
m=int(input())
i=n
while i<=m:
    prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            prime=False
            break
    if prime==True and i!=1:
        print(i)
    i+=1
