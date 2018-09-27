def MoveArray(a):
    tmp = []
    tmp += a
    last = a[len(a) - 1]
    for i in range(len(tmp) - 1):
        tmp[len(tmp) - 1 - i] = a[len(tmp) - 2 - i]
    tmp[0] = a[len(a) - 1]
    return tmp

#print(MoveArray([1,2,3,4,5,6,7,8,9,10]))
