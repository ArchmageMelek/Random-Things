# do stuff

import sys
import random
import math

#print(sys.argv)

thing = int(sys.argv[1])
thing2 = int(sys.argv[2])

#print(thing)
#print(thing2)

print(math.floor(random.random()*(thing2-thing+1)+thing))
