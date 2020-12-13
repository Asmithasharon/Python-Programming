'''
To find the reverse of the given digit
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
print("The reverse of given number:", reverse)


