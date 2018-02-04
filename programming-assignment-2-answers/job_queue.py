# python3

class Heap:
    
    def buildHeap(self):
        for i in range(self.size//2, -1, -1):
            self.siftDown(i)
    
    def __init__(self, array = list()):
        self.h = array
        self.size = len(array)
        self.buildHeap()
            
    def parent(self, i):
        return (i-1)//2
    
    def leftChild(self, i):
        return 2*i + 1
    
    def rightChild(self, i):
        return 2*i + 2
    
    def siftUp(self, i):
        while (
            (i > 0) and (
                (self.h[self.parent(i)][1] > self.h[i][1]) or (
                    (self.h[self.parent(i)][1] == self.h[i][1]) and 
                    (self.h[self.parent(i)][0] > self.h[i][0])
            ))):
            self.h[self.parent(i)], self.h[i] = self.h[i], self.h[self.parent(i)]
            i = self.parent(i)
            
    def siftDown(self, i):
        maxIndex = i
        l = self.leftChild(i)
        if (
            (l < self.size) and (
                (self.h[l][1] < self.h[maxIndex][1]) or (
                    (self.h[l][1] == self.h[maxIndex][1]) and 
                    (self.h[l][0] < self.h[maxIndex][0])
            ))): maxIndex = l
        r = self.rightChild(i)
        if (
            (r < self.size) and (
                (self.h[r][1] < self.h[maxIndex][1]) or (
                    (self.h[r][1] == self.h[maxIndex][1]) and 
                    (self.h[r][0] < self.h[maxIndex][0])
            ))): maxIndex = r
        if i != maxIndex:
            self.h[i], self.h[maxIndex] = self.h[maxIndex], self.h[i]
            self.siftDown(maxIndex)
            
    def insert(self, p):
        self.size += 1
        self.h.append(p)
        self.siftUp(len(self.h)-1)
        
    def extractMin(self):
        self.h[0], self.h[self.size-1] = self.h[self.size-1], self.h[0]
        result = self.h.pop()
        self.size -= 1
        if self.size > 0:
            self.siftDown(0)
        return result

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.n = len(self.jobs)
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(self.n):
            print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        self.assigned_workers = list()
        self.start_times = list()
        threads = Heap([])
        i = 0
        while (i < self.num_workers) and (len(self.jobs) > 0):
            self.assigned_workers.append(i)
            self.start_times.append(0)
            t = self.jobs.pop(0)
            if t > 0: 
                threads.insert((i, t))
                i += 1
        for i in range(len(self.jobs)):
            mn = threads.extractMin()
            self.assigned_workers.append(mn[0])
            self.start_times.append(mn[1])
            threads.insert((mn[0], mn[1] + self.jobs.pop(0)))
            
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()