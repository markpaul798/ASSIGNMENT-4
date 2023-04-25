Def convert(fraction):
    # Split the fraction into X and Y
    Try:
        X, y = map(int, fraction.split(‘/’))
    Except ValueError:
        Raise ValueError(“Invalid input. Input should be in X/Y format, where X and Y are integers.”)

    # Check if Y is 0
    If y == 0:
        Raise ZeroDivisionError(“Invalid input. Y cannot be 0.”)

    # Check if X is greater than Y
    If x > y:
        Raise ValueError(“Invalid input. X cannot be greater than Y.”)

    # Calculate the percentage and round to the nearest int between 0 and 100
    Percentage = round((x / y) * 100)

    Return percentage


Def gauge(percentage):
    # Return “E” if percentage is less than or equal to 1
    If percentage <= 1:
        Return “E”
    # Return “F” if percentage is greater than or equal to 99
    Elif percentage >= 99:
        Return “F”
    # Return the percentage followed by “%” for any other value
    Else:
        Return “{}%”.format(percentage)


Def main():
    # Prompt the user to enter the fraction of fuel remaining
    Fraction = input(“Enter the fraction of fuel remaining (in X/Y format): “)

    # Convert the fraction to a percentage
    Try:
        Percentage = convert(fraction)
    Except (ValueError, ZeroDivisionError) as e:
        Print€
        Return

    # Print the fuel gauge reading
    Print(gauge(percentage))


If __name__ == “__main__”:
    Main()
