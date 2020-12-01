x = int(input("Enter a value: "))
sum = 0
temp = x
while temp > 0:
    digit = temp % 10
    sum = sum + digit
    temp = temp // 10
    if temp < 0:
        break
print("The Sum of Entered Value: ",sum)

