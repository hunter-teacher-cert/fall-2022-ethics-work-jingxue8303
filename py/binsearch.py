# binsearch.py
# Jing Xue
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: online resource "GeeksforGeeks"

def binary_search(a, low, high, t):
  if high >= low:
    mid = (high + low) // 2  #round down to integer
    if a[mid] == t:
      return mid
    elif a[mid] > t:
      return binary_search (a, low, mid-1, t)
    else :
      return binary_search (a, mid +1, high, t)
  else : 
    return -1
    
  #low = 0
  #high = len(a) - 1
  #mid = int((low + high) / 2)
  #while (high > low):
  #  if a[mid] == t:
  #   print (mid)
  #  elif low >= high :
  #    print(-1)
  #  elif (a[mid] < t):
  #    low = mid +1
  #  else : 
  #    high = mid -1
  #  mid = int((low + high) / 2)

#def binsearchRecursive (a, value, loIndex, hiIndex):
  #if hiIndex >= loIndex :
  #  mid = (hiIndex + loIndex) / 2
  #  if a[mid] == value:
  #    print(mid)
  #  if a[mid] < value:
 #     binsearchRecursive(a, value, mid+1, hiIndex)
  #  binsearchRecursive(a, value, loIndex, mid-1)
#  print(-1)


# Test with given array
a = [1, 3, 5, 7, 9, 20]
t = 20

result = binary_search (a, 0, len(a)-1, t)

if result != -1:
  print ("Element is present at index", str (result))
else:
  print ("Element not found in array")


      
  