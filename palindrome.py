'''
To check whether the given number is palindrome or not
Palindrome number is a number which remains same even after it is reversed
'''
x = int(input("Enter an number:"))
reverse = 0
temp = x
while temp > 0:
    digit = temp % 10     #'''To get the last digit'''
    reverse = (reverse * 10) + digit
    temp = temp // 10
    if temp < 0:
        break

if x == reverse:
    print("The number is palindrome number")
else:
    print("The number is not a palindrome number")
