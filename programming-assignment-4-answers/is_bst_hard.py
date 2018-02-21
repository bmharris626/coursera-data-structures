#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def inOrderTraversal(tree, i, result, left):
    if i == -1: return
    inOrderTraversal(tree, tree[i][1], result, left)
    result.append(tree[i][0])
    left.append(tree[i][1])
    inOrderTraversal(tree, tree[i][2], result, left)

def IsBinarySearchTree(tree):
    if len(tree) == 0: return True
    result, left = list(), list()
    inOrderTraversal(tree, 0, result, left)
    # print(tree, result, left, sep="\n")
    for i in range(1, len(tree)):
        if (result[i] < result[i-1]): return False
        if (result[i] == result[i-1]) and (left[i] != -1): return False
    return True

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
