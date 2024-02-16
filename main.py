import os
from cvzone.HandTrackingModule import HandDetector

import cv2

x2 = ['Latte', 'Black Coffee', 'Tea', 'Sugar one teaspoon', 'Sugar two teaspoon', 'No Sugar', 'Small',
      'Medium', 'Large'] #list of options


def man(x, y, z):
    global a1
    global a2
    global a3
    a1 = x - 1
    a2 = y + 2
    a3 = z + 5


def video_camera():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    imgBackground = cv2.imread("Resources/Background.png")

    # importing all the mode images to a list
    folderPathModes = "Resources/Modes"
    listImgModesPath = os.listdir(folderPathModes)
    listImgModes = []
    for imgModePath in listImgModesPath:
        listImgModes.append(cv2.imread(os.path.join(folderPathModes, imgModePath)))

    # importing all the icons to a list
    folderPathIcons = "Resources/Icons"
    listImgIconsPath = os.listdir(folderPathIcons)
    listImgIcons = []
    for imgIconsPath in listImgIconsPath:
        listImgIcons.append(cv2.imread(os.path.join(folderPathIcons, imgIconsPath)))

    modeType = 0  # for changing selection mode
    selection = -1
    counter = 0
    selectionSpeed = 12
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    modePositions = [(1136, 196), (1000, 384), (1136, 581)]
    counterPause = 0
    selectionList = [-1, -1, -1]

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)
        imgBackground[139:139 + 480, 50:50 + 640] = img
        imgBackground[0:720, 847: 1280] = listImgModes[modeType]

        if hands and counterPause == 0 and modeType < 3:
            # Hand 1
            hand1 = hands[0]
            fingers1 = detector.fingersUp(hand1)

            if fingers1 == [0, 1, 0, 0, 0]:
                if selection != 1:
                    counter = 1
                selection = 1
            elif fingers1 == [0, 1, 1, 0, 0]:
                if selection != 2:
                    counter = 1
                selection = 2
            elif fingers1 == [0, 1, 1, 1, 0]:
                if selection != 3:
                    counter = 1
                selection = 3
            else:
                selection = -1
                counter = 0

            if counter > 0:
                counter += 1

                cv2.ellipse(imgBackground, modePositions[selection - 1], (103, 103), 0, 0,
                            counter * selectionSpeed, (0, 255, 0), 20)
                if counter * selectionSpeed > 360:
                    selectionList[modeType] = selection
                    modeType += 1
                    counter = 0
                    selection = -1
                    counterPause = 1

        # To pause after each selection is made
        if counterPause > 0:
            counterPause += 1
            if counterPause > 20:
                counterPause = 0

        # Add selection icon at the bottom
        if selectionList[0] != -1:
            imgBackground[636:636 + 65, 133:133 + 65] = listImgIcons[selectionList[0] - 1]
        if selectionList[1] != -1:
            imgBackground[636:636 + 65, 340:340 + 65] = listImgIcons[2 + selectionList[1]]
        if selectionList[2] != -1:
            imgBackground[636:636 + 65, 542:542 + 65] = listImgIcons[5 + selectionList[2]]

        cv2.imshow("Background", imgBackground)
        key = cv2.waitKey(1)
        if key == ord('e'):
            man(selectionList[0], selectionList[1], selectionList[2])
        if key == ord('q'):
            return


x22 = input("whats your name")
# txt file x22 :
print(x2)
video_camera()
print(x2[a1])
print(x2[a2])
print(x2[a3])

with open("orders.txt", "a") as f:
    f.write(x22)
    f.write(": ")
    f.write(x2[a1])
    f.write(', ')
    f.write(x2[a2])
    f.write(', ')
    f.write(x2[a3])
    f.write('\n')
