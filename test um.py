From um import count


Def test_count_no_um():
    Assert count(“hello world”) == 0
    Assert count(“this is a test”) == 0


Def test_count_one_um():
    Assert count(“um, what was I saying?”) == 1
    Assert count(“I need to, um, think about that.”) == 1


Def test_count_multiple_um():
    Assert count(“um, um, um, um”) == 4
    Assert count(“um, let me think…um…oh, right!”) == 2
    Assert count(“um, excuse me, um, do you have the time?”) == 2
