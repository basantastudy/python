# Write a program that uses input() twice to get two numbers from
# the user, multiplies the numbers together, and displays the result.
# If the user enters 2 and 4, then your program should print the
# following text: The product of 2 and 4 is 8.0.

prompt = "Enter a number :"

number1 = int(input(prompt))
number2= float(input(prompt))

mul = number1 * number2

print("The Product of "+ str(number1) + " and "+ str(number2) + " is "+str(mul))