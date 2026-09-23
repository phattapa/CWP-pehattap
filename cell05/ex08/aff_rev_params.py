import sys

x = len(sys.argv)

if x < 3:
    print("none")
else:
    for i in sys.argv[1:]:
        print(i)