number =[12,3,4,5,1,3]
sum_number = 0
if len(number) == 0 :
        print(0)
elif len(number) > 0 :
        for i in range(0, len(number), 2):
                sum_number+= number[i]
        print(sum_number*number[-1])




