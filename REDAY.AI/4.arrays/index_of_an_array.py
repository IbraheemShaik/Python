def find_index(arr, element):
    try:
        index = arr.index(element)
        return index
    except ValueError:
        return -1

numbers = [71, 23, 65, 82, 50]
ele = 23
index = find_index(numbers, ele)

if index != -1:
    print(f"The index of {ele} is: {index}")
else:
    print(f"{ele} is not in the list.")

