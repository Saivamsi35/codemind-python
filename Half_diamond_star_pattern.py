n=int(input())
n1=n-1
if n>2 and n<101:
    for i in range(1,n+1):
        print(i*"*")
    for j in range(n1,0,-1):
        print(j*"*")
else:
    print("The pattern is not possible")