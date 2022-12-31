def test_simple():
    assert True

def test_string():
    assert "using assert for errors" == "using asert for errors"

def test_fails():
    assert False

def test_list():
    assert ['a', 'very', 'long', 'list', 'of', 'items'] == [
        'a', 'very', 'long', 'list', 'items']