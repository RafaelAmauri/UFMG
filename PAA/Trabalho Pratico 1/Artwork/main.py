# Solução Beecrowd 2962 https://judge.beecrowd.com/en/problems/view/2962

from math import dist

sizeX, sizeY, nSensors = map(int, input().split(" "))

touchingCeiling   = {k: False for k in range(nSensors)}
touchingFloor     = {k: False for k in range(nSensors)}
touchingLeftWall  = {k: False for k in range(nSensors)}
touchingRightWall = {k: False for k in range(nSensors)}

sensors = {}

for i in range(nSensors):
    sensorPosX, sensorPosY, sensorSens = map(int, input().split(" "))
    
    if sensorPosX - sensorSens <= 0:
        touchingLeftWall[i] = True
    if sensorPosX + sensorSens >= sizeX:
        touchingRightWall[i] = True

    if sensorPosY - sensorSens <= 0:
        touchingFloor[i] = True
    if sensorPosY + sensorSens >= sizeY:
        touchingCeiling[i] = True

    sensors[i] = (sensorPosX, sensorPosY, sensorSens)


for s1Id, s1Info in sensors.items():
    s1X, s1Y, s1Sens = s1Info
    for s2Id in range(s1Id+1, nSensors):
        s2X, s2Y, s2Sens = sensors[s2Id]

        if dist((s1X, s1Y), (s2X, s2Y)) <= s1Sens + s2Sens:
            if touchingCeiling[s1Id] or touchingCeiling[s2Id]:
                touchingCeiling[s2Id] = True
                touchingCeiling[s1Id] = True
            
            if touchingFloor[s1Id] or touchingFloor[s2Id]:
                touchingFloor[s1Id] = True
                touchingFloor[s2Id] = True
            
            if touchingLeftWall[s1Id] or touchingLeftWall[s2Id]:
                touchingLeftWall[s1Id] = True
                touchingLeftWall[s2Id] = True
            
            if touchingRightWall[s1Id] or touchingRightWall[s2Id]:
                touchingRightWall[s1Id] = True
                touchingRightWall[s2Id] = True


pathExists = True
for sId in sensors.keys():
    if touchingCeiling[sId] and touchingFloor[sId]:
        pathExists = False
        break
    if touchingCeiling[sId] and touchingRightWall[sId]:
        pathExists = False
        break
    if touchingLeftWall[sId] and touchingRightWall[sId]:
        pathExists = False
        break
    if touchingLeftWall[sId] and touchingFloor[sId]:
        pathExists = False
        break

if pathExists:
    print("S")
else:
    print("N")