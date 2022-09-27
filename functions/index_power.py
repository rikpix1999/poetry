def index_power(array: list, n: int) -> int:
    if n<len(array):
        return array[n]**n
    else:
        return -1
