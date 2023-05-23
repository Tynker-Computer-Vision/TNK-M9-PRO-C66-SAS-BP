import numpy as np
import cv2

# Set confidence thresholds
confidenceThreshold = 0.5

modelConfiguration = 'cfg/yolov3.cfg'
modelWeights = 'yolov3.weights'

# Path to labels file


# Load labels from file


yoloNetwork = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

image = cv2.imread('static/img1.jpg')

dimensions = image.shape[:2]
H = dimensions[0]
W = dimensions[1]


blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416))
yoloNetwork.setInput(blob)


# Get names of unconnected output layers


# Forward pass through network
# Replace the list yoloNetwork and forward the layerName with yoloNetwork
layerOutputs = []


# Initialize lists to store bounding boxes, confidences, and class Ids
boxes = []
confidences = []
classIds = []


# Process each output from YOLO network
for output in layerOutputs:
    for detection in output:
        # Get class scores and ID of class with highest score

        # If confidence threshold is met, save bounding box coordinates and class Id
        # Uncomment the below code
        '''
        if confidence > confidenceThreshold:
            box = detection[0:4] * np.array([W, H, W, H])
            (centerX, centerY,  width, height) = box.astype('int')
            x = int(centerX - (width))
            y = int(centerY - (height))

        '''


for i in range(len(boxes)):
    x = boxes[i][0]
    y = boxes[i][1]
    w = boxes[i][2]
    h = boxes[i][3]

    # default red color
    color = (0, 0, 255)

    cv2.rectangle(image, (x, y), (x + h, y + w), color, 3)

cv2.imshow('Image', image)
cv2.waitKey(0)
