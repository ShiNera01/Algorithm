n = int(input())

time_array = []
profit = []
next_array = []

result = [0] * n

for _ in range(n):
  a,b = map(int,input().split())
  time_array.append(a)
  profit.append(b)

for i in range(n):
  if time_array[i] -1  + i < n:
    next_array.append(time_array[i]  + i )
  else:
    next_array.append(-1)

for i in range(n-1,-1,-1):
  if next_array[i] >= n:
    result[i] = profit[i]
  elif time_array[i] - 1 + i >= n:
    result[i] = 0
  else:
    result[i] = profit[i]  + max(result[next_array[i]:])

print(max(result))
