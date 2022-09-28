def mult_two(a: int, b: int) -> int:
    # your code here
    prod=a*b
    return prod
def test_mult_two():
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0
