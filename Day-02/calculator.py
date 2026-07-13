a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("\n-----Operations Available-----")
print("1.Addition")
print("2.Subtraction:")
print("3.Multiplication")
print("4.Division")
c=int(input("\nEnter your choice: "))
if(c==1):
    print("\nAddition is: ",a+b)
elif(c==2):
    print("Subtraction is: ",a-b)
elif(c==3):
    print("Multiplication is: ",a*b)
elif(c==4):
    if(b!=0):
       print("Division is: ",a/b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid input")

