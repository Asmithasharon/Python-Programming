'''
To find the square root of a number using newton's method.
'''

def sq_root(number, precision):
    sqroot = number
    while abs(number - (sqroot * sqroot)) > precision :
        #'''abs() is to get the absolute value'''
        sqroot = (sqroot + number / sqroot) / 2
    return sqroot

number = int(input("Enter a number: "))
precision = 10 ** -4
print(sq_root(number , precision))



