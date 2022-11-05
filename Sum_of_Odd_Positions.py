num=int(input())
lst=list(map(int,input().split()))
sum=0
for i in range(num):
    if (i)%2!=0:
        sum=sum+lst[i] 
print(sum)