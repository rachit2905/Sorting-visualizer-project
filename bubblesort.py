import time


def bubble_sort(data, drawData, timetick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['blue' if x == j or x == j +
                         1 else '#A90042' for x in range(len(data))])
                time.sleep(timetick)
    drawData(data, ['green' for x in range(len(data))])
