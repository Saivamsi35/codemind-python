N=int(input())
lst=list(map(int,input().split()))
for i in range(N,0,-1):
    if lst[i-1]%2==0:
        print(i-1)
        break