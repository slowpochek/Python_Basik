# Розділити один список на два списки
numbers=[1,2,3,4,5]
middle=(len(numbers)+1)//2
first_half=numbers[:middle]
second_half=numbers[middle:]
print(first_half,second_half)