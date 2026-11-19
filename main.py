# Random generator, with two arguments it returns a random number between the two, with more than two, it returns one at random
import sys
import random

# text colour options
REDBACK = "\033[41m"
CLEAR = "\033[0m"

# pop out the filename leaving only the args behind
filename = sys.argv.pop(0)

if len(sys.argv) == 2:
    # Two args means return a number between the two inclusively
    try:
        # Try to grab the two numbers and convert to ints
        lowest_number = int(sys.argv[0])
        highest_number = int(sys.argv[1])
    except ValueError as ex:
        # Conversion failed
        print(REDBACK + "You must supply two integers." + CLEAR)
    except Exception as ex:
        # Some other exception!
        print(REDBACK + type(ex).__name__ + ": " + str(ex) + CLEAR)
    else:
        # If no error occured, generate a random int between the two values
        print(REDBACK + str(random.randint(lowest_number, highest_number)) + CLEAR)
elif len(sys.argv) > 2:
    # more than 2 args means select one at random and print
    item_list = sys.argv
    
    # Pick one item at random and print it
    print(REDBACK + random.choice(item_list) + CLEAR)
else:
     # Fewer than 2 args supplied
     print(REDBACK + "Please supply at least 2 args." + CLEAR)
