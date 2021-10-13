import math

def isprime(number):
  if number == 1:
    return False

  for i in range(2,int(math.sqrt(number)+1)):
    if number % i == 0:
      return False
  return True


N = int(input())
answer = 0
array = list(map(int,input().split()))

for i in range(N):
  if isprime(array[i]) == True:
    answer += 1

print(answer)
