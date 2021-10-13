number_input = int(input())
array = [0,1]

if number_input == 0 or number_input == 1:
  print(number_input)
else:
  for i in range(2,number_input+1):
    array.append(array[i-1]+array[i-2])

  print(array[-1])
