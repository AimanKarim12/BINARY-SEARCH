def binarySearch(array, item):
  
  top = len(array) - 1
  mid = 0
  bottom = 0
  
  while bottom <= top:
    mid = (top + bottom) // 2
    if array[mid] < item:
      bottom = mid + 1
    elif array[mid] > item:
      top = mid - 1
    else:
      return mid
  return - 1
    
list = [10, 30, 40, 45, 70, 80, 85, 90, 100]
item = 45

result = binarySearch(list, item)

if result != -1:
  print("Element is present at index", str(result)) 
else:   
  print("Element is not present in list")