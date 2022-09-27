def end_zeros(a: int) -> int:
    text=str(a)
    text_length=len(text)
    text_without_zero=text.strip("0")
    text_length_without_zero=len(text_without_zero)
    return text_length-text_length_without_zero