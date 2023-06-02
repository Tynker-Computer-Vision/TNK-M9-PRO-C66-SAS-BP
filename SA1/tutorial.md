Load and Display the Image
=========================

In this activity, you will learn to use the YOLO algorithm to load, process, and display an image.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10482717/SA1.png" width = "480" height = "320">


Follow the given steps to complete this activity:
1. ### Load the YOLO network
* Load a YOLO network variable and assign `cv2.dnn.readNetFromDarknet()` to load the yolo object detection network.

    `yoloNetwork = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)`


* Load and resize the `img3.png` image using `cv2.imread()` and `cv2.resize()` functions.

    `image = cv2.imread('static/img3.jpg')`

    `image = cv2.resize(image, (700, 500))`
 
* Store the image shape, height, and width dimensions of the image.

    `dimensions = image.shape[:2]`

    `H = dimensions[0]`

    `W = dimensions[1]`
 
* Create a blob from an image and set input for the YOLO network.

    `blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416))`

    `yoloNetwork.setInput(blob)`


* Render the image using cv2.imshow() and display it in a window until any key is pressed.

    `cv2.imshow('Image', image)`

    `cv2.waitKey(0)`

* Save and run the code to check the output.
