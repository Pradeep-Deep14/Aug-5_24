# Question.1 you are given below string take the sum of all the sale amount
# please note that string object may have space as well!


sales = '100, unknown, unknown,     20, 20, 10'

my_list=sales.split(',')
#print(my_list)

total=0
for item in my_list:
    item1 = item.strip()
    try:
        total += int(item1)
    except ValueError:
        pass
print(total)
