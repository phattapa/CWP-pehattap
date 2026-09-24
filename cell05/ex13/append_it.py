import sys
import re

x = len(sys.argv)

if x < 2:
    print("none")
else:
    for i in (sys.argv[1:]):
        if i.endswith("ism"):
            pass
        else :
            print(f"{i}ism")
