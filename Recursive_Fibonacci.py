import re


def recursiveFibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)


print(recursiveFibonacci(30))
