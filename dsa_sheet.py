# try:
#     num = float(input("Enter a number: "))
# except ValueError:
#     print("Please enter a valid number.")
#     raise SystemExit(1)



# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")



# try:
#     num = float(input("Enter a number: "))
# except ValueError:
#     print("Please enter a valid number.")
#     raise SystemExit(1)


# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")



# a = int(input("Enter a number: "))
# if a % 5 == 0: 
#     print("The number is divisible by 5.")
# else:
#     print("The number is not divisible by 5.")



# a = int(input("Enter a number: "))
# if a % 5 == 0 and a % 3 == 0: 
#     print("The number is divisible by both 5 and 3.")
# else:
#     print("The number is not divisible by both 5 and 3.")
    


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# print(max(num1, num2))



# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# print(max(num1, num2, num3))



# temperature = float(input("Enter the temperature in Celsius: "))
# if temperature > 30:
#     print("It's hot.")
# elif temperature < 10:
#     print("It's cold.")
# else:
#     print("It's warm.")



# c = input("Enter a character: ")
# print("The character is a vowel." if c.lower() in 'aeiou' else "The character is a consonant.")


f = input("Enter a character: ")
if f.isalpha():
    print("The character is an alphabet.")
else:    
    print("The character is not an alphabet.")
