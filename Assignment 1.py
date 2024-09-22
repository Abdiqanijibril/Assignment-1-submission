'''
This project was done by Abdiqani Jibril AJ

'''
print ("add")
print("Sub")
print("mult")
print("div")
    
option = (input("choose an operation:"))


Choose = (input("What do you numerical type do you want to use Float or Integers:"))


if Choose == "Float":
    option in {"add", "sub", "mult", "div"}
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
if Choose == "Integers":
    option in {"add", "sub", "mult", "div"}
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))



if (option == "add"):
    result = num1 + num2
    print("The result is", result)
elif (option == "sub"):
    result = num1 - num2
    print("The result is", result)
elif (option == "mult"):
    result = num1 * num2
    print("The result is", result)
elif (option == "div"):
    result = num1 / num2
    print("The result is", result)
else:
    print("This wrong")













