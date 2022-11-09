num=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in range(len(lst)):
    if a>lst[i] or b<lst[i]:
        sum=sum+lst[i]
print(sum)