T = int(input())
   
all_number = list(map(int, input().split()))

median = int(T/2)
all_number.sort()
print(all_number[median])
