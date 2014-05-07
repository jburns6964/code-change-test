import time
p = 10
while p != 0:
   print("There are {0} green bottles hanging for a wall".format(p))
   time.sleep(0.2)
   print("There are {0} green bottles hanging for a wall".format(p))
   time.sleep(0.2)
   print("and if 1 green bottle should accidentaly fall")
   time.sleep(0.2)
   p = p-1
   print("there will be {0} green bottles hanging on the wall".format(p))
   print()
