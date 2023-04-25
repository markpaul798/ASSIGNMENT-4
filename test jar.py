From jar import Jar


Def test_init():
    Jar = Jar(5)
    Assert jar.capacity == 5
    Assert jar.size == 0

    Jar = Jar()
    Assert jar.capacity == 12
    Assert jar.size == 0

    Try:
        Jar = Jar(-5)
    Except ValueError:
        Pass
    Else:
        Assert False


Def test_str():
    Jar = Jar(5)
    Assert str(jar) == “”

    Jar.deposit(3)
    Assert str(jar) == “🍪🍪🍪”

    Jar.deposit(2)
    Assert str(jar) == “🍪🍪🍪🍪🍪”

    Jar.withdraw(3)
    Assert str(jar) == “🍪🍪”


Def test_deposit():
    Jar = Jar(5)
    Jar.deposit(2)
    Assert jar.size == 2

    Jar.deposit(3)
    Assert jar.size == 5

    Try:
        Jar.deposit(1)
    Except ValueError:
        Pass
    Else:
        Assert False


Def test_withdraw():
    Jar = Jar(5)
    Jar.deposit(3)
    Jar.withdraw(1)
    Assert jar.size == 2

    Try:
        Jar.withdraw(3)
    Except ValueError:
        Pass
    Else:
        Assert False


Def test_capacity():
    Jar = Jar(5)
    Assert jar.capacity == 5


Def test_size():
    Jar = Jar(5)
    Assert jar.size == 0

    Jar.deposit(2)
    Assert jar.size == 2
