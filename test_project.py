from project import fuzz_ratio
from project import read_file
from project import write_file

def test_fuzz_ratio():
    assert fuzz_ratio(bytes) == ("bytes()", "Returns a bytes object", "Sorry, no more info about bytes() yet!")
    assert fuzz_ratio("wrong") == ("ValueError", "Raised when there is a wrong value in a specified data type", "Sorry, no more info about ValueError yet!")
    try:
        assert "WrongAnswer" in fuzz_ratio(message)
    except NameError:
        assert True
    else:
        assert False

def test_read_file():
    assert read_file("dict.csv") != ""
    try:
        assert read_file("wrong.csv")
    except FileNotFoundError:
        assert True
    else:
        assert False
        
def test_write_file():
    assert write_file("test") != "'test' is added to requests for learning purposes"
    assert write_file("requests.csv") != ""
    try:
        assert read_file("wrong.csv")
    except FileNotFoundError:
        assert True
    else:
        assert False