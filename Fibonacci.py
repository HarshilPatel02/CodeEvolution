def Fibonacci(number):
    first = 0
    second = 1
    list_fib = []
    list_fib.append(first)
    list_fib.append(second)

    for i in range(2, number):
        list_fib.append(first + second)
        first = second
        second = list_fib[i]

    return list_fib


print(Fibonacci(4))
