Detect the Object 
=========================

In this activity, you will learn to detect the objects from an image and highlight them by drawing the boxes around it.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10459399/pasted-from-clipboard.png" width = "180" height = "320">


Follow the given steps to complete this activity:
1. ### Add label and confidence percentage


* Open the main.py file.

*  Apply Non Maxima Suppression to remove overlapping bounding boxes.

    `indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidenceThreshold, NMSThreshold)`

* Write condition to check the i is in indexes.

    `if i in indexes:`

* Define the font style.

    `font = cv2.FONT_HERSHEY_SIMPLEX`



* Declare a variable label and set detected object class ID as value.


    `label = labels[classIds[i]]
`


* Declare the text variable using the format() and pass label and confidence as its parameter to display the label and confidence percentage.


    `text = '{}: {:.2f}'.format(label, confidences[i]*100)`

* Use cv2.putText() to display the label on the image.

   `cv2.putText(image, text, (x, y - 5), font, 0.5, color, 1)`
 
* Save and run the code to check the output.


