def checkio(number: int) -> str:
    if (number%3==0) and (number%5==0):
        return "Fizz Buzz"
    elif (number%3==0) and (number%5!=0):
        return "Fizz"
    elif (number%5==0) and (number%3!=0):
        return "Buzz"
    else:
        return str(number)
def test_checkio():
    assert checkio(15) == "Fizz Buzz"
    assert checkio(6) == "Fizz"
    assert checkio(10) == "Buzz"
    assert checkio(7) == "7"