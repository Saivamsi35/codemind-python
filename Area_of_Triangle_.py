a,b,c=map(int,input().split())
s=(a+b+c)/2
#area of the triangle
#(s*(s-a)*(s-b)*(s-c))**0.5
x=s-a
y=s-b
z=s-c
Area=(s*x*y*z)**(0.5)
flo="{:.2f}".format(Area)
print(flo)