def gcdOfTwoNumbers(a,b):    
    
    assert int(a) ==a  and int(b) == b, "The number must be integer only"

    if a < 0:
        a = -1 * a

    if b < 0:
        b = -1 * b 

    if b == 0:
        return a 
    else:
        return gcdOfTwoNumbers(b,a%b)

a = int(input('Enter a: '))
b = int(input('Enter b: '))

if a < b:
    a, b = b, a

print(gcdOfTwoNumbers(a,b))
