def factorialRecursive(n):
    assert n >=0 and int(n) == n, "the number must be a postive integer only"
    if n in [0,1]:
        return 1
    else:
        return n * factorialRecursive(n-1)

value = int(input('Enter n:'))
print(factorialRecursive(value))