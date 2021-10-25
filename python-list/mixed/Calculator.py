
def add(a, b):
    print("\nResult is :", a+b)


def sub(a, b):
    print("\nResult is :", a-b)


def mul(a, b):
    print("\nResult is :", a*b)


def div(a, b):
    print("\nResult is :", a/b)


while True:
    print("""\n select which operation do you want to do \n press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division""")

    choice = int(input("\n"))

    a = float(input("enter a first variable\n"))
    b = float(input("enter a second variable\n"))

    if choice == 1:
        add(a, b)
    elif choice == 2:
        sub(a, b)
    elif choice == 3:
        mul(a, b)
    elif choice == 4:
        div(a, b)

    confirmation = input("\nyou want to do the operations again press (Y/N)\n")
    if confirmation == "n":
        break

    else:
        print("  \n   ")
