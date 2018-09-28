def MoveArray(arr):
    if arr == []:
        return arr
    tmp = []
    tmp += arr
    last = arr[len(arr) - 1]
    for i in range(len(tmp) - 1):
        tmp[len(tmp) - 1 - i] = arr[len(tmp) - 2 - i]
    tmp[0] = arr[len(arr) - 1]
    return tmp

print(MoveArray([]))
