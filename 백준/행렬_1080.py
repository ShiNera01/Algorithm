def swap(a):
  if a == "1":
    return "0"
  else:
    return "1"

a,b = map(int,input().split())

array_a = []
array_b = []
answer = 0


for i in range(a):
  word = list(input())
  array_a.append(word)

for i in range(a):
  word = list(input())
  array_b.append(word)


for i in range(a-2):
  
  for j in range(b-2):
    if array_a[i][j] != array_b[i][j]:
      array_a[i][j] = swap(array_a[i][j])
      array_a[i][j+1] = swap(array_a[i][j+1])
      array_a[i][j+2] = swap(array_a[i][j+2])
      array_a[i+1][j] = swap(array_a[i+1][j])
      array_a[i+1][j+1] = swap(array_a[i+1][j+1])
      array_a[i+1][j+2] = swap(array_a[i+1][j+2])
      array_a[i+2][j] = swap(array_a[i+2][j])
      array_a[i+2][j+1] = swap(array_a[i+2][j+1])
      array_a[i+2][j+2] = swap(array_a[i+2][j+2])
      answer += 1


if array_a == array_b:
  print(answer)
else:
  print(-1)
