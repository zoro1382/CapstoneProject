from subtraction import subtract

while True:
    choice = input("1. Add\n2. Subtract\n3. Exit\nEnter you choice:")
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    if choice == '3':
        print("Thanks for using our program!")
        break
    elif choice == "1":
        pass
    elif choice == "2":
        print(subtract(num1, num2))

