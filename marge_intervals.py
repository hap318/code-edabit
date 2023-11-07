def merge_intervals(interval):
    i = 0
    while i < len(interval) -1:
        if interval[i][1] > interval[i+1][0]:
            interval.pop(i+1)
        else:
            i += 1
    return interval

print(merge_intervals([[1,3],[2,4],[6,9]]))
