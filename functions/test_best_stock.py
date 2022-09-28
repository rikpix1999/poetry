def best_stock(data: dict[str, float]) -> str:
    
    return max(data, key = data.get)

def test_best_stock():
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"