n=int(input())
ec=0
oc=0
while n>0:
    r=n%10
    if r%2==0:
        ec+=1
    else:
        oc+=1
    n=n//10
if ec>0 and oc>0:
    print('Mixed')
elif ec>0:
    print("Even")
else:
    print("Odd")