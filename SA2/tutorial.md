Highlight the Objects
=========================

In this activity, you will learn to highlight the identified object, add label, and confidence percentage to it.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10459185/pasted-from-clipboard.png" width = "480" height = "320">


Follow the given steps to complete this activity:
1. Detect the Objects

* Get the names of the unconnected layers using the yoloNetwork.getUnconnectedOutLayersNames() method.
* Get the unconnected layer outputs using yoloNetwork.forward(layerName).

    `layerName = yoloNetwork.getUnconnectedOutLayersNames()`

    `layerOutputs = yoloNetwork.forward(layerName)`


* Initialize the lists to store bounding `boxes, confidences`, and `classIds`.

    `boxes = []`

    `confidences = []`

    `classIds = []`


* Detect the score using detection.  
* Get the `classId` using the `np.argmax()`.
* Store the `confidence` value using the scores method.

    `scores = detection[5:]`

    `classId = np.argmax(scores)`

    `confidence = scores[classId]`


2. ### Store the box information
    `oilImg = cv2.xphoto.oilPainting(orignalImage, size=7, dynRatio=1)`


* Check if the confidence is greater than confidenceThreshold using an if condition.
    
    `if confidence > confidenceThreshold:`

* Uncomment the below code.

    `box = detection[0:4] * np.array([W, H, W, H])`

    `(centerX, centerY,  width, height) = box.astype('int')`

    `x = int(centerX - (width/2))`

    `y = int(centerY - (height/2))`



* Append the coordinates and dimensions of the box in the boxes list.

    `boxes.append([x, y, int(width), int(height)])`

* Append the confidence of prediction in the confidences list.
    
    `confidences.append(float(confidence))`

* Append the classId in the classIds list.

    `classIds.append(classId)`


* Try changing the value of RGB to set the green color to the box ( default color is red).

    `color = (0,0,255)`

* Play with the values of the box to draw the proper rectangle around the detected object.

    `cv2.rectangle(image, (x, y), (x + w, y + h), color, 1)`

* Save and run the code to check the output.
