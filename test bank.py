From bank import value


Def test_value_hello():
    Assert value(“Hello, world!”) == 0
    Assert value(“hello there”) == 0


Def test_value_h():
    Assert value(“hi there”) == 20
    Assert value(“hey, how are you?”) == 20


Def test_value_other():
    Assert value(“goodbye”) == 100
    Assert value(“howdy”) == 100
    Assert value(“hELLO, wORLD!”) == 0
    Assert value(“greetings”) == 100
