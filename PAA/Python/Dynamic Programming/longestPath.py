# Longest path in graph
from collections import defaultdict

adjacencyList = defaultdict(list)
adjacencyList[1] = [2, 3]
adjacencyList[2] = [7]
adjacencyList[3] = [4]
adjacencyList[4] = [5]
adjacencyList[5] = [6]
adjacencyList[6] = [7]

cache = [ 0 ] * 7

for i in range(len(adjacencyList)+1):
    neighbors = adjacencyList[i]
    for j in neighbors:
        cache[j-1] = max(1, cache[i-1]+1, cache[j-1])

print(max(cache))