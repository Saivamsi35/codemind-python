#Find integer avg of the given array is presented as
#the list elements or not
N=int(input())
lst=list(map(int,input().split()))
sum=0
for i in lst:
    sum=sum+i
avg=sum//N
if avg in lst:
    print("True")
else:
    print('False')