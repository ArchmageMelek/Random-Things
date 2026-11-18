# do stuff

import sys
import random
import math

#print(sys.argv)

if len(sys.argv) > 3:
    thing1 = sys.argv[1]
    thing2 = sys.argv[2]
    thing3 = sys.argv[3]
    
    print("\033[41m" + random.choice([thing1, thing2, thing3]) + "\033[0m")
else:
    thing = int(sys.argv[1])
    thing2 = int(sys.argv[2])

    #print(thing)
    #print(thing2)

    #red back
    print("\033[41m" + str(math.floor(random.random()*(thing2-thing+1)+thing)) + "\033[0m")
