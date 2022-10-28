n=int(input())
s=""
for i in range(1,n+1):
    s+=str(i)
    s1=int(s)
print(s1)
while s1>0:
    if s1//10==0:
        break
    print(s1//10)
    s1=s1//10