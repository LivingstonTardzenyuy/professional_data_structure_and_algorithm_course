# def convertDecimalToBinary(n, list):
#     if n == 1:
#         return 1
#     else:
#         convertDecimalToBinary(int(n/2), list)
#         list.insert(n%2)

# list = []
# value = int(input('enter n: '))
# convertDecimalToBinary(value, list)



# Question 4
def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(int(n/2))


print(decimalToBinary(43))
