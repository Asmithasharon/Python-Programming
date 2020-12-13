'''
To find the gcd of two numbers using euclid algorithm for finding gcd
'''
def gcd_numbers(a, b):
    if a < b:
        (a, b) = (b, a)
    if(a % b) == 0:
        return b
    else:
        return gcd_numbers(b, a % b)  #'''Recursive function'''


a = int(input("ENTER THE FIRST NUMBER: "))
b = int(input("ENTER THE SECOND NUMBER: "))
print(gcd_numbers(a, b))             #'''To call the gcd_numbers() function'''





