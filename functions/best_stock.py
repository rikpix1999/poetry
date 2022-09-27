def best_stock(data: dict[str, float]) -> str:
    
    return max(data, key = data.get)
