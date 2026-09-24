import sys
import re

x = len(sys.argv)

if x != 3:
    print("none")
else:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    ans = [i for i in range(n1,n2+1)]
    print(ans)