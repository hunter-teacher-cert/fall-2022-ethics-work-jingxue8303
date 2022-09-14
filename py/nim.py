# nim.py
# Jing Xue
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

import random
stone = 12
stoneTaken = 0
stoneRemain = stone - stoneTaken
#player 
#machine
maxPick = 3
print ('There are total number of ' + str(stone) + ' stone')
while stoneRemain >0 :
  player = input('Choose the number of stone you want to pick (from 1 to ' + str(maxPick) + '):')
  stoneTaken = int(player) + stoneTaken
  stoneRemain = stone - stoneTaken
  print ('Player took ' + str(player) + ' stones')
  print ('Stone remaining: ' + str(stoneRemain))
  if stoneRemain <= 0:
    print ('Player wins')
    break
  if stoneRemain <= maxPick:
    machine = stoneRemain
  else: machine = random.randint(1,3)
  stoneTaken = stoneTaken + machine
  stoneRemain = stone - stoneTaken
  print('Machine took ' + str(machine) + ' stones')
  print ('Stone remaining: ' + str(stoneRemain))
  if stoneRemain <= 0:
    print ('Machine wins')
    break
print ('The game has ended.')