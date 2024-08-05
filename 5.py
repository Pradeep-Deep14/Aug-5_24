input_list=[1,2,2,3,4,5,5]


seen=set()
result=[]

def remove_duplicates(input_list):
    for i in input_list:
        if i not in seen:
            result.append(i)
            seen.add(i)
    
    return print(result)

print(remove_duplicates(input_list))

