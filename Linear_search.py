def linear_search(arr , target):
  size = len(arr)
  for index in range (0,size):
    if(arr[index] == target):
      return index

  return -1


my_list = [10,23,45,70,11]
target = 70
result = linear_search(arr, target)
print(result)
