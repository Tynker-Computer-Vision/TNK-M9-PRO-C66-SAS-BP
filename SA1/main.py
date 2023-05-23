import cv2


# Path to model configuration and weights files
modelConfiguration = 'cfg/yolov3.cfg'
modelWeights = 'yolov3.weights'

# Load YOLO object detection network


# Load image


# Get image dimensions


# Create blob from image and set input for YOLO network
# Syntax: blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size)
# 1/255 is takes to normalise the pixel value from 0-255 to 0-1 as the yolo (other models also) require the pixel to be in range 0 to 1.
# 416,416 is size of images taken by yolo model


# Display image
