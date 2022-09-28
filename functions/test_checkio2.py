def checkio2(data: list) -> list:
    # your code here
    newlist=[]
    for item in data:
        if data.count(item)>1:
            newlist.append(item)
        
            
    return newlist
def test_checkio2():
    assert checkio2([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
    assert checkio2([1, 2, 3, 4, 5]) == []
    assert checkio2([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert checkio2([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]