# Solução Beecrowd 1085 https://judge.beecrowd.com/en/problems/view/1085

import heapq
from collections import defaultdict


def djikstra(adjacencyList: list, srcLanguage: str, destLanguage: str, disallowedFirstLetters: dict):
    distanceFromSrc = { language : float('inf') for language in adjacencyList }
    distanceFromSrc[srcLanguage] = 0

    visitedVertices = set()
    priorityQueue   = [(0, srcLanguage, None)]
    
    while priorityQueue:
        currentLanguageDistanceToSrc, currentLanguage, previousLetter = heapq.heappop(priorityQueue)

        if currentLanguage == destLanguage:
            return distanceFromSrc[currentLanguage]

        if currentLanguage in visitedVertices:
           continue
        
        visitedVertices.add(currentLanguage)

        for neighborLanguage, linkingInfo in adjacencyList[currentLanguage].items():
            for sharedWordLength, sharedWord in linkingInfo:
                if  (sharedWord[0] == previousLetter) or\
                    (neighborLanguage in disallowedFirstLetters and sharedWord[0] in disallowedFirstLetters[neighborLanguage]):
                    continue

                distanceToNeighbor = currentLanguageDistanceToSrc + sharedWordLength

                if distanceToNeighbor < distanceFromSrc[neighborLanguage]:
                    distanceFromSrc[neighborLanguage] = distanceToNeighbor
                    heapq.heappush(priorityQueue, (distanceToNeighbor, neighborLanguage, sharedWord[0]))
    
    
    return distanceFromSrc[destLanguage] if distanceFromSrc[destLanguage] != float('inf') else "impossivel"


try:
    while(True):
        adjacencyList             = defaultdict(lambda: defaultdict(list))
        disallowedFirstLetters    = defaultdict(list)
        nLanguages                = int(input())
        srcLanguage, destLanguage = input().split(" ")

        for idx in range(nLanguages):
            src, dest, word = input().split(" ")
            word = word.replace(" ", "")
            
            heapq.heappush(adjacencyList[src][dest], (len(word), word))
            heapq.heappush(adjacencyList[dest][src], (len(word), word))

            if dest == destLanguage:
                disallowedFirstLetters[src].append(word[0])
            elif src == destLanguage:
                disallowedFirstLetters[dest].append(word[0])


        if  (srcLanguage  not in adjacencyList) or \
        (destLanguage not in adjacencyList):
            print("impossivel")
        else:
            print(djikstra(adjacencyList, srcLanguage, destLanguage, disallowedFirstLetters))


except EOFError:
    pass