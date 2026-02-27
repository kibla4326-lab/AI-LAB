last_value = 0   

while True:
    new_value = int(input("Enter a number (0 to stop): "))

    if new_value == 0:
        print("Game stopped.")
        break

    total = last_value + new_value   

    if total % 3 == 0 and total % 5 == 0:
        result = "Fizz Buzz"
    elif total % 3 == 0:
        result = "Fizz"
    elif total % 5 == 0:
        result = "Buzz"
    else:
        result = "None"
    print("Number entered:", new_value)
    print("Result:", result)

    last_value = new_value