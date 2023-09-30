def sumOfDigitsOfPositiveInteger(n):
    assert n >=0 and int(n) == n, "The value must be positive"
    if n < 10:
        return n
    else:
        
        return int(n%10)  + sumOfDigitsOfPositiveInteger(int(n/10))

result = 0
value = int(input('Enter the value of n: '))
print(sumOfDigitsOfPositiveInteger(value))
 