# 0 1 1 2 3 5 8 13 21

a=int(input("enter a frist number of Fibonacci series\n"))
b=int(input("enter a second number of Fibonacci series\n"))
n=int(input("enter elements in Fibonacci series\n"))

for i in range (n):
    c=a+b
    a=b
    b=c

    print(c, end=" ")
