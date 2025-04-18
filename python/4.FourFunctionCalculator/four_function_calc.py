from unittest import case

print("Four Function Calculator:")
print("+, -, /, *")


run = True
while run:
    op = input("Enter operation (q to quit): ")
    match op:
        case '-':
            first = float(input("Enter the minuend: "))
            second = float(input("Enter the subtractend: "))
            print(first, "-",second,"=",(first - second))
            pass
        case '+':
            first = float(input("Enter the first addend: "))
            second = float(input("Enter the second addend: "))
            print(first, "+",second,"=",(first + second))
            pass
        case '*':
            first = float(input("Enter the multiplicand: "))
            second = float(input("Enter the multiplier: "))
            print(first, "*",second,"=",(first * second))
            pass
        case '/':
            first = float(input("Enter the dividend: "))
            second = float(input("Enter the divisor: "))
            print(first, "/",second,"=",(first / second))
            pass
        case 'q':
            run = False
            pass
        case _:
            print("Invalid choice")
            pass
