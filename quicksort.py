import time


def partition(data, head, tail, drawData, timetick):
    border = head
    pivot = data[tail]
    drawData(data, getcolorArray(len(data), head, tail, border, border))
    time.sleep(timetick)
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getcolorArray(
                len(data), head, tail, border, j, True))
            time.sleep(timetick)
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, getcolorArray(len(data), head, tail, border, j))
        time.sleep(timetick)

    drawData(data, getcolorArray(len(data), head, tail, border, tail, True))
    time.sleep(timetick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawData, timetick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timetick)
        quick_sort(data, head, partitionIdx-1, drawData, timetick)
        quick_sort(data, partitionIdx+1, tail, drawData, timetick)


def getcolorArray(dataLen, head, tail, border, currentIdx, isSwapping=False):
    colorArray = []
    for i in range(dataLen):
        if(i >= head and i <= tail):
            colorArray.append("gray")
        else:
            colorArray.append("white")
    if(i == tail):
        colorArray[i] = "red"
    elif i == border:
        colorArray = "blue"
    elif i == currentIdx:
        colorArray = "yellow"
    if isSwapping:
        if i == border or i == currentIdx:
            colorArray[i] = "green"
    return colorArray
