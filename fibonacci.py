def fib(n):
    if n < 0:
        print("invalid input")

    elif n == 1:
        print(1)

    else:
        a=0
        b=1
        for i in range(1, n):
            c=a+b
            a=b
            b=c
        print(b)
        return b

fib(9) 