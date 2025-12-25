//nice# a calculator for simple operations.

while True:
    x = float(input("first number: ").strip())    
    op = (input("operation: ").strip())
    if op == "*":
        y = float(input("second number: ").strip())
        e = x * y
        print(f"the result of {x} * {y} is: {e}")
        break
    elif op == "/":
        y = float(input("second number: ").strip())
        e = x / y
        print(f"the result of {x} / {y} is: {e}")
        break
    elif op == "+":
        y = float(input("second number: ").strip())
        e = x + y
        print(f"the result of {x} + {y} is: {e}")
        break
    elif op == "-":
        y = float(input("second number: ").strip())
        e = x - y
        print(f"the result of {x} - {y} is: {e}")
        break
    else:
        print("invalid operation!!! [+, -, *, /]")
    
