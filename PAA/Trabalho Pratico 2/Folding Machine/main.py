# Solução Beecrowd 1470 - https://judge.beecrowd.com/en/problems/view/1470

def fold(tape, foldPosition):
    firstPart  = tape[0 : foldPosition]
    secondPart = tape[foldPosition : ]
    secondPart.reverse()


    sizeDiff = len(secondPart) - len(firstPart)
    if sizeDiff > 0:
        firstPart  = [0] * sizeDiff + firstPart
    else:
        secondPart = [0] * (-sizeDiff) + secondPart

    foldedList = [ x+y for x,y in zip(secondPart, firstPart) ]
    return foldedList


def testFold(inputTape, outputTape):
    if  inputTape == outputTape or\
        list(reversed(inputTape)) == outputTape:
        return True

    # A fita só pode diminuir a cada dobra. Se ela ficar menor que a outputTape, não precisa continuar
    if len(outputTape) > len(inputTape):
        return False
    
    # Se a soma total der diferente, já sabemos que não é possível nenhuma combinação.
    if sum(outputTape) != sum(inputTape):
        return False
    
    # A cada dobra, os numeros so aumentam. Se o maior elemento de outputTape for menor que o de inputTape, é porque
    # fizemos dobras demais.
    if max(outputTape) < max(inputTape):
        return False

    for i in range(1, len(inputTape)):
        currentTest = fold(inputTape, i)
        if testFold(currentTest, outputTape):
            return True

    return False
    
try:
    while True:
        inputTapeSize  = int(input())
        inputTape      = list(map(int, input().split()))

        outputTapeSize = int(input())
        outputTape     = list(map(int, input().split()))

        isPossible = testFold(inputTape, outputTape)
        if isPossible:
            print("S")
        else:
            print("N")
except EOFError:
    pass