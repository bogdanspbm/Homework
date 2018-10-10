from memory_profiler import *


@profile
def startRecFactorial(varint):
   return recFactorial(varint)

def recFactorial(varint):
    if varint <= 1:
        return 1
    else:
        return varint*recFactorial(varint-1)


@profile
def loopFactorial(varint):
    res = 1
    for i in range(varint):
        res *= (i+1)
    return res


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    vartime = time.process_time()
    startRecFactorial(1000)
    print(time.process_time()-vartime)
