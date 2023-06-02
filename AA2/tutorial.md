Display the Count of Objects Detected from a Single Class
=========================================================

In this activity, you will learn to display the count of objects detected in a similar class.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10482742/pasted-from-clipboard.png" width = "480" height = "320">

Follow the given steps to complete this activity:

1. ### Count the number of detected objects
* Open the main.py file.

* Create detectionCount list to store count for each class.

    `detectionCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]`

* Increment the count at the same index as that of the classIds inside the for loop.

    `detectionCount[classIds[i]] = detectionCount[classIds[i]] + 1`

* Set the initial x and y coordinates for the text of the counter.

    `x = 10 y = 40`

* Set the color for the counter text.

    `color = (0, 0, 255)`

* Use a for loop to loop through the detectionCount index.

    `for i in range(len(detectionCount)):`

* Check if detectionCount is greater than 0.
    `if (detectionCount[i] > 0):`

* Create a text with the name of the label and the count for the label.

    `text = str(labels[i]) + ":" + str(detectionCount[i])`

* Set the text at the defined x and y coordinates.

    `cv2.putText(image, text, (x, y), font, 1, color, 3)`

* Increment y so that next class text appears below the current one.

    `y = y + 30`

* Save and run the code to check the output.
