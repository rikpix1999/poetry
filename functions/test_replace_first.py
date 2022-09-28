from typing import Iterable
def replace_first(items: list) -> Iterable:
    if items:
        items.append(items.pop(0))  # The items.pop(0) method stores the value it cut
                                    # that is, the first one from the list, so we can
                                    # immediately insert it into the list
    return items
def test_replace_first():
    assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
    assert replace_first([1]) == [1]
    assert replace_first([]) == []