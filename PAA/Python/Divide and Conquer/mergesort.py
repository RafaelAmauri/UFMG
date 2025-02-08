def merge(part1: list, part2: list) -> list:
    pointer1  = 0
    pointer2  = 0
    len1      = len(part1)
    len2      = len(part2)

    mergedArr = []
    # While pointer1 and pointer2 haven't reached the end of part1 and part2
    while pointer1 < len1 and pointer2 < len2:

        # Adds the smallest element between part1[pointer1] and part2[pointer2] to mergedArr[]
        if part1[pointer1] < part2[pointer2]:
            mergedArr.append(part1[pointer1])
            pointer1 += 1
        else:
            mergedArr.append(part2[pointer2])
            pointer2 += 1

    # It's possible that one of the pointers reaches the end of its respective part 
    # while the other pointer is still somewhere in the middle of the other part.

    # When this happens, simply add all the remaining elements of the part that still isn't
    # finished to mergedArr[]
    if pointer1 == len1:
        mergedArr.extend(part2[pointer2 : ])
    else:
        mergedArr.extend(part1[pointer1 : ])


    return mergedArr


def mergesort(arr: list) -> list:
    size = len(arr)
    if size == 1:
        return arr
    
    midPoint = size // 2

    part1 = mergesort(arr[ : midPoint]) # Compute first half of arr and recursively call mergersort() for it
    part2 = mergesort(arr[midPoint : ]) # Do the same thing for the second half
    
    return merge(part1, part2)  # Merge the two halves


if __name__ == '__main__':
    arr = [8, 7, 6, 5, 4, 3, 2, 1]
    print(mergesort(arr))