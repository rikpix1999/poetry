def checkio2(data: list) -> list:
    # your code here
    newlist=[]
    for item in data:
        if data.count(item)>1:
            newlist.append(item)
        
            
    return newlist