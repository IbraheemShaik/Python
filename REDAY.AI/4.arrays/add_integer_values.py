def sum_of_array_ele(arr):
    total = 0
    for num in arr:
        total += num
    return total
    
n = [50, 263, 21, 74, 568]
r = sum_of_array_ele(n)
print(f"The sum of the integers in array is: {r}")
