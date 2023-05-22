import numpy as np
import cv2

confidenceThreshold = 0.5
NMSThreshold = 0.3

modelConfiguration = 'cfg/yolov3.cfg'
modelWeights = 'yolov3.weights'

labelsPath = 'coco.names'

labels = open(labelsPath).read().strip().split('\n')

yoloNetwork = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

image = cv2.imread('static/img1.jpg')

dimensions = image.shape[:2]
H = dimensions[0]
W = dimensions[1]

blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416))
yoloNetwork.setInput(blob)

layerName = yoloNetwork.getUnconnectedOutLayersNames()

layerOutputs = yoloNetwork.forward(layerName)

boxes = []
confidences = []
classIds = []

# Create detectionCount list to store count for each class


for output in layerOutputs:
    for detection in output:
        scores = detection[5:]
        classId = np.argmax(scores)
        confidence = scores[classId]

        if confidence > confidenceThreshold:
            box = detection[0:4] * np.array([W, H, W, H])
            (centerX, centerY,  width, height) = box.astype('int')
            x = int(centerX - (width/2))
            y = int(centerY - (height/2))

            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            classIds.append(classId)

indexes = cv2.dnn.NMSBoxes(
    boxes, confidences, confidenceThreshold, NMSThreshold)


font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(len(boxes)):
    if i in indexes:
        x = boxes[i][0]
        y = boxes[i][1]
        w = boxes[i][2]
        h = boxes[i][3]

        label = labels[classIds[i]]

        # Increment the count at same index as that of the classIds

        color = (0, 150, 0)

        if (label == "person"):
            color = (0, 150, 0)
        if (label == "bench"):
            color = (150, 0, 0)
        if (label == "bicycle"):
            color = (0, 0, 150)

        cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
        text = '{}: {:.2f}'.format(label, confidences[i]*100)
        cv2.putText(image, text, (x, y - 5), font, 1, color, 3)

# Set initial location of the text for counter


# Set color of counter text


# Loop through detectionCount index

    # Check if detectionCount is greater then 0

        # Add text at location x,y

        # Increment y so that next class text appears below the current one.


cv2.imshow('Image', image)
cv2.waitKey(0)
