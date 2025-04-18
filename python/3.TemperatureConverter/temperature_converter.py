"""
Temperature Converter
Take user input via input()
Convert between Celsius and Fahrenheit
Use functions to organize logic
"""


def main():
    run = True
    while (run):
        conversion = input("F->C or C->F? (Type 1 or 2) type q to quit:")
        if conversion == "1":  # F->C
            f_to_c(float(input("Input your temperature in Fahrenheit: ")))
        elif conversion == "2":
            c_to_f(float(input("Input your temperature in Celsius: ")))
        elif conversion == "q":
            run = False
        else:
            print("Invalid input")

def f_to_c(f : float):
    print((f - 32) * (5 / 9))
def c_to_f(c : float):

    print(c * (9 / 5) + 32)

