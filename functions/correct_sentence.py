def correct_sentence(text: str) -> str:
    """
    returns a corrected sentence which starts with a capital letter
    and ends with a dot.
    """
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text

