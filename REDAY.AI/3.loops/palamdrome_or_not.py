def palindrome_or_not(x):
    x = x.replace(" ", "").lower()
    return x == x[::-1]

a = input("Enter a string: ")

if palindrome_or_not(a):
    print(f"'{a}' is a palindrome.")
else:
    print(f"'{a}' is not a palindrome.")
