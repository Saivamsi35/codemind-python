n=int(input())
m=int(input())
a=n+m+1
while True:
    s=0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            s=1
            break
    if s==0:
        break
    else:
        a+=1
print(a-(n+m))
    