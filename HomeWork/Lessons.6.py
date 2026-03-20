#Добуток чисел
print("Hi, let's calculate the product of numbers")
numbers= None
while True:
    whanted = input("If you want, enter yes; if you don't want, enter no :")
    whanted = whanted.lower()
    if whanted == "yes" or whanted == "y":
        while True:
            try:
                numbers=int(input("Enter your number :"))
                if numbers<0:
                    sign=-1
                else:
                    sign=1
                numbers=abs(numbers)
                if numbers == 0 or numbers == 1:
                    print(f"Additional numbers : {numbers}")
                else:
                    while(numbers>9):
                        result=1
                        while(numbers>0):
                            digit=numbers%10
                            result*=digit
                            numbers//=10
                        numbers=result
                    numbers*=sign
                    print(f"Additional numbers :{numbers}")
                break
            except ValueError:
                print("Please enter correct a number")
    elif whanted == "no" or whanted == "n":
        print("Goodbye")
        break
    else:
        print(" Incorrect action")

