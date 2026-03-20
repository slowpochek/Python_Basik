print("Hi, do you want to convert from number to date?")
numbers= None
while True:
    whanted = input("If you want, enter yes; if you don't want, enter no :")
    whanted = whanted.lower()
    if whanted == "yes" or whanted == "y":
        while True:
            try :
                time = int(input("Enter the number you want to convert: "))
                if time < 0:
                    sign = -1
                else:
                    sign = 1
                time = abs(time)
                days = time//86400
                days*=sign
                hours = time % 86400 // 3600
                hours *= sign
                minutes = time % 3600 // 60
                minutes *= sign
                seconds =time % 3600 % 60
                seconds *= sign
                if days % 100 >= 11 and days % 100 <= 19:
                    word = "днів"
                else:
                    if days % 10 == 1:
                        word = "день"
                    elif days % 10 >= 2 and days % 10 <= 4:
                        word = "дні"
                    else:
                        word = "днів"
                print(f"{days} {word},{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
                break
            except ValueError :
                print("Please enter correct a number")
    elif whanted == "no" or whanted == "n":
        print("Goodbye")
        break
    else:
        print("Incorrect action")