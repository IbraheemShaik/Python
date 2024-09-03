def arithmetic_operation(x, y, opr):
    if opr == '+':
        return x + y
    elif opr == '-':
        return x - y
    elif opr == '*':
        return x * y
    elif opr == '/':
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

while(True):
    x=int(input("enter first num "))
    y=int(input("enter  second num "))
    opr=str(input("enter operator "))
    result = arithmetic_operation(x, y, opr)
    print(result) 
    c=str(input("DO YOU WANT TO DO AGAIN ? Y/N  "))
    if c=='N' or c=='n':
        break
