T = int(input())



for i in range(T):
  array = list(map(int,input().split()))
  array.sort()
  print(array[-3])
