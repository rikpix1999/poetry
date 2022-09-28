def number_length(a: int) -> int:
    # your code here
    lunghezza=len(str(a))
    return lunghezza
def test_number_length():
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2