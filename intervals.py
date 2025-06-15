intervals = [[1,3], [6,9], [8,10], [15,18]]

for start, _ in intervals:
    print(start)

print(intervals.index([6,9]))

left=0
target=[8,10]
right=len(intervals)-1

while left<=right:
    mid=(left+right)//2

    if target==intervals[mid]:
        print(intervals[mid][0])
        break
    elif left<=mid:
        left+=1
    else:
        right-=1
    