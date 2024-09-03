def insert_element(arr, i, element):
    if i < 0 or i > len(arr):
        raise IndexError("Index out of range.")
    arr.insert(i, element)
    return arr

arr = [10,20,30,40,50,60]
position = 2
ele = 99
updated_list = insert_element(arr, position, ele)
print(f"Updated list: {updated_list}")
