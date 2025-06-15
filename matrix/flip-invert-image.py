def flipAndInvertImage(image: List[List[int]]):
    for row in image:
        print(row[::-1])
    

    return [[1 - bit for bit in row[::-1]] for row in image]

    """
    :type image: List[List[int]]
    :rtype: List[List[int]]
    """
image = [
    [1,1,0],
    [0,1,1],
    [0,0,1]]

flipAndInvertImage(image)
