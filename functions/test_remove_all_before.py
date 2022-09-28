from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    if border in items:
        idx=items.index(border)
        return items[idx:]
    else:
        return items
    
    
    return items
def test_remove_all_before():
    assert remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
    assert remove_all_before([1, 1, 2, 4, 2, 3, 4], 2) == [2, 4, 2, 3, 4]
    assert remove_all_before([1, 1, 5, 6, 7], 2) == [1, 1, 5, 6, 7]