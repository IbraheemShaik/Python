def even_or_odd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))

result = even_or_odd(num)
print(f"The number {num} is {result}.")
