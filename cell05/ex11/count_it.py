import sys
import re

x = len(sys.argv)

if x < 2:
    print("none")
else:
    for i in range (len(sys.argv[1:])):
        print(f"{sys.argv[i+1]}: {len(sys.argv[i+1])}")
