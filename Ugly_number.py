n=int(input())
lst=[]
for i in range(1,n):
    if n%i==0:
        lst.append(i)
if 2 in lst or 3 in lst or 5 in lst:
    print("Ugly Number")
elif n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")