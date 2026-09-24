import sys
import re

x = len(sys.argv)

if x != 3:
    print("none")
else:
    x1 = sys.argv[1]
    x2 = sys.argv[2]
    result = re.findall(x1,x2)
    print(len(result))
     