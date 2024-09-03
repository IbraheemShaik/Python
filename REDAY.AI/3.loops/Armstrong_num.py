def is_armstrong(x):
    digits = str(x)
    pow = len(digits)
    sum_of_powers = sum(int(i) ** pow for i in digits)
    return sum_of_powers == x

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
