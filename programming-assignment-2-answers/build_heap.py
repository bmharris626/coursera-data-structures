# python3

class Heap:
    
    def buildHeap(self):
        for i in range(self.size//2, -1, -1):
            self.siftDown(i)
    
    def __init__(self, array = list()):
        self.h = array
        self.size = len(array)
        self.swaps = list()
        self.buildHeap()
    
    def leftChild(self, i):
        return 2*i + 1
    
    def rightChild(self, i):
        return 2*i + 2
            
    def siftDown(self, i):
        maxIndex = i
        l = self.leftChild(i)
        if (l < self.size) and (self.h[l] < self.h[maxIndex]):
            maxIndex = l
        r = self.rightChild(i)
        if (r < self.size) and (self.h[r] < self.h[maxIndex]):
            maxIndex = r
        if i != maxIndex:
            self.h[i], self.h[maxIndex] = self.h[maxIndex], self.h[i]
            self.swaps.append([i, maxIndex])
            self.siftDown(maxIndex)

class HeapBuilder:
    
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        self.n = int(input())
        self._data = [int(s) for s in input().split()]
        assert self.n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])
            
    def GenerateSwaps(self):
        q = Heap(self._data)
        self._swaps = q.swaps

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
