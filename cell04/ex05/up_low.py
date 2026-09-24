text = input()

for i in text:
    if i == i.upper():
        print(i.lower(),end="")
    elif i == i.lower():
        print(i.upper(),end="")
print("")

# print(text.swapcase())