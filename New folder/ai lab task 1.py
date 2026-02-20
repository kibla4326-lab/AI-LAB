print("Simple Calculator (type 'exit' to quit)")

while True:
    expr = input("Enter calculation: ")

    if expr.lower() == "exit":
        print("Goodbye!")
        break

    try:
        print("Result:", eval(expr))
    except:
        print("Invalid expression")