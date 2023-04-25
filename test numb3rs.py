From numb3rs import validate

Def test_valid_ipv4_address():
    Assert validate(“192.168.0.1”) == True
    Assert validate(“10.0.0.0”) == True
    Assert validate(“172.16.0.255”) == True

Def test_invalid_ipv4_address():
    Assert validate(“256.168.0.1”) == False
    Assert validate(“172.16.0.256”) == False
    Assert validate(“1.2.3”) == False
    Assert validate(“1.2.3.4.5”) == False
