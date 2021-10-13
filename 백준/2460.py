array = []
number = 0
for i in range(10):
  out_p,in_p = map(int,input().split())
  number += -out_p + in_p
  array.append(number)
  

print(max(array))
