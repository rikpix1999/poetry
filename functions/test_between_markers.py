def between_markers(text: str, start: str, end: str) -> str:
    
    return  text[text.index(start)+1:text.index(end)]
def test_between_markers():
    assert between_markers('What is >apple<', '>', '<') == 'apple'
    assert between_markers('What is [apple]', '[', ']') == 'apple'
    assert between_markers('What is ><', '>', '<') == ''
    assert between_markers('[an apple]', '[', ']') == 'an apple'