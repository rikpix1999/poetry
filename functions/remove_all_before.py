def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    if border in items:
        idx=items.index(border)
        return items[idx:]
    else:
        return items
    
    
    return items