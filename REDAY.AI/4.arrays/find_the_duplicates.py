def find_duplicates(arr):
    dup = []
    unique = []
    
    for value in arr:
        if value in unique :
            if value not in dup:
                dup.append(value)
        else:
            unique.append(value)
    
    return dup,unique

array = [10, 22, 51, 42, 51, 33, 62, 81, 22, 51]
duplicates, uni= find_duplicates(array)
print(uni)
print("Duplicates:", duplicates)
