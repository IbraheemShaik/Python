def specific_value(arr, value):
    return value in arr

numbers = [20, 60, 55, 40, 44]
val = 55
result = specific_value(numbers, val)

if result:
    print(f"The list contains the value {val}.")
else:
    print(f"The list does not contain the value {val}.")
