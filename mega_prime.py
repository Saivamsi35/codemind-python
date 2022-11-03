n=int(input())
b=1
for i in range(2,int(n**0.5)+1):
        if n%i==0:
            b=0
            break
c=str(n)
a=1
for ch in c:
    for j in range(2,int(int(ch)**0.5)+1):
        if int(ch)%j==0:
            a=0
            break
if "1" in c:
    print("Not Mega Prime")
elif a==1 and b==1:
    print("Mega Prime")
else:
    print("Not Mega Prime")
    
            
        

        