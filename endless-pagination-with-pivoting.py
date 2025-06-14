dblist = [13, 5, 6, 54, 82, 39, 11, 69, 96, 32, 48, 18, 45, 77, 99]

def getPage(dbList, pivotID, pageSize, pageNum):
    startIndex = dbList.index(pivotID)
    dbList = dbList[startIndex:] + dbList[:startIndex]

    startPos = pageNum * pageSize
    endPos = startPos + pageSize

    if endPos < len(dbList):
        return dbList[startPos:endPos]
    elif startPos < len(dbList):
        return dbList[startPos:]
    else:
        return []

print("PageNum Page")
for i in range(10):
    print("{}\t{}".format(i, getPage(dblist, 69, 2, i)))