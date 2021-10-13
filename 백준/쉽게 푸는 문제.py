array = []

number = 1
answer = 0
count = 0
a,b = map(int,input().split())
while count <= 1000:
  for i in range(1,number+1):
    array.append(number)
    count += 1
  number += 1
for i in range(a-1,b):
  answer += array[i]

print(answer)
