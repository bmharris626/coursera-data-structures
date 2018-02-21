# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(S, p, x):
    hsh = 0
    for c in reversed(S):
        hsh = (hsh * x + ord(c)) % p
    return hsh

def PrecomputeHashes(T, P, p, x):
    H = [None for i in range(len(T)-len(P)+1)]
    S = T[len(T)-len(P):len(T)]
    H[len(T)-len(P)] = PolyHash(S, p, x)
    y = 1
    for i in range(1, len(P)+1):
        y = (y * x) % p
    for i in range(len(T)-len(P)-1, -1, -1):
        H[i] = (x*H[i+1] + ord(T[i]) - y * ord(T[i+len(P)])) % p
    return H

def RubinKarp(P, T):
    p = 1000000007
    x = random.randint(1, p-1)
    result = list()
    H = PrecomputeHashes(T, P, p, x)
    pHash = PolyHash(P, p, x)
    for i in range(len(T) - len(P) +1):
        if pHash != H[i]: continue
        if T[i:i+len(P)] == P: result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(RubinKarp(*read_input()))