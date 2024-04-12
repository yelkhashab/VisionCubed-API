import cv2
import numpy as np
import base64
import math

def processImage(encodedImage):
    decodedImage = np.frombuffer(base64.b64decode(encodedImage), dtype=np.uint8)
    reconstructedImage = cv2.imdecode(decodedImage, 1)
    labImage = cv2.cvtColor(reconstructedImage, cv2.COLOR_BGR2LAB)

    croppedImage = labImage[17:161, 45:189]

    return croppedImage

def calculateCenterColors(faceIndex, centerColors, centerPiece):
    centerPoint = centerPiece[24, 24]
    normalizedCenterPoint = (centerPoint[0] / 2.55,
                             centerPoint[1] - 128,
                             centerPoint[2] - 128)

    faceOrder = ["R", "B", "O", "G", "W", "Y"]
    centerColors[faceOrder[faceIndex]] = normalizedCenterPoint

def findClosestColor(targetSquare, referenceColors):
    closestColor = ""
    minDistance = math.inf

    targetPoint = targetSquare[24, 24]
    normalizedTargetPoint = (targetPoint[0] / 2.55,
                             targetPoint[1] - 128,
                             targetPoint[2] - 128)

    for color, referencePoint in referenceColors.items():
        distance = math.sqrt(((referencePoint[0] - normalizedTargetPoint[0]) ** 2) +
                             ((referencePoint[1] - normalizedTargetPoint[1]) ** 2) +
                             ((referencePoint[2] - normalizedTargetPoint[2]) ** 2))

        if distance < minDistance:
            minDistance = distance
            closestColor = color

    return closestColor

def extractCubeState(encodedImages):
    faceColors = [[[None] * 3 for _ in range(3)] for _ in range(6)]
    centerColors = {}

    for faceIndex in range(6):
        faceImage = processImage(encodedImages[faceIndex])

        centerPiece = faceImage[48:96, 48:96]
        calculateCenterColors(faceIndex, centerColors, centerPiece)

    for faceIndex in range(6):
        faceImage = processImage(encodedImages[faceIndex])

        for row in range(3):
            for col in range(3):
                square = faceImage[(row * 48):((row + 1) * 48), (col * 48):((col + 1) * 48)]
                faceColors[faceIndex][row][col] = findClosestColor(square, centerColors)

    cubeState = {
        'F': faceColors[0][0] + faceColors[0][1] + faceColors[0][2],
        'R': faceColors[1][0] + faceColors[1][1] + faceColors[1][2],
        'B': faceColors[2][0] + faceColors[2][1] + faceColors[2][2],
        'L': faceColors[3][0] + faceColors[3][1] + faceColors[3][2],
        'U': faceColors[4][0] + faceColors[4][1] + faceColors[4][2],
        'D': faceColors[5][0] + faceColors[5][1] + faceColors[5][2],
    }

    return cubeState