def getEndlessPageByCursor(dbList, pageSize, cursor=None):
    if not dbList:
        return [], None
    
    totalItems = len(dbList)
    
    if cursor is None:
        startIndex = 0
    else:
        try:
            startIndex = dbList.index(cursor)
            print(startIndex)
        except ValueError:
            startIndex = 0
    
    page = []
    nextCursor = None
    
    for i in range(pageSize):
        index = (startIndex + i) % totalItems
        page.append(dbList[index])
    
    nextCursorIndex = (startIndex + pageSize) % totalItems
    nextCursor = dbList[nextCursorIndex]
    
    return page, nextCursor

dbList = ['A', 'B', 'C', 'D', 'E', 'R', 'W']

page2, cursor2 = getEndlessPageByCursor(dbList, 9, dbList[1])
print(f"Page 2: {page2}, Next cursor: {cursor2}")
