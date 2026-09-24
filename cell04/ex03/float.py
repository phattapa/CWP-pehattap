x = input("Give me a number: ")

try :
    n = float(x)

    if n.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

except ValueError:
    print("This is not a number !")