def recursionPowerOfTwo(base, power):
    if power == 0:
        return 1
    else:
        power = base * recursionPowerOfTwo(base, power-1)
        return power 

power = int(input('Enter the power: '))
base = int(input('Enter the base: '))
print(recursionPowerOfTwo(base, power)) 