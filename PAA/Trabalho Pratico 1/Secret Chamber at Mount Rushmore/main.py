# Solução Beecrowd 2646 https://judge.beecrowd.com/en/problems/view/2646

nTranslations, nWordPairs = input().split(' ')
translate = dict()

for _ in range(int(nTranslations)):
    first, second = input().split(' ')
    if not first in translate:
        translate[first] = []
    translate[first].append(second)


for _ in range(int(nWordPairs)):
    first, second = input().split(' ')
    if first == second:
        print("yes")
    elif len(first) != len(second):
        print("no")
    else:
        checkedLetters = set()
        success = True
        for firstLetter, secondLetter in zip(first, second):
            if firstLetter == secondLetter:
                continue

            stack      = []
            foundMatch = False
            checkedLetters.clear()

            [stack.append(value) for value in translate.get(firstLetter, [])]

            while stack:
                firstLetter = stack.pop(0)
                if firstLetter == secondLetter:
                    foundMatch = True
                    break
                if firstLetter not in checkedLetters:
                    [stack.append(value) for value in translate.get(firstLetter, [])]

                checkedLetters.add(firstLetter)

            if not foundMatch:
                print("no")
                success = False
                break
        if success:
            print("yes")