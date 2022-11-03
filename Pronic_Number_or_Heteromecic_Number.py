n=int(input())
m=int(n**0.5)
for i in range(1,m+1):
    mul=i*(i+1)
    if mul==n:
        print("YES")
        break
else:
    print("NO")