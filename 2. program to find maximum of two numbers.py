# Finding maximum between two numbers

# Method 1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("The greater number is: " + str(num1))
elif num2 > num1:
    print("The greater number is: " + str(num2))
else:
    print("Both numbers are equal")

# Method 2

def findingMaximum(number1, number2):
    if number1 > number2:
        # print("The maximum number is: " + str(number1))
        return number1
    elif number2 > number1:
        # print("The maximum number is: " + str(number2))
        return number2
    else:
        # print("Both numbers are equal")
        return "Both numbers are equal"


first = int(input("Enter the number1: "))
second = int(input("Enter the number2: "))


result = findingMaximum(first, second)
print(result)


