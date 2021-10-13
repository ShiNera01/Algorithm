from itertools import combinations

array = []
answer = []
for i in range(9):
  array.append(int(input()))


comb = list(combinations(array,7))


for i in range(len(comb)):
  if sum(comb[i]) == 100:
    answer = list(comb[i][:])
    break

answer.sort()

for i in range(len(answer)):
  print(answer[i])
