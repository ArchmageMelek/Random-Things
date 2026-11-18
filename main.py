# do stuff

import sys
import random
import math

#print(sys.argv)

thing = int(sys.argv[1])
thing2 = int(sys.argv[2])

#print(thing)
#print(thing2)

#red back
print("\033[41m" + str(math.floor(random.random()*(thing2-thing+1)+thing)) + "\033[0m")
