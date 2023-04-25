Def value(greeting):
    # Convert the greeting to lowercase for case-insensitive matching
    Greeting = greeting.lower()

    # Check if the greeting starts with “hello”
    If greeting.startswith(“hello”):
        Return 0

    # Check if the greeting starts with “h” (but not “hello”)
    Elif greeting.startswith(“h”):
        Return 20

    # Return 100 for any other greeting
    Else:
        Return 100


Def main():
    # Prompt the user for a greeting
    Greeting = input(“Enter a greeting: “)

    # Calculate the value of the greeting
    Print(“The value of the greeting is:”, value(greeting))


If __name__ == “__main__”:
    Main()
