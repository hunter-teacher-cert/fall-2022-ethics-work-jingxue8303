# binsearch.py
# Jing Xue
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

def binsearchOne(a, t):
  low = 0
  high = len(a) - 1
  mid = int((low + high) / 2)
  while (high > low):
    if a[mid] == t:
     print (mid)
    elif low >= high :
      print(-1)
    elif (a[mid] < t):
      low = mid +1
    else : 
      high = mid -1
    mid = int((low + high) / 2)

#def binsearchRecursive (a, value, loIndex, hiIndex):
  #if hiIndex >= loIndex :
  #  mid = (hiIndex + loIndex) / 2
  #  if a[mid] == value:
  #    print(mid)
  #  if a[mid] < value:
 #     binsearchRecursive(a, value, mid+1, hiIndex)
  #  binsearchRecursive(a, value, loIndex, mid-1)
#  print(-1)


binsearchOne([1,2,3], 4)


      
  