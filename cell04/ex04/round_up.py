n = float(input("Give me a number: "))

n_round = round(n,0)

if n_round >= n:
    print(int(n_round))
else:
    print(int(n_round + 1))
