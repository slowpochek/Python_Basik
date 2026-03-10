# Перемістити всі нулі до кінця списку
numbers =[0,0,0,0,0,0,0,0,0]
zero_in_numbers=numbers.count(0)
if zero_in_numbers>0 and len(numbers)!=1:
    if  zero_in_numbers==len(numbers):
        print(numbers)
    else:
        for i in range(zero_in_numbers):
            numbers.remove(0)
            numbers.append(0)
        print(numbers)
else :
    print(numbers)

# мне кажется лучше бы я подумал над другими вариантами а не проверками )))
