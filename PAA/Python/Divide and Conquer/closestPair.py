import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceToPoint(self, other):
        return math.dist((self.x, self.y), (other.x, other.y))

    def __repr__(self):
        return f"{self.x}, {self.y}"


# Retorna os points e a distancia
def merge(firstHalf, secondHalf, lowestDistance) -> int:
    hyperplaneCoordX = (firstHalf[-1].x + secondHalf[0].x) / 2
    
    insideHyperplaneBuffer = []
    for point in (firstHalf + secondHalf):
        if abs(point.x - hyperplaneCoordX) <= lowestDistance:
            insideHyperplaneBuffer.append(point)

    insideHyperplaneBuffer.sort(key=lambda point: point.y) # Ordena por Y

    # Como os pontos estão ordenados por Y e o X já é garantido de estar dentro do buffer do hyperplano,
    # então é possível cortar as iterações antes de testar tudo caso o a distância calculada seja menor que
    # o lowestDistance. Isso porque o Y dos pontos só se distancia mais e mais, então se um ponto já não é menor que
    # lowestDistance, então o próximo também não vai ser.
    for i in range(len(insideHyperplaneBuffer)):
        for j in range(i+1, len(insideHyperplaneBuffer)):
            distance = insideHyperplaneBuffer[i].distanceToPoint(insideHyperplaneBuffer[j])
            
            if distance < lowestDistance:
                lowestDistance = distance
            else:
                break

    firstHalf.extend(secondHalf)

    return firstHalf, lowestDistance


def divide(points):
    if len(points) == 1:
        return points, float('inf')
    elif len(points) == 2:
        return points, points[0].distanceToPoint(points[1])
    

    mid  =  len(points) // 2
    firstHalf,  dist1 = divide(points[ : mid])
    secondHalf, dist2 = divide(points[mid : ])
    
    lowestDistance = dist1 if dist1 < dist2 else dist2

    return merge(firstHalf, secondHalf, lowestDistance)  # Merge the two halves


    
def main():
    points = [
        Point(100, 100),
        Point(50, 50),
        Point(0, 0),
        Point(0, 10),
        Point(0, 20),
        Point(0, 30),
        Point(0, 2)
]

    points.sort(key=lambda point: point.x) #Ordena por X
    
    print(divide(points)[1])


if __name__ == '__main__':
    main()