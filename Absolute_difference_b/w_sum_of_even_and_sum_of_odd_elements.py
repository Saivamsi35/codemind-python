num=int(input())
lst=list(map(int,input().split()))
sum=sum1=0
for i in range(num):
    if lst[i]%2==0:
        sum=sum+lst[i]
    else:
        sum1=sum1+lst[i]
print(abs(sum-sum1))