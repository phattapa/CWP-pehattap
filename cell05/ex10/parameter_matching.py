import sys
import re

x = len(sys.argv)

if x != 2:
    print("none")
else:
    x1 = sys.argv[1]
    x2 = input("What was the parameter? ")
    if x1 == x2:
        print("Good job!")
    else:
        print("Nope, sorry...")

