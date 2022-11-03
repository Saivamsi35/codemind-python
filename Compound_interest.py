p,r,t=map(int,input().split())
Amount = p * (pow((1 + r/ 100), t))
a="{:.2f}".format(Amount)
print(a)