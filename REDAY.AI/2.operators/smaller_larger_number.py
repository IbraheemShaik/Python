def smaller_and_larger(x, y):
    if x < y:
        smaller = x
        larger = y
    elif x > y:
        smaller = y
        larger = x
    else:
        smaller = larger = x 
    
    return smaller, larger

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

smaller, larger = smaller_and_larger(num1, num2)

if smaller == larger:
    print("Both numbers are equal.")
else:
    print("Smaller number: ",smaller)
    print("Larger number: ",larger)
