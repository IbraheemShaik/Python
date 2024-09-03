def average(arr):
    if not arr:
        raise ValueError("The list is empty")
    
    total = sum(arr)
    count = len(arr)
    average = total / count
    return average

numbers = [156, 213, 143, 342, 531]
result = average(numbers)
print(f"The average is: {result:.2f}")
