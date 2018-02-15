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
        self.elems = [list()] * bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            print(' '.join(self.elems[query.ind]))            
        if query.type == "add":
            hsh = self._hash_func(query.s)
            not_exists = True
            for i, elem in enumerate(self.elems[hsh]):
                if elem == query.s:
                    self.elems[hsh][i] = query.s
                    not_exists = False
                    break
            if not_exists: self.elems[hsh].insert(0, query.s)
        if query.type == "del":
            hsh = self._hash_func(query.s)
            for i, elem in enumerate(self.elems[hsh]):
                if elem == query.s: 
                    self.elems[hsh].pop(i)
                    break
        if query.type == "find":
            hsh = self._hash_func(query.s)
            response = "no"
            for elem in self.elems[hsh]:
                if elem == query.s: 
                    response = "yes"
                    break
            print(response) 

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()