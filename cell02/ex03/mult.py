n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))
product = n1 * n2
out1 = f"{n1} x {n2} = {product}"
print(out1)

if product == 0 :
    print("The result is positive and negative.")
elif product > 0:
    print("The result is positive.")
else :
    print("The result is negative.")