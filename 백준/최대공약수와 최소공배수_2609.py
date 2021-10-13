import math

a,b = map(int,input().split())

ans1 = math.gcd(a,b)
ans2 = a*b//ans1

print(ans1)
print(ans2)
