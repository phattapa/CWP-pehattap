step = 10

for i in range(step+1):
    out1 = "Table de " + str(i) + ":"
    print(out1,end="")
    for j in range(step+1):
        out2 = " " + str(i*j)
        print(out2,end="")
    print("")