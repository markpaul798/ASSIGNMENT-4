From fuel import convert, gauge


Def test_convert_valid_input():
    Assert convert(“1/2”) == 50
    Assert convert(“2/2”) == 100
    Assert convert(“3/4”) == 75


Def test_convert_invalid_input():
    # Test input that is not in X/Y format
    Try:
        Convert(“1”)
    Except ValueError as e:
        Assert str€ == “Invalid input. Input should be in X/Y format, where X and Y are integers.”

    # Test input where X is greater than Y
    Try:
        Convert(“2/1”)
    Except ValueError as e:
        Assert str€ == “Invalid input. X cannot be greater than Y.”

    # Test input where Y is 0
    Try:
        Convert(“1/0”)
    Except ZeroDivisionError as e:
        Assert str€ == “Invalid input. Y cannot be 0.”


Def test_gauge():
    Assert gauge(0) == “E”
    Assert gauge(1) == “E”
    Assert gauge(50) == “50%”
    Assert gauge(99) == “F”
    Assert gauge(100) == “F”
