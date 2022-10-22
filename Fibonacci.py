def Fibonacci(number):

    list_fib = [0, 1]

    for i in range(2, number):
        list_fib.append(list_fib[i-1] + list_fib[i-2])

    return list_fib


print(Fibonacci(9))
