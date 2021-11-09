num1 = input("#1 Number: ")
art = input("Operation: ")
num2 = input("#2 Number: ")

num1 = int(num1)
num2 = int(num2)

if art == "+":
    print("", num1, "+", num2)
    print("Answer: ", num1 + num2)

elif art == "-":
    print("", num1, "-", num2)
    print("Answer: ", num1 - num2)

elif art == "*":
    print(": ", num1, "*", num2)
    print("Answer: ", num1 * num2)

elif art == "/":
    print("", num1, "/", num2)
    print("Answer:", num1 / num2)


