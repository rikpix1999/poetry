def backward_string(val: str) -> str:
    
    return val[::-1]

def test_backward_string():
    assert backward_string("val") == "lav"
    assert backward_string("") == ""
    assert backward_string("ohho") == "ohho"
    assert backward_string("123456789") == "987654321"