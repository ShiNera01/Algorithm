N = int(input())

dic = dict()

for i in range(N):
  word = input()
  if word in dic:
    dic[word] += 1
  else:
    dic[word] = 1

dic = sorted(dic.items(), key = lambda x: (-x[1],x[0]))

print(dic[0][0])
