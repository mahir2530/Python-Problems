print('MAIN MENU')
print('1 For ADDITION')
print('2 For SUBTRACTION')
print('3 For MULTIPLICATION')
print('4 For DIVISION')

choice = int(input("Enter your choice: "))

a = int(input("Enter a Value: "))
b = int(input("Enter b Value: "))

if choice == 1:
    result = a + b
    print("The result of addition is: ",result)
elif choice == 2:
    result = a - b
    print("The result of subtraction is: ",result)
elif choice == 3:
    result = a * b
    print("The result of multiplication is: ",result)
elif choice == 4:
    if b != 0:
        result = a / b
        print("The result of division is: ",result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid option from the menu.")
