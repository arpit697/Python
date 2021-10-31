def pal(num):
    rev = num[::-1]

    if rev == num:
        print("the passed argument is palindrome")

    else:
        print("the passed argument is not a palindrome")


x=int(input("enter the number to check weatehr it is palindrome or not"))
s=str(x)
pal(s)
