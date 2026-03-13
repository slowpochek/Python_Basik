# Модифікувати калькулятор
print("Hi, do you want to count something? :")
while True:
    whanted = input("If you want, enter yes; if you don't want, enter no :")
    whanted=whanted.lower()
    if whanted == "yes" or whanted == "y":
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        print("Select an action : + , - , * , / ")
        action = input()
        match action:
            case "+":
                print(first_number + second_number)
            case "-":
                print(first_number - second_number)
            case "/":
                if second_number == 0:
                    print("You can't divide by zero")
                else:
                    print(first_number / second_number)
            case "*":
                print(first_number * second_number)
            case _:
                print("Incorrect action")
        print("Want more ")
        continue

    elif whanted == "no" or whanted == "n":
        print("Goodbye")
        break
    else :
        print(" Incorrect action")


