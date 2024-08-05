input_list = [1, 2, 2, 3, 4, 5, 5]

def remove_duplicates(input_list):
    seen = set()
    result = []
    result1 = []
    for i in input_list:
        if i not in seen:
            result.append(i)
            seen.add(i)  # Add the item to the seen set
        else:
            result1.append(i)
    return result, result1

# Call the function and print the result
unique_list, duplicates = remove_duplicates(input_list)
print("Unique list:", unique_list)
print("Duplicates:", duplicates)
