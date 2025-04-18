"""
Temperature Converter
Take user input via input()
Convert between Celsius and Fahrenheit
Use functions to organize logic
"""
run = True
while (run):
    conversion = input("F->C or C->F? (Type 1 or 2) type q to quit:")
    if conversion == "1": # F->C
        f: float = float(input("Input your temperature in Fahrenheit: "))
        print((f - 32) * (5/9))
    elif conversion == "2":
        c : float = float(input("Input your temperature in Celsius: "))
        print(c * (9/5) + 32)
    elif conversion == "q":
        run = False
    else:
        print("Invalid input")
