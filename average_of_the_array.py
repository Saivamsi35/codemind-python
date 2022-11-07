#Find integer avg of the given array
N=int(input())
lst=list(map(int,input().split()))
sum=0
for i in lst:
    sum=sum+i
avg=sum/N
print('{:.2f}'.format(avg))