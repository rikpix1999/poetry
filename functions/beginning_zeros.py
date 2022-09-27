def beginning_zeros(a: str) -> int:
        a_num = int(a)
        if not a_num: # case a as all zeros
            return len(a)
        return len(a) - len(str(a_num))
    