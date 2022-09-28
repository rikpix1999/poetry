def first_word(text: str) -> str:
    # your code here
    parole=text.split()
    
    return parole[0]
def test_first_word():
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("greeting from CheckiO Planet") == "greeting"
    assert first_word("hi") == "hi"