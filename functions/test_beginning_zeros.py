def beginning_zeros(a: str) -> int:
        a_num = int(a)
        if not a_num: # case a as all zeros
            return len(a)
        return len(a) - len(str(a_num))
    
def test_beginning_zeros():
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2