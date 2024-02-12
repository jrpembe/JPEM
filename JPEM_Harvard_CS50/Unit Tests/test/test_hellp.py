from hello import hello

# initial tests

def test_default():
    assert hello() == "Hello, World"
    
def test_argument():
    assert hello("Jason") == "Hello, Jason"