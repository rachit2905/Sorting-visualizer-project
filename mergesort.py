import time


def merge_sort(data, drawData, timetick):
    merge_sort_algo(data, 0, len(data)-1, drawData, timetick)


def merge_sort_algo(data, left, right, drawData, timetick):
    if left < right:
        middle = (left+right)//2
        merge_sort_algo(data, left, middle, drawData, timetick)
        merge_sort_algo(data, middle+1, right, drawData, timetick)
        merge(data, left, middle, right, drawData, timetick)


def merge(data, left, middle, right, drawData, timetick):
    drawData(data, getcolorarray(len(data), left, middle, right))
    time.sleep(timetick)
    leftpart = data[left:middle+1]
    rightpart = data[middle+1:right+1]
    leftidx = rightidx = 0
    for dataidx in range(left, right):
        if leftidx < len(leftpart) and rightidx < len(rightpart):
            if leftpart[leftidx] <= rightpart[rightidx]:
                data[dataidx] = leftpart[leftidx]
                leftidx += 1
            else:
                data[dataidx] = rightpart[rightidx]
                rightidx += 1
        elif leftidx < len(leftpart):
            data[dataidx] = leftpart[leftidx]
            leftidx += 1
        else:
            data[dataidx] = rightpart[rightidx]
            rightidx += 1
    drawData(data, ['green' if x >= left and x <=
             right else "white" for x in range(len(data))])
    time.sleep(timetick)


def getcolorarray(length, left, middle, right):
    colorArray = []
    for i in range(length):
        if i >= left and i < right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("orange")
        else:
            colorArray.append("white")
    return colorArray
