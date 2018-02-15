# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check': self.ind = int(query[1])
        else: self.s = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [list() for i in range(bucket_count)] 

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def read_query(self):
        return Query(input().split())

    def _has_key(self, O):
        L = self.elems[self._hash_func(O)]
        for v in L:
            if v == O: return "yes"
        return "no"
    
    def _get(self, O, L):
        for i, v in enumerate(L):
            if v == O: return i
        return -1
    
    def _set(self, O):
        L = self.elems[self._hash_func(O)]
        for v in L:
            if v == O: return
        L.insert(0, O)
    
    def process_query(self, query):
        if query.type == "check":
            print(' '.join(self.elems[query.ind]))            
        if query.type == "add":
            self._set(query.s)
        if query.type == "del":
            L = self.elems[self._hash_func(query.s)]
            if not L: return
            i = self._get(query.s, L)
            if i >= 0: L.pop(i)
        if query.type == "find":
            print(self._has_key(query.s))

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()