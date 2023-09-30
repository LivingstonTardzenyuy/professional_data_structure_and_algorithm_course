def fibonacciNumber(n):
    assert n >=0 and int(n)==n, "The value must be postive starting from 0"
    if n in [0,1]:
        return n
    else:
        return fibonacciNumber(n-1) + fibonacciNumber(n-2)

value = int(input('Enter n:'))

print(fibonacciNumber(value))