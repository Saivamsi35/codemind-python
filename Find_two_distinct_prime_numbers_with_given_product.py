n=int(input())
count=0
lst=[]
for i in range(2,n):
    if n%i==0:
        lst.append(i)
a=1 #if the num is prime
lst1=[]
for ch in lst:
    for j in range(2,int(ch**0.5)+1):
        if ch%j==0:
            a=2
            break
    if a==1:
        count+=1
        lst1.append(ch)
if count>=2:
    for k in lst1:
        print(k,end=" ")
else:
    print("-1")