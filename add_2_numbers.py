# Python program adding two numbers

# solution method 1
number_1 = 56
number_2 = 90

# Now we are adding 2 numbers
adding = number_1 + number_2

# print("Result is: " + str(adding))
# print("Sum of: " + "number_1" + "+" + "number_2 " + "is this" + str(adding))
print("The sum of {0} and {1} is {2}".format(number_1, number_2, adding))

# Solution method 2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_of = num1 + num2

print("The sum of {0} and {1} is {2}".format(num1, num2, sum_of))

