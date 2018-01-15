# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.depths = [None for i in range(self.n)]

    def node_height(self, node):
        parent = self.parent[node]
        self.depths[node] = self.depths[parent] + 1
        children = self.children[node]
        if children:
            for child in children:
                self.node_height(child) 
    
    def compute_height(self):
        nodes = [list() for i in range(self.n)]
        for child_index in range(self.n):
            parent_index = self.parent[child_index]
            if parent_index == -1: self.root = child_index
            else: nodes[parent_index].append(child_index)
        self.children = nodes
        self.depths[self.root] = 1
        max_height = 0
        for child in self.children[self.root]:
            self.node_height(child)
        return max(self.depths)

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
