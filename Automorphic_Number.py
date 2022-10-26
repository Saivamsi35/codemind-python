n = int(input())
nl = len(str(n))
sqr = n**2
last_no= sqr%10**nl
if last_no == n:
  print("Automorphic Number")
else:
  print("Not an Automorphic Number")