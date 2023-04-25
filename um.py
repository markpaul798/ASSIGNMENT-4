Def count(s):
    # Split the text into words and convert to lowercase
    Words = s.lower().split()

    # Count the number of times “um” appears as a standalone word
    Count = 0
    For word in words:
        If word == “um”:
            Count += 1

    Return count


Def main():
    Print(count(input(“Text: “)))


If __name__ == “__main__”:
    Main()
