def max_digit(a: int) -> int:
    a=str(a)
    a=max(map(int,a))    
    return a

def test_max_digit():
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1