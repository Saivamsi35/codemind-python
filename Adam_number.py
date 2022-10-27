n=int(input()) #12
sqr=n*n #144
s=""
s1=""
while n>0:
    r=n%10
    n=n//10
    s+=str(r)#21
sqr1=(int(s)**2)#441
while sqr1>0:
    r1=sqr1%10
    sqr1=sqr1//10
    s1+=str(r1)#441
if int(s1)==int(sqr):
    print("True")
else:
    print("False")